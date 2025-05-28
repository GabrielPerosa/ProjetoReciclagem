import { State } from './state';

export interface Device {
  id: string;
  description: string;
  states: State[];
}