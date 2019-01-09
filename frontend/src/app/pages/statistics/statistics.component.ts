import { Component, OnInit, ViewChild } from '@angular/core';
import { MatPaginator, MatSort, MatTableDataSource } from '@angular/material';

import { StatisticService } from '../../shared/services/statistic.service';

import { GameElement } from '../../shared/classes/game-element';
import { StatisticElement } from '../../shared/classes/statistic-element';


@Component({
  selector: 'app-statistics',
  templateUrl: './statistics.component.html',
  styleUrls: ['./statistics.component.css']
})
export class StatisticsComponent implements OnInit {
  dataSource: MatTableDataSource<StatisticElement>;
  dataSourcePerGame: GameElement[] = [];
  displayedColumns: string[] = ['position', 'gameName', 'login', 'points'];
  displayedColumnsPerGame: string[] = ['position', 'login', 'points'];

  @ViewChild(MatSort) sort: MatSort;
  @ViewChild(MatPaginator) paginator: MatPaginator;

  constructor(private statisticService: StatisticService) { }

  ngOnInit() {
    this.loadStatistics();
  }

  private loadStatistics() {
    this.statisticService.getAll()
      .subscribe(value => {
        const allStatElements: StatisticElement[] = [];

        for (let i = 0; i < value.length; i++) {
          if (this.dataSourcePerGame.length !== 0) {
            for (let j = 0; j < this.dataSourcePerGame.length; j++) {
              const item = new StatisticElement(0, value[i].game_name, value[i].login, value[i].points);
              allStatElements.push(item);
              if (this.dataSourcePerGame[j].name === value[i].game_name) {
                this.dataSourcePerGame[j].pushElement(item);
              }
            }
          } else {
            const item = new StatisticElement(0, value[i].game_name, value[i].login, value[i].points);
            this.dataSourcePerGame.push(new GameElement(value[i].game_name, item));
            allStatElements.push(item);
          }
        }
        for (let j = 0; j < this.dataSourcePerGame.length; j++) {
          this.dataSourcePerGame[j].statElements
            .sort((a, b) => (a.points < b.points) ? 1 : ((b.points < a.points) ? -1 : 0));
          for (let i = 0; i < this.dataSourcePerGame[j].statElements.length; i++) {
            this.dataSourcePerGame[j].statElements[i].position = i + 1;
          }
        }
        allStatElements.sort((a, b) => (a.points < b.points) ? 1 : ((b.points < a.points) ? -1 : 0));
        for (let j = 0; j < allStatElements.length; j++) {
          allStatElements[j].position = j + 1;
        }
        this.dataSource = new MatTableDataSource<StatisticElement>(allStatElements);
        this.dataSource.sort = this.sort;
        this.dataSource.paginator = this.paginator;
      });
  }

  applyFilter(filterValue: string) {
    this.dataSource.filter = filterValue.trim().toLowerCase();
  }

}
