import {Component, OnInit, ViewChild} from '@angular/core';
import {PollyService, SpeechSynthResponse, Voice} from './polly.service';
import {MatSnackBar} from '@angular/material';


// Mapping of the OutputFormat parameter of the SynthesizeSpeech API
// and the audio format strings understood by the browser
const AUDIO_FORMATS = {
  ogg_vorbis: 'audio/ogg',
  mp3: 'audio/mpeg',
  pcm: 'audio/wave; codecs=1'
};

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  voices: Voice[];
  selectedVoice: string;
  text = 'Polly will einen Keks';

  ngOnInit(): void {
    this.pollyService.getVoices().subscribe(response => {
      this.voices = response as Voice[];
      const germanVoices = this.voices.filter(v => v.LanguageCode === 'de-DE');
      this.selectedVoice = germanVoices[Math.floor(Math.random() * germanVoices.length)].Id;
    });
  }

  constructor(private pollyService: PollyService, private snackBar: MatSnackBar) {
  }

  /**
   * Returns a list of audio formats supported by the browser
   */
  getSupportedAudioFormats(player: HTMLAudioElement): string[] {
    return Object.keys(AUDIO_FORMATS)
      .filter((format) => {
        const supported = player.canPlayType(AUDIO_FORMATS[format]);
        return supported === 'probably' || supported === 'maybe';
      });
  }

  read($event: MouseEvent, player: HTMLAudioElement) {
    const supportedAudioFormat = this.getSupportedAudioFormats(player)[0];
    this.pollyService.speechSynthesize(this.selectedVoice , this.text, supportedAudioFormat).subscribe(response => {
        const speech = response as SpeechSynthResponse;
        player.setAttribute('src', 'data:' + AUDIO_FORMATS[supportedAudioFormat] + ';base64,' + speech.speech);
        player.load();
        player.play();
      },
      (err) => {
        this.snackBar.open(err.message, null, {
          horizontalPosition: 'center',
          verticalPosition: 'top',
          duration: 5000,
          panelClass: 'snack-error'
        });
      }
    );
  }
}
