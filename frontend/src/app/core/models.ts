/** Types partagés avec l'API du backend (voir backend/server.py : build_meta, build_tree, result_json). */

export type Domain = 'math' | 'info' | 'physics' | 'shs';

export interface CourseMeta {
  id: string;
  name: string;
  /** Identifiant du contexte (cycle / année / semestre / parcours). */
  curriculum: string;
  curriculum_label: string;
  program: string;
  track: string | null;
  study_year: number | null;
  semester: number | null;
  count: number;
  /** Nombre de passages par type de document. */
  kinds: Record<string, number>;
  /** Années scolaires disponibles (`null` = sans date). */
  years: (number | null)[];
}

export interface Curriculum {
  id: string;
  program: string;
  track: string | null;
  study_year: number | null;
  semester: number | null;
  label: string;
  count: number;
}

export interface Meta {
  courses: CourseMeta[];
  kinds: Record<string, string>;
  curricula: Curriculum[];
  programs: Record<string, string>;
}

export interface DocInfo {
  key: string;
  label: string;
  kind: string;
  corrige: boolean;
  year: number | null;
  count: number;
  with_correction: boolean;
}

/** Documents de chaque matière, indexés par identifiant de matière. */
export type Tree = Record<string, DocInfo[]>;

/** Types de blocs produits par `content_blocks` (backend/server.py). */
export type BlockType = 'md' | 'text' | 'slides' | 'code';

export interface Block {
  type: BlockType;
  text: string;
}

export interface Video {
  notion: string;
  url: string;
  /** `null` quand aucune vidéo ne traite la notion : le lien ouvre alors une recherche YouTube. */
  title: string | null;
  channel: string | null;
}

export interface PdfSource {
  doc: string;
  /** Numéros des pages (à partir de 1) du PDF d'origine. */
  pages: number[];
}

export interface CurrentCorrection {
  td: number;
  exercise: number;
  partial: boolean;
}

export interface SearchResult {
  label: string;
  section: string;
  doc_label: string;
  course: string;
  course_name: string;
  curriculum: string;
  curriculum_label: string;
  study_year: number | null;
  semester: number | null;
  program: string;
  track: string | null;
  kind: string;
  corrige: boolean;
  year: number | null;
  with_correction: boolean;
  /** `null` quand le passage est affiché sans recherche (ouverture d'un document). */
  score: number | null;
  doc_key: string;
  current?: CurrentCorrection | null;
  blocks: Block[];
  alt: Block[] | null;
  videos: Video[];
  pdf: PdfSource | null;
}

export interface SearchResponse {
  tokens: string[];
  reference: string | null;
  relaxed: boolean;
  highlight: string[];
  searched: number;
  results: SearchResult[];
}

export interface DocResponse {
  results: SearchResult[];
}

/** Filtres de recherche choisis par l'utilisateur (persistés dans localStorage). */
export interface Filters {
  program: string;
  study_year: string;
  semester: string;
  track: string;
  course: string;
  kinds: string[];
  versions: string[];
  years: string[];
  k: number;
  recent: boolean;
}
