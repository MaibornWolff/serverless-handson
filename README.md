# NSE Tag 2019 - CloudNative

Anbei finden sie den Code für die Beispiele die während des NSE-Tag 2019 durchgeführt wurden.

#### Hinweise
- Die Sourcen wurden speziell für dieses Ereignis erstellt und sind nur den Teilnehmer des NSE Tag 2019 zur Verfügung gestellt worden
- Die Beispiele wurden zielgruppenspezifisch zugeschnitten - d.h. sie wurde didaktisch angepasst um die Konzepte bestmöglich zu vermitteln
- Der Code und die Dokumentation spiegeln nicht die qualitativen Ansprüche von MaibornWolff an ein produktiven Einsatz wieder
- Bitte wenden sie sich bei Fragen gerne an MaibornWolff direkt z.B. michael.abey@maibornwolff.de


### Voraussetzung

#### Betriebssystem
Es wurde für folgende Betriebssysteme getestet:
- Linux
- OSX

#### Cloud Account
- AWS Account erstellen + credentials im Betriebssystem hinterlegen 
 
 
    vi ~/.aws/credentials
    [1]
    aws_access_key_id = AKIA...
    aws_secret_access_key = r4VAd....


#### Umgebungsvariablen setzen

    export AWS_PROFILE=<aws profile name in ~/.aws/credentials e.g. 1>
    export GROUP_ID=1
    
#### Zentrales Monitoring
Wir haben für den NSE Tag einen zentralen Elasticstack aufgesetzt. Diesen können wir den Sourcen nicht hinzufügen.
Beispiele die darauf angewiesen sind müssten übersprungen oder ein Elasticsearch und Kibana müssten zur Verfügung gestellt werden.
Dies Betriff Aufgabe 3+4 


#### Testen
Für ein vollständiges automatisiertes testen aller Beispiele wurde ein Smoketest geschrieben der die groben Funktionalitäten einmal durchläuft.
Er frägt zuvor auch alle technisch installierten Vorraussetzungen ab, die dann gegebenfalls manuell installiert werden müssen.


    cd internals
    ./smoke-test.sh
    
Einzelne Aufgaben testen anhand der Nummer z.B.

    ./smoke-test.sh 1
    
    
#### Löschen
Sollte ein Test schiefgehen oder eine Aufgabe wieder aufgeräumt werden müssen

    cd internals
    ./destroy-task.sh
    
    
## Beispiele - Aufgabenstellung
Finden sie in der beigelegten Präsentation und in den taskN/README.md


## Beispiel - ausführen
Die Beispiele sind alle gleich aufgebaut:

    
    /taskN
    	/code
    		/serverless_functions      - Serverless Funktionen
    		/hint                      - Hinweise die Aufgabe zu lösen
    	serverless.yml                 - Serverless Framework Konfiguration
    	./deploy.sh                    - Skript zum deployen
    	README.md                      - Dokumentation

Bitte folgen sie den Hinweisen in den Aufgaben in den Ordnern:
/task1 .. N

Sie finden dort alle benötigten Informationen um die Beispiele auszuführen.