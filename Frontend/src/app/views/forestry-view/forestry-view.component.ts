import { Component, OnInit } from '@angular/core';
import { ForestryController } from 'src/app/controllers/forestry-controller/forestry-controller';
import {AddForestryDialogComponent} from "./../forestry-list/add-forestry-dialog/add-forestry-dialog.component";
import {MatDialog} from "@angular/material/dialog";
import { HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-forestry-view',
  templateUrl: './forestry-view.component.html',
  styleUrls: ['./forestry-view.component.css']
})
export class ForestryViewComponent implements OnInit {
  forestryController: ForestryController;
  forestry: any;

  constructor(
    public dialog: MatDialog,
    public http: HttpClient
  ) {
    this.forestryController = new ForestryController(this, http);
  }

  ngOnInit(): void {
  }

  onClick(): void {
    this.forestryController.getForestry();
  }

  setForestry(value: any): void {
    this.forestry = value;
  }

  showAddForestryDialog(){
    const dialogConfig = {
      width: '600px',
      data: {data1: 'value1', data2: 'value2'}
    }
    const dialogRef = this.dialog.open(AddForestryDialogComponent, dialogConfig);

    dialogRef.afterClosed().subscribe(result => {
      console.log(result)
      // todo
      // create forestry from received data (with controller) 
      const forestry = {
        id: "cef0cbf3-6458-4f13-a418-ee4d7e7505dd", // it should be new valid uuid
        //location: [{"x": 1.0, "y": 1.2}, {"x": 1.0, "y": 1.2}, {"x": 1.0, "y": 1.2}],  // it should be forestry location
        location: result.coordinates,
        name: result.forestryName
      } 
      this.forestryController.addForestry(forestry);
    });
  }

  addForestryDialog(){
    this.forestryController.handleShowDialog();
  };
}
