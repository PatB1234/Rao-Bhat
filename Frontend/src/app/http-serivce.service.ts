import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators'

@Injectable({
  providedIn: 'root'
})
export class HttpSerivceService {

  private URL = 'http://localhost:8000';
  constructor(private http: HttpClient) { }

  getUsers() {

    return this.http.get(this.URL + '/get_users')
  }
  editUser(data: any) {

    return this.http.post(this.URL + '/update_full', data)
  }
  checkData(data: any) {

    return this.http.post(this.URL + '/check_data', data).pipe(map((res: any) => {

      return res
    }))
  }

  updateSpouse(data: any) {

    return this.http.post(this.URL + '/update_spouse', data).pipe(map((res: any) => {

      return res
    }))
  }

  updateMother(data: any) {

    return this.http.post(this.URL + '/update_Mother', data).pipe(map((res: any) => {

      return res
    }))
  }
  updateFather(data: any) {

    return this.http.post(this.URL + '/update_Father', data).pipe(map((res: any) => {

      return res
    }))
  }

  updateRest(data: any) {

    return this.http.post(this.URL + '/update_rest', data).pipe(map((res: any) => {

      return res;
    }))
  }

  add_member(data: any) {

    return this.http.post(this.URL + "/add_member", data).pipe(map((res: any) => {

      return res
    }))
  }
}
