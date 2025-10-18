export type Song = {
  name: string;
  link: string;
  id: string;
};

export type Block = {
  name: string;
  songs: Song[];
  categories: string;
  songCount: number;
};