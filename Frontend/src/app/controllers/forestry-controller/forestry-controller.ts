import { ForestryViewComponent } from '../../views/forestry-view/forestry-view.component';
import { HttpClient, HttpHeaders} from '@angular/common/http';

export class ForestryController {
  forestryView: ForestryViewComponent;
  baseURL: string = "http://127.0.0.1:5000/";

  constructor(forestryView: ForestryViewComponent, private http: HttpClient) {
    this.forestryView = forestryView;
  }

  handleShowDialog(){
    this.forestryView.showAddForestryDialog();
  }

  async getForestry() {
    // const res = await fetch('api');
    const res = "forestry value";
    this.forestryView.setForestry(res);
  }

  addForestry(forestry: any){ //TODO change any to Forestry
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json'
      })
    }; 
    const body=forestry;
    console.log(body)
    this.http.post(this.baseURL + 'forestry', body, httpOptions).subscribe(forestry => console.log(forestry));  
  }

}
