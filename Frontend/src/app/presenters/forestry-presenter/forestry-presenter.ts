import { IForestryList } from 'src/app/interfaces/iforestry-list';
import { IForestryPresenter } from "src/app/interfaces/iforestry-presenter";

export class ForestryPresenter implements IForestryPresenter {
    private forestryList: IForestryList|undefined;

    init(forestryList: IForestryList) {
        this.forestryList = forestryList;
    }
    
    handleShowAllForestries(): void {}
}
