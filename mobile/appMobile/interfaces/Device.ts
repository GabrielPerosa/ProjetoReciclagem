import { State } from './State';

export interface Device {
  id: string;
  description: string;
  states: State[];
}