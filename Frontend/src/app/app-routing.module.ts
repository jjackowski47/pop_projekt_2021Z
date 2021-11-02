import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ForestryWindowComponent } from './windows/forestry-window/forestry-window.component';

const routes: Routes = [
  { path: '', component: ForestryWindowComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
