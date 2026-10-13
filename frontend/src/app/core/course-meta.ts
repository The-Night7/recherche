/** Présentation des matières : symbole, domaine (couleur) et exemples de recherche. */
import { Domain } from './models';

const COURSE_SYM: Record<string, string> = {
  algebre1: '⊕', algebre2: '⊕', 'algebre-lineaire': '⊕', algebre: '⊕',
  analyse1: '∫', analyse2: '∫', 'analyse-rn': 'ℝⁿ', series: 'Σ',
  cef1: '¶', cef: '¶', ic1: '✎', shs: '§', ethique: '§', design: '✎', 'histoire-du-design': '✎',
  informatique1: '⌘', informatique2: '⌘', informatique3: '⌘', informatique4: '⌘',
  physique1: 'F', 'mecanique-du-point': '→', electromagnetisme: 'Φ', ondes: '∿', 'physique-moderne': 'Ψ',
  'projet1-s1': '◇', 'projet1-s2': '◇', projet: '◇', 'integration-proba': 'μ',
  algorithmique: '⟳', bdd: '▤', 'data-exploration': '▦', 'mesures-integration': 'μ', optimisation: '∇',
  probabilites: 'ℙ', 'programmation-procedurale': '{ }', unix: '$', informations: 'i',
  'complement-maths': '∀', 'systeme-exploitation': '>_',
  'analyse-numerique': '≈', 'data-mining': '◈', 'equations-differentielles': 'y′', 'gestion-entreprise': '€',
  'statistique-inferentielle': 'x̄', 'theorie-graphes': '⊶', 'theorie-langages': 'L',
  anglais: 'Aa', 'architecture-reseau': '⇄', 'communication-interculturelle': '@', 'decidabilite-complexite': '⊥',
  ece: '¶', 'modele-lineaire': 'β', 'optimisation-deterministe': '∇', 'programmation-fonctionnelle': 'λ',
  'traitement-signal': '∿', economie: '€', 'compressive-sensing': 'ℓ₁', 'design-decision': '◆',
  edp: '∂', ia: 'AI', 'methodes-agiles': '⟲', 'programmation-parallele': '∥', 'series-temporelles': 't',
};

const DOMAINS: Record<Exclude<Domain, 'shs'>, string> = {
  math: 'algebre1 algebre2 algebre-lineaire algebre analyse1 analyse2 analyse-rn series integration-proba complement-maths mesures-integration probabilites optimisation optimisation-deterministe analyse-numerique equations-differentielles statistique-inferentielle modele-lineaire edp series-temporelles compressive-sensing data-exploration data-mining',
  info: 'informatique1 informatique2 informatique3 informatique4 algorithmique bdd programmation-procedurale programmation-fonctionnelle programmation-parallele unix systeme-exploitation theorie-graphes theorie-langages decidabilite-complexite architecture-reseau ia methodes-agiles',
  physics: 'physique1 mecanique-du-point electromagnetisme ondes physique-moderne traitement-signal',
};

const DOMAIN_OF: Record<string, Domain> = Object.fromEntries(
  Object.entries(DOMAINS).flatMap(([domain, ids]) => ids.split(' ').map((id) => [id, domain as Domain])),
);

/** Retire le préfixe ING (`ing-1-s2-data-…`) pour retrouver l'identifiant de la matière. */
const baseId = (id: string): string => id.replace(/^(?:ing-1-s\d-(?:gm|info|data)|ing-\d(?:-s\d)?)-/, '');

export const courseSym = (id: string): string => COURSE_SYM[baseId(id)] || '·';
export const courseDomain = (id: string): Domain => DOMAIN_OF[baseId(id)] || 'shs';

const EXAMPLES: Record<string, string[]> = {
  'analyse-rn': ['norme équivalente', 'différentiabilité'],
  series: ["critère de d'Alembert", 'rayon de convergence'],
  informatique3: ['listes chaînées', 'arbres binaires', 'piles et files'],
  electromagnetisme: ['théorème de Gauss', 'champ magnétique'],
  shs: ['recherche documentaire', 'méthodes'],
  algebre1: ['nombres complexes', 'polynômes'],
  analyse1: ['limites', 'suites'],
  informatique1: ['boucles', 'HTML'],
  physique1: ['mécanique', 'énergie'],
  cef1: ['communication'],
  ic1: ['ingénieur'],
  'projet1-s1': ['projet'],
  algebre2: ['applications linéaires', 'matrices'],
  analyse2: ['intégrales', 'développements limités'],
  informatique2: ['pointeurs', 'fonctions'],
  'mecanique-du-point': ['énergie cinétique'],
  'projet1-s2': ['projet'],
  'algebre-lineaire': ['diagonalisation', 'produit scalaire'],
  ethique: ['éthique'],
  informatique4: ['classes', 'héritage'],
  'integration-proba': ['variables aléatoires', 'intégration'],
  ondes: ['propagation', 'interférences'],
  'physique-moderne': ['quantique', "fonction d'onde"],
};

const ING_EXAMPLES: Record<string, string[]> = {
  algebre: ['diagonalisation'], algorithmique: ['complexité'], bdd: ['requêtes SQL'],
  'data-exploration': ['régression'], 'mesures-integration': ['fonctions mesurables'],
  probabilites: ['variables aléatoires'], optimisation: ['simplexe'],
  'programmation-procedurale': ['pointeurs'], unix: ['commandes shell'],
  'analyse-numerique': ['interpolation'], 'data-mining': ['classification'],
  'equations-differentielles': ['équations différentielles'], 'statistique-inferentielle': ['estimation'],
  'systeme-exploitation': ['processus'], 'theorie-graphes': ['plus court chemin'],
  'theorie-langages': ['automates'], 'architecture-reseau': ['adressage IP'],
  'decidabilite-complexite': ['machine de Turing'], 'modele-lineaire': ['régression linéaire'],
  'optimisation-deterministe': ['gradient'], 'programmation-fonctionnelle': ['Scala'],
  'traitement-signal': ['transformée de Fourier'], economie: ['marché'],
  'compressive-sensing': ['parcimonie'], edp: ['différences finies'],
  ia: ['apprentissage par renforcement'], 'programmation-parallele': ['OpenMP'],
  'series-temporelles': ['moyenne mobile'], 'methodes-agiles': ['Scrum'],
};

export const courseExamples = (id: string): string[] =>
  EXAMPLES[id] || ING_EXAMPLES[id.replace(/^ing-[12](?:-s[12])?(?:-(?:gm|info|data))?-/, '')] || [];
