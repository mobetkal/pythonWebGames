export class StatisticElement {
  position: Number;
  gameName: String;
  login: String;
  points: Number;

  constructor(position: Number, gameName: String, login: String, points: Number) {
    this.position = position;
    this.gameName = gameName;
    this.login = login;
    this.points = points;
  }
}
