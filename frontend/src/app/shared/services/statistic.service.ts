import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { API_URL } from '../../env';

@Injectable()
export class StatisticService {

  constructor(private http: HttpClient) {
  }

  getAll() {
    return this.http.post<any>(`${API_URL}/stat`, {});
  }
}
