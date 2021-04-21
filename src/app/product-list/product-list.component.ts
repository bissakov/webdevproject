import { Component } from '@angular/core';
import { CartService } from '../cart.service';
import { products } from '../products';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})

export class ProductListComponent {
  products = products;
  selectedOption = '';

  constructor(
    private cartService: CartService,
  ) {
  }

  addToCart(product): void {
    this.cartService.addToCart(product);
    window.alert('Your product has been added to the cart!');
  }

  hidecategory(event: any): any{
    let a = document.getElementsByTagName('h5');
    for (let i = 0; i < a.length; ++i){
      let cat = a[i].innerHTML;
      let st =  cat.indexOf(' ');
      cat = cat.slice(st+1,cat.length);
      if (cat == event.target.value || event.target.value == 'all'){
        /* tslint:disable:no-string-literal */
        a[i].parentNode['setAttribute']('style', 'display: inline-block;');
        /* tslint:enable:no-string-literal */
      }
      else{
        /* tslint:disable:no-string-literal */
        a[i].parentNode['setAttribute']('style', 'display: none;');
        /* tslint:enable:no-string-literal */
      }
    }
  }

  addlike(): any {
    let a: any = document.getElementsByClassName('fa fa-thumbs-up');
    for (let i = 0; i < a.length; ++i) {
      if (document.activeElement == a[i]) {
        a[i].innerHTML = (parseInt(a[i].innerHTML) + 1).toString();
        a[i].disabled = true;
      }
    }
  }
  remove(): any{
  let a: any = document.getElementsByClassName('fa fa-times');
    for (let i = 0; i < a.length; ++i) {
      if(document.activeElement == a[i]){
        console.log('ok');
        /* tslint:disable:no-string-literal */
        document.activeElement.parentNode['setAttribute']('style', 'display: none;');
        /* tslint:enable:no-string-literal */
      }
    }
  }
}
