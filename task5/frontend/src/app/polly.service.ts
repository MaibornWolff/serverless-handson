import {Injectable} from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';
import {environment} from '../environments/environment';

export interface Voice {
  Gender: string;
  Id: string;
  LanguageCode: string;
  LanguageName: string;
  Name: string;
}

export interface SpeechSynthResponse {
  speech: string;
}


@Injectable({
  providedIn: 'root'
})
export class PollyService {

  voicesEndpoint = 'voices';
  speechSynthesizeEndpoint = 'speech-synthesize';

  constructor(private http: HttpClient) {
  }

  getServiceEndPoint() {
    if (environment.lambdaApiEndpoint.slice(-1) !== '/') {
      return environment.lambdaApiEndpoint + '/';
    } else {
      return environment.lambdaApiEndpoint;
    }
  }

  getVoices() {
    return this.http.get(this.getServiceEndPoint() + this.voicesEndpoint);
  }


  speechSynthesize(voiceID: string, text: string, outputFormat: string) {

    let queryParams = new HttpParams();
    queryParams = queryParams.append('voiceId', voiceID);
    queryParams = queryParams.append('text', text);
    queryParams = queryParams.append('outputFormat', outputFormat);

    return this.http.get(this.getServiceEndPoint() + this.speechSynthesizeEndpoint, {params: queryParams});
  }

}
