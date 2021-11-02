import { Component, Input, OnInit } from '@angular/core';
import { IForestryList } from 'src/app/interfaces/iforestry-list';
import { IForestryPresenter } from 'src/app/interfaces/iforestry-presenter';

@Component({
  selector: 'app-forestry-list',
  templateUrl: './forestry-list.component.html',
  styleUrls: ['./forestry-list.component.css']
})
export class ForestryListComponent implements OnInit, IForestryList {
  @Input() forestryPresenter: IForestryPresenter|undefined;

  constructor() {}

  ngOnInit(): void {}

  showForestries(forestries: any[]): void {}
}
