import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ForestryWindowComponent } from './forestry-window.component';

describe('ForestryWindowComponent', () => {
  let component: ForestryWindowComponent;
  let fixture: ComponentFixture<ForestryWindowComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ForestryWindowComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ForestryWindowComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
