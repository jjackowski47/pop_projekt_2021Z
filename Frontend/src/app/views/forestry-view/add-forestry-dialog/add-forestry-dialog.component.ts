import { Component, OnInit } from '@angular/core';
import {FormControl} from "@angular/forms";
import { ForestryController } from 'src/app/controllers/forestry-controller/forestry-controller';
import { HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-add-forestry-dialog',
  templateUrl: './add-forestry-dialog.component.html',
  styleUrls: ['./add-forestry-dialog.component.css']
})
export class AddForestryDialogComponent implements OnInit {

  forestryName = '';
  forestrySurface = 0;
  afforestationTypes: string[] = ['Liściaste', 'Iglaste'];
  afforestation = new FormControl();
  foresterLodges: string[] = ['Leśniczówka 1', 'Leśniczówka 2', 'Leśniczówka 3'];
  selectedForesterLodge = '';
  forestryBorders: string[] = ['Granica 1', 'Granica 2', 'Granica 3'];
  selectedForestryBorder = '';

  x = "";
  y = "";
  coordinates: any[] = [];



  returnData(){
    const formValues = {
      forestryName: this.forestryName,
      forestryBorder: this.selectedForestryBorder,
      forestrySurface: this.forestrySurface,
      afforestationTypes: this.afforestation.value,
      foresterLodge: this.selectedForesterLodge,
      coordinates: this.coordinates
    }

    return formValues
  }

  handleAddCoordClick(){
    const coord = {x: parseFloat(this.x), y: parseFloat(this.y)};
    this.coordinates.push(coord);
  }


  constructor() {   
  }

  ngOnInit(): void {
  }

}
