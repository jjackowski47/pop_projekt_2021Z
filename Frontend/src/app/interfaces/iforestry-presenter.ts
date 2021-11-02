import { IForestryList } from "./iforestry-list";

export interface IForestryPresenter {
    init(forestryList: IForestryList): void;
    handleShowAllForestries(): void;
}
