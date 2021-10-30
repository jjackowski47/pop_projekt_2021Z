import { Component, OnInit } from '@angular/core';
import { ForestryController } from 'src/app/controllers/forestry-controller/forestry-controller';
import {AddForestryDialogComponent} from "./add-forestry-dialog/add-forestry-dialog.component";
import {MatDialog} from "@angular/material/dialog";

@Component({
  selector: 'app-forestry-view',
  templateUrl: './forestry-view.component.html',
  styleUrls: ['./forestry-view.component.css']
})
export class ForestryViewComponent implements OnInit {
  forestryController: ForestryController;
  forestry: any;

  constructor(
    public dialog: MatDialog
  ) {
    this.forestryController = new ForestryController(this);
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
    const dialogRef = this.dialog.open(AddForestryDialogComponent);

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }

  addForestryDialog(){
    this.forestryController.handleShowDialog();
  };
}
