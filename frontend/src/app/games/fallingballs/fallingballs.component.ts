import { Component, OnInit, OnDestroy } from '@angular/core';
//import * as br from '';


let node;

@Component({
  selector: 'app-fallingballs',
  templateUrl: './fallingballs.component.html',
  styleUrls: ['./fallingballs.component.css']
})



export class FallingballsComponent implements OnInit, OnDestroy {
  
  
  constructor() { }
  
  ngOnInit() {

   // this.loadScript('/src/app/games/brython/brython.js');
         
      //document.getElementsByTagName('body')[0].setAttribute("onload", "brython(2)");
      node = document.createElement('script');
      let url = './src/app/games/fallingballs/fallingballs.py';
      node.src = url;
      node.type = 'text/python';
      document.getElementsByTagName('body')[0].appendChild(node);
    
  }

  /* public loadScript(url: string)
  {
    const body = <HTMLDivElement> document.body;
    const script = document.createElement('script');
    script.innerHTML = '';
    script.src = url;
    script.className = "brython";
    script.async = false;
    script.defer = true;

    body.appendChild(script);  
  } */


  ngOnDestroy()
  {
    
    document.getElementsByTagName('body')[0].removeChild(node);
    
  }
  
}
