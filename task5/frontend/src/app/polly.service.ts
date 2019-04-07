import {Injectable} from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';

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

declare global {
  interface Window { LAMBDA_ENDPOINT: string; }
}
window.LAMBDA_ENDPOINT = window.LAMBDA_ENDPOINT || '';

@Injectable({
  providedIn: 'root'
})
export class PollyService {

  voicesEndpoint = 'voices';
  speechSynthesizeEndpoint = 'speech-synthesize';

  constructor(private http: HttpClient) {
  }

   static getServiceEndPoint(): string {
    return window.LAMBDA_ENDPOINT;
  }

  getVoices() {
    return this.http.get(PollyService.getServiceEndPoint() + this.voicesEndpoint);
  }


  speechSynthesize(voiceID: string, text: string, outputFormat: string) {

    let queryParams = new HttpParams();
    queryParams = queryParams.append('voiceId', voiceID);
    queryParams = queryParams.append('text', text);
    queryParams = queryParams.append('outputFormat', outputFormat);

    return this.http.get(PollyService.getServiceEndPoint() + this.speechSynthesizeEndpoint, {params: queryParams});
  }

}
