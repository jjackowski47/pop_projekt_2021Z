import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddForestryDialogComponent } from './add-forestry-dialog.component';

describe('AddForestryDialogComponent', () => {
  let component: AddForestryDialogComponent;
  let fixture: ComponentFixture<AddForestryDialogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddForestryDialogComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AddForestryDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
