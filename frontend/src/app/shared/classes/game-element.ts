import { StatisticElement } from './statistic-element';

export class GameElement {
  name: String;
  statElements: StatisticElement[] = [];

  constructor(name: String, statElement: StatisticElement) {
    this.name = name;
    this.statElements.push(statElement);
  }

  public pushElement(statElement: StatisticElement): void {
    this.statElements.push(statElement);
  }
}
