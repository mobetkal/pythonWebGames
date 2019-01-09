import { Component, OnInit, OnDestroy } from '@angular/core';

let node;

@Component({
  selector: 'app-mc-bird',
  templateUrl: './mc-bird.component.html',
  styleUrls: ['./mc-bird.component.css']
})
export class McBirdComponent implements OnInit, OnDestroy {

  constructor() {
  }

  ngOnInit() {
    node = document.createElement('script');
    node.src = 'assets/games/mc-bird/MCBird.py';
    node.type = 'text/python';
    document.getElementsByTagName('body')[0].appendChild(node);
  }

  ngOnDestroy() {
    document.getElementsByTagName('body')[0].removeChild(node);
  }

}