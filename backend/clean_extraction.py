# -*- coding: utf-8 -*-
"""
Nettoie les artefacts propres à l'extraction de texte depuis les PDF
du cours :
  - en-têtes / pieds de page répétés à chaque page ("14 CHAPITRE 2. ...",
    "2.2. ELÉMENTS DE TOPOLOGIE DANS R" + numéro de page collé)
  - exposants coupés sur la ligne suivante ("R" puis "2" -> "R²")

Ce nettoyage se fait une fois, sur le texte brut, avant le découpage
en paragraphes et l'indexation.
"""
import re

SUPERSCRIPT = {
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵",
    "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹",
    "n": "ⁿ", "p": "ᵖ", "N": "ᴺ", "P": "ᴾ",
    "+": "⁺", "-": "⁻",
}
SUP_TOKEN_RE = re.compile(r"^(?=[0-9npNP+\-]*[0-9npNP])[0-9npNP+\-]{1,2}$")
# lettres d'indice de sommation/produit : toujours des indices (jamais des
# exposants) dans ce cours -> pas d'ambiguïté contrairement à "n"/"p"/un chiffre
SUBSCRIPT = {
    "i": "ᵢ", "j": "ⱼ", "k": "ₖ", "l": "ₗ", "m": "ₘ", "n": "ₙ", "p": "ₚ",
    "0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄",
    "5": "₅", "6": "₆", "7": "₇", "8": "₈", "9": "₉",
}
INDEX_LETTER_RE = re.compile(r"^[ijklm]$")
# "∂fi", "∂xj", "∂fn", "∂f1", "∂x12" sur UNE seule ligne (contrairement aux
# cas coupés par un saut de ligne) : sans ambiguïté car "∂" n'apparaît
# jamais dans un mot français, donc pas de risque de confondre avec
# "affine", "modifie", etc.
PARTIAL_DERIV_INDEX_RE = re.compile(r"∂([a-zA-Z])([ijklmnp]|\d{1,2})\b")
# l'exposant peut aussi être seulement en tête de la ligne suivante,
# suivi du reste de la phrase sur la même ligne ("n dans R occupe...")
SUP_TOKEN_LEADING_RE = re.compile(r"^((?=[0-9npNP+\-]*[0-9npNP])[0-9npNP+\-]{1,2})(\s+(\S.*))?$")
# la ligne précédente se termine par un "socle" (R, x, kxk, ...) auquel
# l'exposant de la ligne suivante doit se raccrocher, sans faire partie
# d'un mot plus long (d'où la frontière \b devant)
BASE_END_RE = re.compile(r"(?:\b(?:k[a-zA-Zα-ωΑ-Ω]+k|[A-Za-zα-ωΑ-Ω]))$")

CHAPTER_HEADER_RE = re.compile(r"^\d+\s*(CHAPITRE|ANNEXE)\s+[A-Z\d]", re.IGNORECASE)
NUMBERED_UPPER_RE = re.compile(
    r"^\d+(\.\d+)*\.?\s+[A-ZÉÈÀÂÊÎÔÛ0-9][A-ZÉÈÀÂÊÎÔÛ0-9\s\.'’ÊÇ]+$"
)
# même en-tête, mais avec un numéro de page collé sans saut de ligne à la fin
TRAILING_PAGENUM_RE = re.compile(r"^(.*[A-ZÉÈÀÂÊÎÔÛ])\s+\d{1,4}$")
PAGE_NUM_ARTIFACT_RE = re.compile(r"^[A-Za-zα-ωΑ-Ω∗]{0,4}\s*\d{1,4}$")


def merge_superscripts(lines):
    out = []
    i = 0
    while i < len(lines):
        cur = lines[i]
        cur_stripped = cur.rstrip()
        nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
        if cur_stripped and BASE_END_RE.search(cur_stripped) and SUP_TOKEN_RE.match(nxt):
            sup = "".join(SUPERSCRIPT.get(ch, ch) for ch in nxt)
            # cas "x\n2\ni" = x_i au carré : le "i" (indice de somme) qui suit
            # se rattache en indice à la base, pas en nouvel exposant
            nxt2 = lines[i + 2].strip() if i + 2 < len(lines) else ""
            if INDEX_LETTER_RE.match(nxt2):
                out.append(cur_stripped + SUBSCRIPT[nxt2] + sup)
                i += 3
                continue
            out.append(cur_stripped + sup)
            i += 2
            continue

        # cas "x\ni" direct (sans exposant intermédiaire) : x_i
        if cur_stripped and BASE_END_RE.search(cur_stripped) and INDEX_LETTER_RE.match(nxt):
            out.append(cur_stripped + SUBSCRIPT[nxt])
            i += 2
            continue

        m = SUP_TOKEN_LEADING_RE.match(nxt) if (cur_stripped and BASE_END_RE.search(cur_stripped)) else None
        if m and len(nxt) <= 60:  # évite de confondre avec une vraie ligne qui commence juste par un chiffre
            sup = "".join(SUPERSCRIPT.get(ch, ch) for ch in m.group(1))
            rest = m.group(3) or ""
            out.append(cur_stripped + sup + (" " + rest if rest else ""))
            i += 2
            continue

        out.append(lines[i])
        i += 1
    return out


def strip_running_headers(lines):
    seen_headers = set()
    out = []
    skip_next_if_page_artifact = False
    for line in lines:
        stripped = line.strip()

        if skip_next_if_page_artifact:
            skip_next_if_page_artifact = False
            if PAGE_NUM_ARTIFACT_RE.match(stripped):
                continue  # numéro de page / résidu d'exposant collé au header

        if CHAPTER_HEADER_RE.match(stripped):
            continue  # "14 CHAPITRE 2. ..." : en-tête de page, toujours du bruit

        # normalise en retirant un éventuel numéro de page collé en fin de ligne,
        # pour reconnaître la même en-tête même si le numéro de page diffère
        m = TRAILING_PAGENUM_RE.match(stripped)
        normalized = m.group(1) if (m and NUMBERED_UPPER_RE.match(m.group(1))) else stripped

        if NUMBERED_UPPER_RE.match(normalized):
            if normalized in seen_headers:
                skip_next_if_page_artifact = True
                continue  # répétition = en-tête de page, pas un vrai titre
            seen_headers.add(normalized)
            if m and normalized != stripped:
                out.append(normalized)  # on garde le titre, sans le numéro de page collé
                continue

        out.append(line)
    return out


CONTROL_CHAR_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\ue000-\uf8ff]")


def strip_control_chars(text):
    """Retire les caractères de contrôle résiduels (glyphes de grandes
    parenthèses/accolades de matrices mal extraits) qui s'affichent
    comme des carrés vides dans un navigateur."""
    return CONTROL_CHAR_RE.sub("", text)


def fix_inline_partial_derivative_indices(text):
    def repl(m):
        idx = "".join(SUBSCRIPT[ch] for ch in m.group(2))
        return "∂" + m.group(1) + idx
    return PARTIAL_DERIV_INDEX_RE.sub(repl, text)


def clean_text(text):
    lines = text.split("\n")
    lines = strip_running_headers(lines)
    lines = merge_superscripts(lines)
    cleaned = strip_control_chars("\n".join(lines))
    return fix_inline_partial_derivative_indices(cleaned)


LIST_MARKER_RE = re.compile(r"^(\d+[.)]|\(?[a-z]\)|[-•∀∃])\s")
PURE_ELLIPSIS_RE = re.compile(r"^[.\s⋮⋯…]+$")


def is_formula_line(line):
    """Heuristique : une ligne dominée par des symboles (peu de lettres)
    est probablement une formule affichée plutôt que de la prose."""
    stripped = line.strip()
    if not stripped:
        return False
    letters = sum(ch.isalpha() for ch in stripped)
    return (letters / len(stripped)) < 0.55


BARE_NUMBER_RE = re.compile(r"^\d{1,3}$")
LAST_TOKEN_NUM_RE = re.compile(r"^([(\[{])?(\d{1,3})$")
STARTS_WITH_CLOSER_RE = re.compile(r"^[,.;:)\]}]")
TIGHT_OPENER_RE = re.compile(r"[(\[{]$")  # après une vraie ouverture, pas d'espace
NEW_EQUATION_RE = re.compile(r"^[A-Za-zα-ωΑ-Ω0-9~∇∂][^=]{0,25}=(?!=)")


def smart_join(fragments):
    """Recolle des petits fragments de formule (chacun sur sa propre
    ligne dans le PDF d'origine) avec un espacement raisonnable :
    virgules/parenthèses collées, deux nombres bruts consécutifs
    reliés par '/' (fraction empilée), sinon un espace. Une nouvelle
    ligne n'est conservée que quand le fragment ressemble au début
    d'une nouvelle équation."""
    out_lines = [""]
    for frag in fragments:
        if not frag:
            continue
        if not out_lines[-1]:
            out_lines[-1] = frag
            continue
        prev = out_lines[-1]
        last_tok = prev.split()[-1] if prev.split() else ""
        m = LAST_TOKEN_NUM_RE.match(last_tok)
        if NEW_EQUATION_RE.match(frag) and not TIGHT_OPENER_RE.search(prev):
            out_lines.append(frag)
        elif m and BARE_NUMBER_RE.match(frag):
            out_lines[-1] = prev + "/" + frag
        elif STARTS_WITH_CLOSER_RE.match(frag):
            out_lines[-1] = prev + frag
        elif TIGHT_OPENER_RE.search(prev):
            out_lines[-1] = prev + frag
        else:
            out_lines[-1] = prev + " " + frag
    return "\n".join(out_lines)


def to_blocks(text):
    """Découpe un passage en blocs ('prose' | 'formula'), en recollant
    les lignes de prose qui n'étaient coupées que par la largeur de
    page du PDF d'origine, et en recollant intelligemment les
    fragments de formule (fractions empilées, ponctuation collée)."""
    blocks = []
    buf = []
    formula_frags = []

    def flush_prose():
        if buf:
            blocks.append({"type": "prose", "text": " ".join(buf)})
            buf.clear()

    def flush_formula():
        if formula_frags:
            blocks.append({"type": "formula", "text": smart_join(formula_frags)})
            formula_frags.clear()

    for raw_line in text.split("\n"):
        stripped = raw_line.strip()
        if not stripped:
            flush_prose()
            flush_formula()
            continue
        if PURE_ELLIPSIS_RE.match(stripped):
            # "...", ". . .", "⋮" : notation de matrice qui n'a plus de sens
            # une fois la structure (lignes/colonnes) perdue par la linéarisation
            continue
        if is_formula_line(stripped) or LIST_MARKER_RE.match(stripped):
            flush_prose()
            formula_frags.append(stripped)
            continue
        flush_formula()
        buf.append(stripped)
    flush_prose()
    flush_formula()
    return blocks
