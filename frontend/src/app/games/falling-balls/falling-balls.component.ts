import { Component, OnInit, OnDestroy } from '@angular/core';

let node;

@Component({
  selector: 'app-falling-balls',
  templateUrl: './falling-balls.component.html',
  styleUrls: ['./falling-balls.component.css']
})
export class FallingBallsComponent implements OnInit, OnDestroy {

  constructor() {
  }

  ngOnInit() {
    node = document.createElement('script');
    node.src = 'assets/games/falling-balls/falling-balls.py';
    node.type = 'text/python';
    document.getElementsByTagName('body')[0].appendChild(node);
  }

  ngOnDestroy() {
    document.getElementsByTagName('body')[0].removeChild(node);
  }

}
