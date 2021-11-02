import { AfterViewInit, Component, OnInit, ViewChild } from '@angular/core';
import { IForestryList } from 'src/app/interfaces/iforestry-list';
import { IForestryPresenter } from 'src/app/interfaces/iforestry-presenter';
import { ForestryPresenter } from 'src/app/presenters/forestry-presenter/forestry-presenter';

@Component({
  selector: 'app-forestry-window',
  templateUrl: './forestry-window.component.html',
  styleUrls: ['./forestry-window.component.css']
})
export class ForestryWindowComponent implements OnInit, AfterViewInit {
  @ViewChild('forestryList') 
  private forestryList: IForestryList|undefined;
  forestryPresenter: IForestryPresenter;

  constructor() {
    this.forestryPresenter = new ForestryPresenter();
  }

  ngOnInit(): void {}

  ngAfterViewInit(): void {
    this.forestryPresenter.init(this.forestryList!);
  }
}
