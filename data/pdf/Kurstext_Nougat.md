[MISSING_PAGE_EMPTY:1]

Das Werk ist urheberrechtlich geschützt. Die dadurch begründeten Rechte, insbesondere das Recht der Vervielfältigung und Verbreitung sowie der übersetzung und des Nachdrucks, bleiben, auch bei nur auszugsweiser Verwertung, vorbehalten. Kein Teil des Werkes darf in irgendeiner Form (Druck, Fotokopie, Mikrofilm oder ein anderes Verfahren) ohne schriftliche Genehmigung der FemUniversitat reproduziert oder unter Verwendung elektronischer Systeme verarbeitet, vervielfältigt oder verbreitet werden.

[MISSING_PAGE_EMPTY:3]

* 3 Zustand 34
* 3.1 Eingrenzung 34
* 3.2 Kapselung 36
* 4 Verhalten 36
* 4.1 Ausdrucke 37
* 4.1.1 Zuweisungsausdrucke 37
* 4.1.2 Nachrichtenausdrucke 37
* 4.1.3 Auswertung von Ausdrucken 41
* 4.1.4 Reihenfolge der Auswertung von geschachtelten Ausdrucken 43
* 4.2 Anweisungen 44
* 4.3 Methoden 45
* 4.3.1 Zuordnung von Methoden zu Objekten 48
* 4.3.2 Methodenaufruf und dynamisches Binden 49
* 4.3.3 Methoden als Parameter 52
* 4.3.4 Verbergen der Repräsentation des Zustands hinter Methoden 53
* 4.3.5 Operationen auf zustandslosen (unveränderlichen) Objekten 55
* 4.3.6 Konstante Methoden 56
* 4.3.7 Primitive Methoden 57
* 4.3.8 Protokoll 58
* 4.4 Blocke 58
* 4.4.1 Home context und Closure 59
* 4.4.2 Continuation 60
* 4.4.3 Parametrisierte Blocke 61
* 4.5 Kontrollstrukturen 62
* 4.5.1 Sequenz 62
* 4.5.2 Dynamisch gebundener Methodenaufruf 63
* 4.6 Abgeleitete Kontrollstrukturen 63
* 4.6.1 Verzweigung 64
* 4.6.2 Wiederholung 66
* 4.6.3 Iteration 66
* 4.6.4 Iterieren über Zu-n-Beziehungen 68

[MISSING_PAGE_EMPTY:5]

[MISSING_PAGE_EMPTY:6]

[MISSING_PAGE_EMPTY:7]

[MISSING_PAGE_EMPTY:8]

[MISSING_PAGE_EMPTY:9]

[MISSING_PAGE_EMPTY:10]

[MISSING_PAGE_EMPTY:11]

## Vorwort zur dritten Auflage

Seit der ersten Auflage dieses Kurses im Wintersemester 2006/2007 hat sich viel getan: Java als vormals dominierende objektorientierte Programmiersprache hat weiter Grund u. a. an C# verloren und beiden wird zunehrmend von JavaScript der Rang abgelaufen. Alle drei sind nicht nur objektorientiert, sondem haben (mittlerweile) auch starke funktionale Sprachantieile (die sog. Lambda-Ausdrucke), die im Vergleich zur imperativen Programmierung wesentlich kompaktere Programme emoglichen. Java hat zudem seit der übernahme durch Oracle viel von seinem Community-Charakter eingebulst; die zogerliche Weiterentwicklung der Sprache hat Java-basierten Konkurrenten wie Scala oder Kotlin Raum für Entwicklung gegeben. Ironischerweise sind Vorbild für manche der wichtigsten Weiterentwicklungen alte objektorientierte Programmiersprachen wie Smalltalk oder Eiffel; beide spielen in der aktuellen Programmierpraxis zwar nur noch eine Nebenrolle, ihr Erbe pragt aber die heutige Programmierung massgeblich.

### Zum Inhalt

Dieser Kurs stellt die objektorientierte Programmierung so dar, dass ein **Voraussetzungen** Gegensatz zur klassischen imperativen Programmierung entsteht. Um diesen Gegensatz wahrzunehmen, mussen Sie naturlich die imperative Programmierung kennen, also z. B. den Kurs 01613,,Einfuhrung in die imperative Programmierung" absolviert haben. Gleichwohl ist dieses Wissen keine Voraussetzung -- Sie können mit dem Ihnen vorliegenden Kurs die objektorientierte Programmierung auch als ertes lernen.

So sind die formalen Voraussetzungen zur erfolgreichen Bearbeitung dieses Kurses zunächst gering. Insbesondere bringt es Ihnen wenig, wenn Sie schon,,Java können" -- im ungungstigsten Fall mussen Sie sogar erst einiges vergessen, um die ersten Kurseinheiten unvoreingenommen verinnerlichen zu können. Wichtig für den Erfolg ist jedoch die grundsatzliche Bereitschaft, sich mit der Programmierung und deren Werkzeugen auseinanderzusetzen -- insbesondere wird Ihnen der Kurs nur wenig bringen, wenn Sie nicht bereit sind, die damit verbundenen Programmierubungen wirklich durchzufuhren. Wenn alles gutgeht, sollten Ihnen diese Ubungen allerdings auch freude bereiten.

Wenn Sie diesen Kurs erfolgreich absolviert haben, dann sollten Sie das **Ziele** folgende können:

* objektorientiert denken,
* objektorientiert programmieren,
* die Bestandteile objektorientierter Programmiersprachen erkennen und dabei insbesondere die Bedeutung eines Typsystems richtig einschatzen,
* die Schwachen der objektorientierten Programmierung benennen,

[MISSING_PAGE_EMPTY:13]

strikte Trennung erlaubt es, den Klassenbegriff, der für die meisten objektorientierten Programmiersprachen eine zentrale Rolle spielt, als einen Freiheitsgrad objektorientierter Programmierung darzustellen.

In Kurseinheit 2 wird dann die Klasse als struktur- und ordnungsstiftendes Konstrukt der objektorientierten Programmierung vorgestellt. Eng mit dem Klassenbegriff verbunden sind die Instanzierung von Klassen zu Objekten, der übergang von Klassen zu ihren Metaklassen sowie die Vererbung zwischen Klassen. Insbesondere die Vererbung hat in der objektorientierten Programmierung eine wechselhafte Geschichte hinter sich; auf die mit ihr verbunden Probleme wird jedoch erst in den folgenden Kurseinheiten eingegangen. Stattdessen werden in Kurseinheit 2 noch das dynamische Binden und seine Bedeutung als universelle Kontrollstruktur dargestellt.

Mit Kurseinheit 3 wird in das Thema Typsysteme für die objektorientierte Programmierung eingefuhrt. Dabei wird ausgenutzt, dass Smalltalk kein Typsystem hat; Typsysteme können hier also ohne Vorbelastung durch eine spezielle Sprache auf die objektorientierte Programmierung aufgeproft werden. Dabei wird insbesondere auf den für die objektorientierte Programmierung so zentralen Begriff des Subtyping hingerbeitet; aber auch die generischen Typen, die spatestens seit Java 5 und C# 2.0 auch zum taglichen Brot kommerzieller Programmierrinen gehoren durften, werden so eingefuhrt. Der dabei zum Einsatz kommende Smalltalk-Nachfolger Strongtalk wird dazu als Vorlage genommen, aber nur insoweit, als sich die Eigenschaften dessen Typsystems auch in anderen Programmiersprachen wiederfinden.

Ab Kurseinheit 4 werden dann andere Programmiersprachen vorgestellt. Kurseinheit 4 zollt zunächst Java als der heute wohl immer noch wichtigsten objektorientierten Programmiersprache Tribut: Die Prasentation orientiert sich dabei an der Einfuhrung in die objektorientierte Programmierung aus den vorangegangenen Kurseinheiten. Dies erlaubt eine pragante Darstellung der wesentlichen Konzepte und Unterschiede (und fuhrt zu einer eher ungewohnlichen Sicht auf Java als Programmiersprache). In Kurseinheit 5 werden dann auf analoge Weise der Reihe nach C#, C++ und Eiffel prasentiert. Dies soll nicht zuletzt lhrem Verstandnis von der Vielfalt der Sprachenlandschaft dienen und lhnen die Einsicht vermitteln, dass die gutten Seiten der objektorientierten Programmierung nicht in einer Sprache allein zu finden sind.

Kurseinheit 6 thematisiert die wichtigsten Probleme der objektorientierten Programmierung. Es sind dies im wesentlichen die des Subtyping und der damit verbundenen Substitierbarkeit von Objekten sowie der Kapselung von Objekten zu grosseren Einheiten, die ihr Innere versbergen. Beide scheinen auf den ersten Blick geloste Probleme zu sein; tatsachlich sind sie es aber keineswegs. Auch auf Probleme der Skalierbarkeit der objektorientierten Programmierung wird hier eingegangen.

In Kurseinheit 7 lassen wir schliesslich die Konstrukte objektorientierter Programmiersprachen hinter uns und gehen ausführlich auf das ein, was man gemeinhin objektorientierten

[MISSING_PAGE_FAIL:15]

## Vorkurs

In diesem Vorkurs werden die praktischen Voraussetzungen für die folgenden Kurseinheiten geschaffen. Sie werden dazu an eine objektorientierte Programmiersprache, SMALLtalk, und die damit verbundene Programmierumgebung herangefuhrt. Es ist für den weiteren Verlauf wichtig, dass Sie mit dem Umgang mit mindestens einem SMALLtalk-System vertraut sind, auch wenn Sie noch nicht verstehen, wie es funktioniert und warum es so anders zu sein scheint als alles, was Sie vielleicht schon kennen.

Parallel zum Lesen dieses Vorkurses, der ausgesprochen leichte Kost ist, sollten Sie ein oder mehrere SMALLtalk-Systeme installieren. Wie das geht, finden Sie in den Ubungsaufgaben zu diesem Vorkurs. Die Aufgaben sollten Sie unbedingt durchfuhren und ggf. so off wiederholen, bis Sie die Anleitung dazu nicht mehr brauchen. Es ware aregerlich, wenn Sie die Einsendeaufgaben der folgenden Kurseinheiten nur deswegen nicht losen können, weil Sie mit Ihrem SMALLtalk-System nicht zurechtkommen.

### Objektorientierte Programmierung

Das Adjektiv,,objektorientiert" wurde nach eigenem Bekunden von Alan Kay gepragt:

_... a new design paradigm -- which I called object-oriented -- for attacking large problems of the professional programmer..._

Kay erhielt 2003 den renommerten Turing-Award (auch als Nobelpreis der Informatik bezeichnet), und zwar u. a. für seine Rolle bei der Entwicklung von SMALLtalk:

_For pioneering many of the ideas at the root of contemporary object-oriented programming languages, leading the team that developed SMALLtalk, and for fundamental contributions to personal computing._

Hutern der englischen Sprache, die nichts mit Programmieren zu tun haben, stobt der Begriff,,object-oriented" ubtrigens sauer auf, denn sprachlich korrekt musste es,,object-oriented" heissen. Zum Gluck wurde dieser Frevel, der oft Skandinavierinnen zugeschrieben wurden, nach eigenem Bekunden von einem Muttersprachler begangen.

Das der objektorientierten Programmierung zugrundeliegende Weltbild ist das von _Objektten_, die jeweils eine _Identitat_ haben, die einander _Nachrichten_ schicken und die in Reaktion auf die Nachrichten durch Anweisungen, die in _Methoden_ festgehalten sind, ihren _Zustand_ verändern. Welche Nachrichten ein Objekt versteht, zahlt zu seinen _Eigenschaften_. Objekte können zudem entstehen und wieder vergehen -- das objektorientierte Weltbild ist also in vielerlei Hinsicht dynamisch.

Damit sich Objekte gezielt Nachrichten schicken können, mussen sie sich kennen. Welche anderen Objekte ein Objekt kennen kann, zahlt zu seinen Eigenschaften; welche es kennt, macht den Zustand eines Objektes aus und unterliegt mit diesem der Veränderung. Um neue Bekanntschaften zu schliessen, können einem Objekt ein oder mehrere andere Objekte als Parameter einer Nachricht geschickt werden. Der Empfang einer Nachricht durch ein Objekt fuhrt in der Regel zum Versand weiterer Nachrichten durch das empfangende Objekt sowohl an andere Objekte als auch an sich selbst. Auch das Entstehen und Vergehen von Objekten erfolgt in der Regel als Reaktion auf den Empfang einer Nachricht.

Da Objekte so allgemeine Dinge wie Personen oder Dokumente, aber auch so spezielle Dinge wie Zahlen oder Wahrheitswerte sein können und Nachrichten so allgemeine wie _schreib dich ein" oder _drucke dich aus", aber auch so spezielle wie _,_+" oder _,_-", hat man damit schon fast alles, was man zum Programmieren braucht. Die einzigen zusatzlich benotigten Konzepte sind das der _Variable_ und der _Wertzuweisung_, die se vermutlich bereits aus anderen Programmiersprachen kennen.

Der Begriff der Objektorientierung verlangt aber noch mindestens eine weitere Eigenschaft, die der _Verebung_. Sie besagt, dass Objekte Eigenschaften von anderen erben können, dass also insbesondere nicht jedes Objekt für sich seine eigenschaften definieren muss. Allerdings hat sich der Begriff der Verebung als ein zwar leicht zu fassender, aber ungemein schwierig umzusetzender erwiesen, zumindest, wenn man sich durch Verebung nicht in dem Umfang Schwierigkeiten einhanden will, in dem man sich Arbeit erspart. Und so sehen viele heute eher das sog. _Subtyping_ anstelle der Verebung als für die objektorientierte Programmierung wesensbildende Eigenschaft.

Als die objektorientierte Programmierung noch angeprisesen werden musste, wurden immer wieder dieselben Vorteile genannt:

\begin{tabular}{c|c|c}  & **Eigenschaften der** \\  & **objektorientierten** \\  & **Programmierung** \\  & **Programmierung** \\ \end{tabular}

Auch wenn kein kausaler Zusammenhang bestehen sollte: Seit sich die objektorientierte Programmierung durgesetzt hat, redet kaum eine noch von der _Softwarekrise_.

## Objektorientierte Programmiersprachen

Inzwischen gibt es eine grose Anzahl von Programmiersprachen, die objektorientiert sind. Viele altere Programmiersprachen wie z. B. Pascal oder Ada sind in Fortschreibungen wie Oberon oder Ada-95 objektorientiert geworden, aber auch jingere Sprachen wie z. B. PHP haben sich nach und nach,,objekt-orientiert". Nicht mehr wegzudenken aus der modernen Softwareentwicklung ist die Objektorientierung jedoch erst seit Einfuhrung der von C und Smalltalk abgeleiteten objektorientierten Sprachen C++, Java und C#: Diese haben die kommerzielle Softwareentwicklung quasi im Sturm erobert.

Zu den bekannteren objektorientierten Programmiersprachen (oder zumindest Programmiersprachen mit objektorientierten Anteilen) zahlen heute (in alphabetischer Reihenfolge): Ada 95, BETA, C++, C#, Common LISP, D, Object Pascal (Borland Delphi), Dylan, Eiffel, Sather, Fortran 2003, Java, JavaScript, Modula-3, Oberon, Objectve-C, Perl 5, PHP 5, Self, Python, Ruby, Scala, Simula, Smalltalk, Self und Visual Basic. Diese haben teilweise ihre Wurzeln in der prozeduralen Programmierung (mit Programmiersprachen wie Algol, Pascal oder C), teilweise in der funktionalen (mit Programmiersprachen wie LISP); aber auch ganz eigenstandige wie beispielsweise BETA sind darunter. Auch wenn nicht alle Sprachen gleich praxiselevant sind, kann es sich doch lohnen, sie zu kennen, denn jede hat ihre ganz eigenen Starken und Schwachen und auch wenn man in einer anderen Sprache programmieren muss, kann man doch vielleicht die eine oder andere Idee aus einer anderen Sprache emulieren.

## Smalltalk

Smalltalk wurde seit dem Beginn der 1970er Jahre bei der Firma Xerox in Palo Alto, USA, (genauer: im Palo Alto Research Center PARC) entwickelt, wurde dort 1983 unter der Beziehnung Smalltalk-80 der Offentlichkeit prasentiert und gilt bis heute als die objektorientierte Objektorientierte Programmiersprache. Auch wenn Alan Kay in seinem Ruckblick ein anderes Bild zeichnet, wird als einzige direkte Vorgangerin Smalltalk eigentlich immer die Programmiersprache Simula genannt, die bereits ca. zehn Jahre fruher, also in den 1960er Jahren, von den beiden Norwegian Ole-Johan Dahl und Kristen Nygaard (die dafur WikipediaA schon vor Kay im Jahr 2001 den Turing-Award erhielten und nach denen inzwischen selbst ein Preis benannt ist) an der Universitat Oslo konzipiert wurde und die unter dem Namen Simula-67 in Europa (aber wohl auch nur dort) einige Verbreitung gefunden hatte. Ein aderer wichtiger Einfluss auf Smalltalk war aber sicher LISP, denn gewisse _funktionale_ Eigenschaften (also die Tatsache, dass in der Sprache Funktionsausdrucke ausgewertet werden) kann und will Smalltalk nicht verbergen.

Die Grundidee Smalltalkks lasst sich in einem einzigen, einfachen Satz

Zusammenfassen:

[MISSING_PAGE_FAIL:19]

Unternehmen mit grossen betrieblichen Informationsystemen begannen, erste hausinternne Applikationen mit Smalltalk zu entwicklen.2 Geschatzt wurde vor allem die (im Vergleich zu den branchenublichen Sprachen wie Csool, aber auch zu sog. hoheren Programmiersprachen wie Modula, C oder C++) sehr viel hohere Produktivitat. Ironischenweise wurde dieses zarte Pflanzchen wenig spater ausgerechnet von Java, einer Programmiersprache, die sich manches von Smalltalk abgeguckt hat, in Sachen Laufzeit um keinen Deut besser ist, in Sachen Produktivitat jedoch trotz aller Neuerungen heute immer noch nicht an Smalltalk heranreicht, plattgewalzt. Wahrend der kurzen Blutzezeit von Smalltalk entwickelte IBM ubrigens seine Entwicklungumgebung Visualage, die wenig spater (und noch in Smalltalk programmiert) für Java adaptiert wurde und aus der das heutige Eclipse-Projekt hervorgegangen ist. Doch wahrend Eclipse als Entwicklungsumgebung für Java das Smalltalk-System, aus dem es hervorgegangen ist, seit langem weit übertrifft, hat die Programmiersprache Java bis heute gebraucht, um an die Produktivitat von Smalltalk heranzureichen (machen wurden sagen: Sie hat es bis heute nicht geschhafft).

Footnote 2: Das oft zitierte C3-Projekt, mit dem die Disziplin des Extreme Programming begründet wurde, war ein Smalltalk-Projekt. Leider ist mir keine Arbeit bekannt, die untersucht hatte, auf welche Faktoren genau sich der Erfolg dieses Projekts zuruckfuhren lasst — man kann aber wohl davon ausgehen, dass mit Kent Beck, Ward Cunningham, Ron Jeffries und Martin Fowler einige der bekanntesten (und wohl auch besten) Programmier der Zeit mit an Bord waren, die nun einmal alle Smalltalk sprachen.

Vieleicht das großte Problem Smalltalk was aber, dass es zu fruhl kam.

Seine Architektur, die am unteren Ende auf einer virtuellen Maschine

(VM) mit automatischer Speicherbereinigung (_Garbage collection_) beruhte und am oberen auf einer Bedienberflache mit pixelgraphischen, überlappenden Fenstern und Zeiggeeraten wie Maus oder Tablet, stellte recht deftige Anforderungen an die Hardware, die damals noch klobig und teuer war. Außerdem wurden fast alle innovativen Konzepte Smalltalk s quasi auf der grunen Wiese entwickelt und mussten daher erst einmal in der Pravis erprobt und über einen langen Zeitraum verbessert werden, bis sie wirklich zu gebrauchen waren. Am Ende dieser Entwicklung haben dann nur wenige das Potential erkannt, das in Smalltalk steckte, darunter aber immerhin Steve Jobs, dessen Firmas Macintosh-System ganz wesentliche Elemente Smalltalks (Maus, überlappende Fenster) ubenommen und zur Verbreitung gefuhrt hat.

## Warum gerade Smalltalk?

Man kann lange darüber diskutieren, welche der zahlreichen objektorientierten Programmiersprachen am besten für das Erlernen der objektorientierten Programmierung im Rahmen der universitaren Lehre geeignet ist. In dem Inhen vorliegenden Kurs habe ich mich vor allem aus didaktischen Gründen für Smalltalk entschieden. Dabei soll der Kurs kein Smalltalk-Kurs sein; Sie sollen vielmehr die objektorientierten Konzepte und damit auch das objektorientierte Denken verinnerlichen, und Smalltalk scheint mir dafur am besten geeignet. Gleichwohl setzt das Verinnerlichen einiges an Ubung,,am Objekt" voraus, und deswegenhaben die ersten Kurseinheiten durchaus den Charakter einer Smalltalk-Einfuhrung. Spaestens ab Kurseinheit 4 wird jedoch der Vorhang gehoben und der Blick auf die Weiten der heutigen objektorientierten Programmiersprachenlandschaft freigegeben.

Smalltalk ist von Anfang an als eine leicht zu erlernende Sprache konzi-

piert worden. Insbesondere erweist sich als didaktischer Vorteil, dass man zum Erlernen der Sprache keine Programme schreiben, also genau genommen gar nicht programmieren muss

-- stattdessen fuhrt man mit dem System einfach,,Smalltalk". Dazu kommt, dass die Grammatik der Sprache ausgesprochen klein ausfallt: Es gibt keine Schlusselworter, nur wenige (funfl) reservierte Namen (Java hingegen hat 50 Schlusselworter und PASCAL immerhin auch schon 35) und lediglich die aus dem normalen Schriftegebrauch bekannten Interpunktionszeichen haben eine durch die Sprachdefinition festgelegte Bedeutung. So reicht in Smalltalk fur,,Hello Worldl" bereits der einfache Ausdruck

```
1Transcript show:"Hello Worldl"
```

um den Text auf dem Ausgabeterminal des Smalltalk-Systems, Transcript genannt, auszugeben. Dabei handelt es sich jedoch nicht um ein Programm im landaufigen Sinne, sondern lediglich um einen Ausdruck, der in der Entwicklungspungbung ausgewertet (,,ausgefuhrt") werden kann und als Ergebnis die Ausgabe der Zeichenkette,,Hello Worldl" bewirkt.3Tatsachlich gibt es in SMALLtalk wie bereits erwahnt so etwas wie ein Programm, das Sie schreiben, eigentlich gar nicht; stattdessen handelt es sich beim Smalltalk-System selbst um ein (laufendes) Programm, dass Sie als Programmierenrin -- wahrend es lauft -- so verändern, dass es neben allen anderen Dingen, die es kann, auch das tut, was Sie wollen (das bereits erwahnte _Live programming_). Je nach zu losendem Problem kann lhr eigener Beitrag dabei aus einem einzigen Ausdruck bestehen oder die Definition einer Vielzahl neuer Klassen umfassen. Die Werkeuge, die Sie dabei benutzen, sind selbst auf diese Weise entstanden und können Teil lhrer Anwendung sein.

Footnote 3: Man vergleiche dies mit dem Erklärungsnotstand, den eine Sprache wie Java bereits bei so einem simplen Beispiel mit sich bringt. Wer Eclipse und ahnlich machtige IDEs zur Java-Programmierung benutzt, wird einwenden, dass dies,,in Java auch geht"; tatsachlich geht es aber nicht,,in Java", sondern lediglich,,in Eclipse", also der IDE. Wer dieses Feature nicht kennt und es ausprobieren möchte: File > New > Other > Java > Java Run/Debug > Scrapbook Page. Es ist dies eines der vielen Erbstücke aus der Zeit, als die Entwicklerinnen von Eclipse noch an VisualAGE saßen.

Diese Besonderheit des Smalltalk-Systems ist aber nicht nur ein faszinie-

render Denkansatz, sondern ermoglicht auch eine sehr praktische Heran-

gehensweise bei der Vermittlung der Sprache. Es ist namlich moglich, die Sprache durch Ausprobieren zu erlernen, ohne sich vorher Gedanken über Dinge wie Editoren, Dateien oder gar Verzeichnisse, den Aufruf des Compilers oder den Start des Programms machen zu mussen. All das ist aber in anderen Sprachen wie z. B. Java trotz aufwendigster Entwicklungspungbungen immer noch der Fall. Mit Smalltalk können Sie hingegen sofort loslegen.

Ein weiterer wichtiger didaktischer Grund für die Wahl Smalltalk ist,

keeine Ablenkung dass es kein Typsystem hat. Bei den meisten anderen Sprachen musste

durch Typsystem

man mit Syntax und Semantik auch das Typsystem lernen und es fallt schwer, das Typsystem vom Rest der Sprache zu trennen. Objektorientierte Typsysteme unterscheiden sich aber zum Teil erheblich, ja sind sogar Gegenstand beinahe fanatsich gefuhrter Auseinandersetzungen, obwohl sie mit den Grundgedanken der objektorientierten Programmierung zuachst nur wenig zu tun haben. Die Verwendung von Smalltalk hingegen erlaubt, objektorientierte Programmierung unabhangig vom Typbegriff zu lehren und Typsysteme als das darzustellen, was sie sind: aufgefpropffe, semantische Regeln, die dazu dienen, logische Fehler in einem Programm zu finden, die aber zur eigentlichen Ausfuhrung des Programms gar nicht notwendig sind.

Wenn also Smalltalk hre erste objektorientierte Programmiersprache ist

Ubiektorientierung

und Sie stattdessen lieber eine andere erlent hatten, dann sollten Sie bedenken, dass es eine Vielzahl (die vermutlich auch zukunftig eher wachsen denn schrumpfen wird) verschiedener Programmiersprachen gibt, und dass der groste gemeinsame Teiler dieser Sprachen selbst keine existierende Programmiersprache ist. Smalltalk ist jedoch, aufgrund seiner extremen Reduziertheit, recht dicht daran und beinahe alle objektorientierten Programmiersprachen wurden von Smalltalk beineflusst. Sie lernen also nicht für die _Bewerschung einer_ objektorientierten Programmiersprache, sondern für ein _Verstandnis aller_.

### Programmierung mit Smalltalk

Wenn Sie lhr Smalltalk-System nach der Installation das erste Mal star-

ten, sehen Sie ein oder mehrere Fenster. Eines darunter ist das sogenannte Transcript, die,,Konsole" des Smalltalk-Systems. Auf ihr werden bestimmte Meldungen vom System ausgegeben; sie entspricht im wesentlichen dem allgemeinen Ausgabestrom anderer Programmiersprachen, die dort z. B. über Print-Statements angesprochen werden. In Java entsprache das Transcript etwa System. out.

Ausgehend vom Transcript können Sie weitere Fenster offnen, und zwar entweder, indem Sie entsprechende Ausdrucke eingeben und auswerten, oder, indem Sie entsprechende Membefehle aktivieren. (Wie das genau geht, erfahren Sie bei der Bearbeitung der Ubungs-aufgaben.) Zwei wichtige Arten von Fenstern sind sogenannte Workspaces und Klassenbrowser.

In einem Workspace können Sie Ausdrucke eingeben und auswerten lassen. Workspaces dienen in der Regel zum Herumexperimentieren. In einem Klassenbrowser können Sie sich die Klassen, aus denen das Smalltalk-System, an dem Sie gerade arbeiten, besteht, anschauen und diese manipulieren. Einen solchen werden Sie vor allem gebrauchen, wenn Sie programmieren.

Jeder Ausdruck, den Sie auswerten, und jede Klasse, die Sie andern, bewirkt eine Veränderung des Smalltalk-Systems. Sie wird, ohne dass Siedas merken, in einem Log file, gemeinhin _,**Change log**" genannt, mitgeschrieben. Wenn Sie Smalltalk beenden, werden Sie gefragt, ob Sie das aktuelle **Image** speichern wollen. Das Image ist der Inhalt des (virtualellen) Speichers lhres Smalltalk-Systems, also all seine Objekte inklusive aller Dinge, die Sie sehen, also auch der Fenster und deren Inhalt. Wenn Sie das Image speichern, wird Smalltalk sich beim nachsten Start genauso Brasentieren, wie Sie es verlassen haben, inklusive aller Anderungen, inklusive aller Fenster und deren Inhalt. Es gibt also keinen Neustart -- dazu mussten Sie das System schon neu installieren. Smalltalk ist also wie ein reelles, physicses System, an dem Sie bauen (und das sich ja auch nicht jedes Mal in seine Ausgangsmaterialien zerlegt, wenn Sie ins Bett gehen).

Wenn Sie das Image nicht speichern, z. B. weil Sie eine fatale Anderung (solche gibt es und sind leicht moglichl) ruckgangig machen wollen oder weil Ihnen der Strom ausgefallen ist das kein Problem, denn Sie haben ja noch das Change log. Das Change log enthalt wie gesagt alle Anderungen, die Sie gemacht haben, und zwar nicht in binarer Form, sondern als Smalltalk-Ausdrucke, die Sie auswerten können. Wenn Sie das tun, wiederholen Sie damit lhre gemachten, aber nicht im letzten Image gespeicherten Anderungen. Sie können den zuvor nicht gespeicherten Zustand lhres Systems also ganz oder auch nur teilweise -- ganz so, wie Sie es wunschen -- wiederherstellen. Mit Hilfe des Change logs verlieren Sie in Smalltalk nie auch nur eine einzige Zeile Code. Und das schon seit 1980.

Dieses wenige ist eigentlich alles, was Sie wissen mussen, um loszulegen. Welche Ausdrucke Sie sinnvollerweise eingeben und wie Sie programmieren, erfahren Sie in den Ubungen zu diesem Vorkurs (im Rahmen der Abarbeitung der Einsendeaufgaben) sowie in den folgenden, ersten beiden Kurseinheiten.

## Verfugbare Smalltalk-Systeme

Aktuell gibt es mindestens drei ernstzunehmende Smalltalk-Systeme, die Sie für diesen Kurs nutzen können:

* VisualWorks ist der direkte Nachfolger von Smalltalk-80; es stellt die Weiterentwicklung des zunächst von den ursprunglichen Autoren selbst (unter dem Namen Parc Place Systems firmierend) vertriebenen originalen Systems dar. Gleichzeitig ist es unter den hier vorgestellten Smalltalk-Systemen wohl das einzige, das auch für die kommerzielle Softwareentwicklung verwendet werden durfte. Gleichwohl ist es für den akademischen Gebrauch frei enhaltlich, und das auch noch für zahlreiche Plattformen. Wenn Sie sich jedoch von einem riesigen Funktionsumfang eher abgeschrekt als angezogen fuhlen, ist VisualWorks eher nicht das Richtige für Sie.
* Squeak ist ein Albeger des originalen Smalltalk-80-Systems, der von seinen beiden Vatern Dan Ingalls und Alan Kay in eine etwas andere, strikt nicht-kommerzielle Richtung getrieben wurde, in die unter anderem die Unterrichtung von Kindern fallt. So enthalt Squeak umfangreiche Multimediabiliotheken und damit Konstrukte, die man normalerweise nicht mit einer Programmiersprache assozlieren wurde. Leider

[MISSING_PAGE_FAIL:24]

[MISSING_PAGE_FAIL:25]

Kurseinheit 1: Grundkonzepte der objektorientierten Programmierung

Ein laufendes objektorientiertes Programm muss man sich als eine Menge interagjerender Objekte vorstellen. Damit die Objekte interagjeren können, mussen sie verbunden sein; sie bilden dazu ein Geflecht, das neben Objekten aus Beziehungen zwischen diesen besteht. Das Geflecht verändert sich dynamisch infolge der Interaktion zwischen Objekten; es unterliegt aber gewissen, durch das Programm vorgegebenen statischen Strukturen.

Die _Unterscheidung zwischen Statik und Dynamik_ ist eine klassische der

**Statik vs. Dynamik** Programmierung. Wahrend Programme traditionell statische Gebilde sind, die auf Papier oder in einem Nur-lese-Speicher festgehalten werden können, ist ihre Ausfuhrung immer etwas Dynamisches. Wenn aber Programme selbst als Daten aufgefasst werden, dann verwischt die Grenze zwischen Statik und Dynamik: Programme werden veränderlich. Insbesondere, wenn Programme sich selbst verändern können, ist die Unterscheidung zwischen Statik und Dynamik nur noch bedingt nutzlich.

Alternativ zu Statik und Dynamik kann man auch zwischen _Struktur_ und

**Struktur vs. Verhalten** unterscheiden, wobei mit Struktur das oben ewahnte Objekt-

**Verhalten** geflecht und mit Verhalten die (Spezifikation der) Folge seiner Veränderungen gemeint ist. Diese Unterscheidung liegt der Gliederung des Rests dieser Kurseinheit zugrunde: von Objekten (Kapitel 1) und Beziehungen zwischen diesen (Kapitel 2) geht es über den Zustand als Bindegliied (Kapitel 3) zu den Elementen der Verhaltensbeschreibung (Kapitel 4).

## 1 Objekte

In rein objektorientierten Programmiersprachen sind samtliche Daten, die ein Programm verarbeiten kann, in Form von Objekten im Speicher abgelegt. Der Reiz dieses Merkmals der objektorientierten Programmierung ist, dass unser Weltbild, zumindest in weiten Teilen, auf einem ahnlichen Modell basiert: Die Welt besteht aus Objekten, die miteinander in Beziehung stehen. Dabei ist der Objektbegriff nicht auf das rein Materielle beschrankt: Nach allgemeinem Verstandnis sind Personen ebenso Objekte wie Dokumente, Zahlen oder Zeichen.

Bei der übertragung von realen (d. h., aus einer Anwendungsdomane **verschiedene Arten** stammrenden) Sachverhalten in ein objektorientiertes Programm ergibt **von Objekten** sich das Problem, dass die übertragung, aufgrund der Homogenitat der Objektorientierung (alles ist ein Objekt), gewisse fundamentale Unterschiedlichkeiten der Kategorien unserer Begriffswelt ignoriert: Zahlen beispielsweise sind im Gegensatz zu Dingen Objekte ohne Identitat, Zustand oder Lebensdauer (sie werden daher auch haufig als **Werte** bezeichnet); Mengen nicht weiter abgrenzbarer Elemente wie z. B. 1 Liter Wasser sind gar keine Objekte im eigentlichen Sinn (auch sie haben keine Identitat) usw. Gleichwohl kommen sie alle in objektorientierten Programmen vor und werden dort -- zumindest der reinen Lehre nach -- durch Objekte reprasentiert. Der Ansatz, alles trotz evidenter ontologischer Unterschiede programmiersprachlich über einen Kamm zu scheren, fuhrt hier und da zu gewissen Inkonsistenzen im ansonsten klaren, ja puristischen objektorientierten Weltbild, mit denen wir leben mussen, wenn wir objektorientiert programmieren wollen (vgl. dazu auch Kapitel 60 in Kurseinheit 6). Es ist dies der Preis des auch,,Ockhams Raisermesser" genannten Sparsamkeitsprinzips, das auch für die objektorientierte Programmierung Leitlinie ist. WikipediaA

### 1 Was ist ein Objekt?

Wie bereits erwahnt sind Objekte im Speicher abgelegte Daten. Dabei ist jedes Objekt an genau einer Stelle im Speicher abgelegt: Es wird damit durch seine Speicherstelle eindeutig identifiziert. Aufgrund dieser eindeutigen Identifizierbarkeit spricht man auch von der **Identitat eines Objekts**; sie kann aus technischer Sicht mit der Speicherstelle, an der das Objekt abgelegt ist, gleichgesetzt werden. Da keine zwei Objekte an derselben Stelle abgelegt werden können, haben auch keine zwei Objekte dieselbe Identitat.

Objekte sind grundsatzlich von _Werten_ zu unterscheiden. Werte werden **Objekte vs. Werte** auch im Speicher abgelegt, haben aber keine Identitat. Es folgt, dass derselbe Wert an verschiedenen Stellen im Speicher vorkommen kann. Viele objektorientierte Programmiersprachen (wie etwa Java oder C#) unterscheiden ganz offen zwischen Werten und Objekten; Smalltalk tut dies nur hinter den Kulissen und folgt ansonsten seinem Motto,,alles ist ein Objekt".

Die Menge des Speichers, den ein Objekt belegt, ist aus technischen **Speicherbedarf von** Gründen konstant. Objekte können somit weder wachsen noch schrump- **Objekten**. Solte dies trotzdem notwendig sein, bleibt nur, ein neues Objekt zu erzeugen, das an die Stelle (nicht die Speicherstelle!) des anderen tritt. Das neue Objekt hat jedoch eine andere Identitat, so dass alle Stellen im Programm, die sich auf das alte Objekt beziehen, ent-sprechend angepasst werden mussen. Wie das geht, wird in Kurseinheit 2, Abschnitt 14.2 erlautert.

### Literale

Ein **Literal** (von lat. littera, der Buchstabe) ist eine in der Syntax der Programmiersprache ausgedruckte Repräsentation eines Objektes. Literale sind somit textuelle Spezifikationen von Objekten: Wenn der Compiler ein Literal übersetzt, erzeugt er daraus -- bei der übersetzung! -- das entsprechende Objekt im Speicher. Dies steht im Gegensatz zu objekterzeugenden _Anweisungen_ eines Programms, denn diese werden erst zur Laufzeit des Programms ausgefuhrt. Da wir uns mit der programmgesteuerten Erzeugung von Objekten aber erst in der nachsten Kurseinheit systematisch befassen, mussen wir hier zunächst mit Objekten mit literaler Repräsentation vorliebnehmen. Wohlgemerkt: Literale reprasentieren Objekte, es sind nicht selbst welche.

Die einfachsten Literale reprasentieren Zeichen (genauer: Zeichenobjekt). Um die literale Repräsentation eines Zeichens von anderen Vorkommen von Zeichen in einem Programm zu unterscheiden, wird ihnen in Smalltalk ein $-Zeichen vorangestellt. So bezeichnet das Literal

das Zeichenobjekt _a" 4. Dieses Objekt ist **atomar**, d. h., es ist nicht aus anderen Objekten zusammengesetzt. Zeichen sind in anderen Programmiersprachen -- auch objektorientietten -- ubrigens typischerweise Werte.

Eine andere Art von Literalen, die atomare Objekte reprasentieren, sind **Zahlliterale** die für Zahlen:

ist z. B. ein Literal, das das Objekt _1" bezeichnet;

4 =12.7

ist ebenfalls ein Zahlliteral. Zahlliterale bezeichnen ebenfalls atomare (nicht zusammenge-setzte) Objekte; sie sind in anderen Programmiersprachen typischerweise ebenfalls Werte (nicht jedoch sehr grosse Zahlen mit beliebiger Genauigkeit -- die werden auch in anderen objektorientierten Sprachen durch Objekte reprasentiert).

Die in anderen Programmiersprachen vorzufindenden Literale (oder, je **Literale vs. (Pseudo-)** nach Sprache, _Schlusselworter_) **true**, false und nil (oder null), die **Variable** genau wie Zeichen- und Zahlliterale atomare Objekte reprasentieren, sind in Smalltalk nichtLiterale, sondem _Pseudovariableen_ (s. Abschnitt 1.7). Der Grund dafur scheint eher pragmatischer Natur zu sein: \(\mathtt{Smalltalk}\) kennt keine \(\mathtt{Schlusselworter}\) und indem man \(\mathtt{true}\), \(\mathtt{false}\) und \(\mathtt{nil}\) als (Pseudo-) Variablen auffasst, mussen sie vom Compiler syntaktisch nicht von _Variablen_ (s. Abschnitt 1.5) unterschieden werden. So oder stehen sie für jeweils ein ent-sprechendes Objekt (die in anderen Sprachen wiederum Werte sind).

Wenn es atomare Objekte gibt, dann muss es auch \(\mathtt{zusammengesetzte}\)\(\mathtt{String}\)-Literalegeben. So können beispielsweise Zeichen zu \(\mathtt{Zeichenketten}\), den sogenannten \(\mathtt{Strings}\), zusammengesetzt werden, die ebenfalls Objekte sind. Ein String kann aber selbst wieder durch ein Literal bezeichnet werden; so steht in \(\mathtt{Smalltalk}\)

```
5\(\mathtt{Smalltalk}^{*}\) für ein String-Objekt,,Smalltalk". Dieses Objekt ist selbst aus Objekten, namlich den von den Zeichenliteralen SS, \(\mathtt{Sm}\), \(\mathtt{Sa}\), \(\mathtt{\lx@sectionsign 1}\), \(\mathtt{\lx@sectionsign 1}\), \(\mathtt{St}\), \(\mathtt{sa}\), \(\mathtt{\lx@sectionsign 1}\) und \(\mathtt{\lx@sectionsign k}\) reprasentierten Zeichenobjekten, zusammengesetzt. Was \(\mathtt{Zusammensetzung}\) von Objekten heilst und wie sie funktioniert, darauf gehe ich in den Abschnitten 2.1 und 2.3 noch genauer ein. Es reprasentieren also String-Literale zusammengesetzte Objekte. Daraus ergibt sich die Frage, ob zwei gleiche String-Literale dasselbe Objekt im Speicher reprasentieren. Dies ist nicht grundsatzlich so, wie wir noch sehen werden. Um durch syntaktisch gleiche Zeichenketten stets dasselbe Objekt zu be-zeichnen, bietet \(\mathtt{Smalltalk}\) sog. \(\mathtt{Symbole}\) als weitere Art von Objekten mit literaler Representation. So ist
6\(\mathtt{\#Smalltalk}\) die literale Repräsentation eines Objekts. Es bezeichnet bei jedem Vorkommen im Programm dasselbe Symbolobjekt,,Smalltalk" (nicht zu verwechseln mit dem obigen String-Objekt). Symbole durfen, anders als Strings, nicht alle Zeichen enthalten (so z. B. keine Leerzeichen). Da gleiche Symbolliterale immer dasselbe Objekt reprasentieren, ist die Erzeugung eines solchen Objekts durch den Compiler technisch aufwendiger als beispielsweise die anhand eines String-Literals. Der Compiler muss namlich vor dem Erzeugen erst prufen, ob das Literal schon einmal irgendwo vorkam. Ist das der Fall, erzeugt er kein neues Objekt, sondem verwendet stattdessen das bereits vorhandene. Das setzt naturlich eine entsprechende Verwaltung aller Symbolliterale und dazugehorigen Objekte durch den Compiler voraus.5 Wie man sich leicht vorstellen kann, ware diese Vorgehensweise für die universell und in grosser Anzahl verwendeten Strings sehr zeitaufwendig.

Gleichwohler versuchen manche Smalltalk-Compiler, gleiche Literale, die zusammen kompiliert werden, auf dasselbe Objekt abzubilden. Das fuhrt manchmal, durch das sog. _Aliasing_ (s. Abschitt 1.8), zu unenwarteten Ergebnissen bei der Verwendung dieser Literale.

Die letzte wichtige Kategorie von Literalen in Smalltalk sind **Array-Lite-** **Array-Literale**. Die von ihnen reprasentierten Objekte sind genau wie Strings zusammengesetzt, bestehen aber im Gegensatz dazu nicht nur aus Zeichen, sondern aus einer Folge beliebiger, wieder durch Literale reprasentierter Objekte. Ein Array-Literal wird in Smalltalk vom #Zeichen und einer offnenden Klammer angefuhrt, der durch Leerzeichen getrennte Literale folgen; es wird durch eine schliessende Klammer abgeschlossen.

```
7#(123)isteinsolchesArray-Literal,
8#("Smalltalk"-"ist"1.0"Klasse")

ein anderes. Array-Literale können ineinander geschachtelt sein; das #-Zeichen entfallt jedoch bei allen inneren Arrays. In
9#((SSSmSaS11StSaS1Sk)"ist"1.0"Klasse")

beispielsweiseistdasString-Literal 'Smalltalk' in Zeile 8 durch ein gleichbedeutendes Array-Literal, das aus Zeichenliteralen besteht, ersetzt.

Fur Array-Literale gilt ansonsten das Gleiche wie für String-Literale: Dass zwei syntaktisch gleich sind heist nicht, dass sie dasselbe Objekt erzeugen (oder, richtiger, dass aus ihnen nur ein Objekt erzeugt wird).

### _Anderbarkeit von Objekten_

Wahrend atomare Objekte grundsatzlich nicht anderbar sind (welchen Sinn hatte es beispielsweise, aus einer,,1" eine,,2" zu machen oder aus einem,,a" ein,,b"?), so gilt das für zusammengesetzte zunächst nicht: Es ist leicht vorstellbar (und auch grundsatzlich sinnvoll), in einem Array-Objekt eine Komponente durch eine andere zu ersetzen. Die Frage ist allerdings, ob dies auch für Array-Objekte gilt, die aus Literalen erzeugt wurden: Soll es erlaubt sein, dass das zusammengesetzte Objekt, das aus dem Array-Literal #(123) hervorgegangen ist, durch ein Programm abgeandert wird, so dass es nicht mehr seiner (ursprunglichen) literalen Repräsentation im Programm entspricht? Dies ist Ansichtssache und wird zumindest für String-und Array-Literale von unterschiedlichen Smalltalk-Dialekten unterschiedlich gehandhabt. Objekte, die aus Symbolliteralen hervorgegangen sind, sollten dagegen nie anderbar sein.

[MISSING_PAGE_FAIL:31]

wenn die durch die String-Literale erzeugten Objekte unabhangig voneinanderänder anderbar sein sollen und deswegen tatsachlich zwei Objekte sein mussen. Ubrigens: Phrasen wie,,zwei identische Objekte" sind strenggenommen Unsinn, denn es handelt sich bei vorliegender Identitat definitionsgemass nicht um zwei, sondern nur um ein Objekt. Die Frage nach der Identitat von Objekten ist nur dann sinnvoll, wenn die Objekte durch _Namen_ (oder _Variablen_) reprasentiert werden. Mehr dazu in Abschnitt 1.5.

**Selbstestestaufgabe 1.1**

Prufen Sie in einem oder mehreren lhnen zur Verfugung stehenden Smalltalk-Systemen für verschiedene gleiche Literale, ob die reprasentierten Objekte identisch sind. Beschranken Sie sich dabei nicht nur auf die Beispiele der Zeilen 10-16. Was fallt lhnen auf?

Wahrend man sich unter der Identitat einer Person oder eines Dokuments

**lst es immer sinnvoll,**

leicht etwas vorstellen kann, scheint der Begriff der Identitat für manch

**von Identitat zu**

**sprechen?**

andere Objekte merkwurdig. Was hat man sich beispielsweise unter der

**sprechen?**

**Identitat der Zahl,,1" vorzustellen?**

**Und wenn,,1" tatsachlich ein Objekt mit Identitat ist,**

was macht dieses Objekt zur Eins? Oder ist die 1 vielleicht die Identitat des Objekts,,1",**

sind also das Objekt und seine Identitat dasselbe?**

Im Falle atomarer (also nicht zusammengesetzter) Objekte konnte man

**dentitat**

**und**

**Erscheinung**

**Objekte mit unterschiedlicher Identitat zu haben. So kann man sich beispielsweise fragen, warum man mehrere,,1" mit unterschiedlicher Identitat in einem System haben sollte. Tatsachlich wurde es wohl kaum auffallen, wenn zwei solche gleichen, aber sich dennoch aufgrund ihrer Identitat unterscheidenden Objekte zu einem verschmelzen wurden. Ganzanders ist das bei veränderlichen Objekten: Aufgrund ihrer Veränderlichkeit können sie sich auch nur vorübergehend gleichen, mussen aber selbst wahrend dieser (vorübergehenden) Gleichheit voneinander zu unterscheiden sein, da sie sich hinterher wieder auseinanderentwickeln können und man dann nicht mehr wusste, welches welches war. Da dies aber für unveränderliche Objekte nicht der Fall sein kann, ist es durchaus berechtigt, zu fragen, warum sie sich nur aufgrund ihrer Identitat unterscheiden sollten.**

**Die Antwort ist vor allem technischer Natur. Wenn sich ein unveränderliches Objekt wie beispielsweise eine Zahl nicht aus einem Literal, sondem Aus einer Operation (einer Rechenoperation) ergibt, dann musste, für eine Zusammenlegung gleicher Objekte zu einem, immer erst überpruft werden, ob ein gleichse Objekt bereits angelegt wurde. Da dies Programme stark verlangsamen wurde, nimmt man lieber in Kauf, mehrere gleiche, aber nicht identische Objekte zu haben. Aber warum sind dann gleiche Zahlen manchmal identisch, manchmal nicht? Die Antwort ist noch technischer: Sie hat etwas mit der Repräsentation von Objekten im Speicher zu tun und wird im nachsten Abschnitt gegeben. Und so werden in Smalltalk bestimmte Objekte eben anders behandelt als der Rest: Ganze Zahlen (Integer) bis zu einer bestimmten Grosbeund Zeichen sind aus technischen Gründen immer auch identisch, wenn sie gleich sind -- für den Rest (mit Ausnahme der Symbolel) gilt das nicht. Konzeptuelle Gründe für die Sonderbehandlung gibt es nicht.

Zusammenfassend merken Sie sich am besten folgendes:

\begin{tabular}{c c}  & Quintessenz\end{tabular}

Die Missachtung dieses Merksatzes ist eine der haufigsten Fehlerquellen der objektorientierten Programmierung. Besonders beim Vergleichen von Strings ist die Verwendung des Tests auf Identitat anstelle des Tests auf Gleichheit ein haufiger logischer Programmierfehler. Deswegen noch einmal ganz deutlich:

\begin{tabular}{c}  & Zwei Objekte können zwar gleich, aber nie dassethe sein, oder es sind nicht zwei Objekte, sondern eins! \\ \end{tabular}

Verwenden Sie also grundsatzlich den Test auf Gleichheit (=), nicht auf Identitat (==), es sei denn, Sie wollen prufen, ob Sie es mit einem oder mit zwei Objekten zu tun haben.

### 1.5 Variablen

Weil Literale immer die gleichen Objekte reprasentieren, reichen sie zum Programmieren nicht aus. Was man vielmehr auch noch benotigt, sind **Namen**, die zu verschiedenen Zeitpunkten verschiedene Objekte bezeichnen können6, die sog. **Variable**.

Footnote 6: Achtung: In der _funktionalen Programmierung_, in der der Begriff des Namens gebrauchlicher ist als in der objektorientierten, steht ein Name immer für dasselbe Objekt.

Genau wie ein Literal steht eine Variable in einem Programm für ein Objekt. Anders als bei Literalen wird aus einer Variable jedoch kein Objekt erzeugt: Sie ist lediglich ein Name für ein Bereits existierendes Objekt. Dazu kommt, dass eine Variable zu unterschiedlichen Zeitpunkten für unterschiedliche Objekte stehen kann (deswegen der Name,,Variable"!). Es können zudem Variablen mit unterschiedlichen Namen für dasselbe Objekt stehen, das damit gewissermassen verschiedene Namen hat (die sog. _Aliae_; s. Abschnitt 1.8). Wir werden daher im folgenden davon sprechen, dass Variablen Objekte _benennen_ oder _bezeichnen_.

#### Inhalt

Das bezeichnete Objekt wird manchmal auch,,Wert" oder,,Inhalt" der Variable genannt (und die Variable selbst _Platzhalter_ des Objekts). Besonders die Verwendung von,,Inhalt" ist aber gefahrlich, da sie nahelegt, ein Objekt konne zu einem Zeitpunkt nur von genau einer Variable bezeichnet werden, so wie ein Gegenstand zu einer Zeit immer nur Inhalt eines Behalters sein kann. Tatsachlich können aber mehrere Variablen gleichzeitig ein und dasselbe Objekt bezeichnen -- die Variablen haben namlich nur **Verweise** (auch **Referenzen** oder **Pointer** genannt) auf Objekte (genauer: auf die Speicherstellen, an denen die Objekte abgelegt sind; s. o.) zum Inhalt. Man spricht deswegen auch von einer **Verweis**- oder **Referenzsemantik** von Variablen, im Gegensatz zur **Wertsemantik**, bei der das bezeichnete Objekt tatsachlich auch Inhalt der Variable ist.

Aus technischer Sicht entspricht einer Variable eine Stelle im Speicher. **Variableninhalt auf** Allerdings steht an dieser Stelle bei Variablen mit Verweissemantik nicht **Speicherbene** das Objekt, das sie bezeichnen, sondern lediglich ein Verweis auf die Speicherstelle, an der das Objekt gespeichert ist. Es handelt sich also bei Variablen mit Verweissemantik aus technischer Sicht um **Pointervariablen**, wie man sie auch aus nicht objektorientierten Programmiersprachen wie PASCAL oder C kennt.

Verweis- und Wertsemantik von Variablen unterscheiden sich fundamental: Unter Wertsemantik können, solange jedes Objekt seine eigene Identitat hat, zwei Variablen niemals dasselbe Objekt bezeichnen. Dies wird aber nur den wenigsten Programmierproblemen gerecht. Da zudem die Verweissemantik einen wesentlich speicher- und recheneffizienteren Umgang mit Objekten erlaubt und dunterschiedliche Objekte wie oben beschrieben unterschiedlich viel Speicherplatz belegen, so dass man im Vorfeld nicht immer weiss, wie viel davon man für eine Variable vorsehen muss, ist sie in der objektorientierten Programmierung vorherrschend. In machen Sprachen, die neben Objekten auch Werte kennen, haben Variablen, die Objekte aufnehmen, stets Verweissemantik und Variablen, die Werte aufnehmen, stets Wertsemantik (z. B. Java); andere objektorientierte Sprachen erlauben der Programmiererin, für jede Variable getrennt festzulegen, ob sie Wert- oder Verweissemantik haben soll (so z. B. C++ und Eiffel).

Nun ist besonders für unveränderliche Objekte, deren interne Repräsentation klein ist (die also wenig Speicherplatz belegt), die Forderung nach der Speicherung eines Objektes an genau einem Ort und Speicherung vonVerweisen in Variablen (also die Speicherung in Variablen mit Verweissemantik) ineffizient. Welchen Sinn hatte es beispielsweise, allen Zeichen eine Identitat zu geben, an der mit der jeweiligen Identitat verbundenen Stelle im Speicher die internen Repräsentationen zu hinterlegen und dann in Variablen die Speicherstelle (Identitat) zu speichern, wenn der Verweis mehr Speicher belegt als das Zeichenobjekt, auf das verweisen wird? Das Gleiche gilt auch für Zahlen bis zu einer gewissen Grosse.

In den meisten Smalltalk -Implementation hat man dieses Problem so **Wertsemantik bei gelost**, dass Variablen, die Zeichen, kleine Zahlen und die Booleschen **Kleinen Objekten** Werte **true** und **false** bezeichnen, Wertsemantik haben. Die Objekte können damit aber tatsachlich an mehreren Stellen im Speicher gespeichert werden, was einen Widerspruch zur reinen Lehre darstellt. Zwar geht damit der Begriff der Identitat für diese Objekte verloren, aber für die Programmiererin ist die damit verbundene mehrfache Existenz identischer Objekte im Speicher insofern ohne grosere Bedeutung, als hier Gleichheit problemlos an die Stelle der Identitat treten kann. Der Preis für diese Flexibilitat ist allerdings, dass man den Variablen nicht mehr fix Wert- oder Verweissemantik zuordnen kann -- diese hangt vielmehr jeweils von der Art der Objekte ab, die sie gerade bezeichnen. In diesem Fall wurde man Wert- bzw. Verweissemantik eher als eine Eigenschaft des Objekts denn der der Variable ansehen; das ist jedoch ziemlich Smalltalk-spezifisch.

#### Sichtbarkeit

Eine Variable bezeichnet also ein Objekt. Wer auf eine Variable zugereifen kann, kann damit automatisch auch auf das Objekt zugereifen, das die Variable bezeichnet. Tatsachlich sind alle Objekte, für die es keine eindeutige literale Repräsentation (wie sie Zeichen, manche Zahlen und Symbole haben) gibt, nach ihrer Erzeugung nur noch über Variablen zugereifbar. Die einzige Ausnahme bilden hier die sog. _konstanten Methoden_, die jedoch erst in Abschnitt 4.3.6 behandelt werden.

Nun ist es nicht sinnvoll, dass in einem Programm alle Variablen (und damit auch alle Objekte) von überall her zugereifbar sind. Um den Zugriff auf Variablen einzuschranken, gibt es den Begriff der _Sichtbarkeit_ und _Regen für die Sichtbarkeit von Variablen_. Kurzgefasst ist die Sichtbarkeit einer Variable gleichbedeutend damit, dass man ihren Namen verwenden kann (und damit auch Zugriff auf das von diesem Namen bezeichnete Objekt hat). Dabei bezieht sich die Sichtbarkeit immer auf einen Abschnitt von Programmcode: Wenn eine Variable in einem Abschnitt sichtbar ist, dann entspricht jedes Vorkommen des Variablen- namens in diesem Abschnitt einer ihrer Verwendungen.

Die einzelnen Programmiersprachen unterscheiden sich zum Teil deutlich

**Iokale und globale**

in der Definition ihrer Sichtbarkeitsregeln. Haufig wird jedoch zwischen

**Variablen**

sog. **globalen** und **lokalen Variablen**

unterschieden. Dabei sind beide Begriffe relativ zu verstehen: lokale Variablen sind in ihrer Sichtbarkeit auf den Programmabschnitt beschrankt, um den es gerade geht (sowie ggf. auf dessen Unterabschnitte), globale Variablen sind auch ausserhalb davon (insbesondere in Oberabschnitten) sichtbar. Variablen, die überall sichtbar sind, sind also immer (relativ zu jedem Programmabschnitt) global. Wenn eine Variable ausserhalb eines bestimmten Programmabschnitts, aber nicht überall sichtbar ist, sagt man auch, sie sei global zu dem Programmabschnitt; sie ist dann lokal zu einem übergeordneten (umschliesenden) Programmabschnitt. Lokale Variablen überdecken ubrigens immer globale Variablen gleichen Namens; man spricht dann auch von _Hiding_.

In SMALLtalk mussen globale Variablen mit einem Grossbuchstaben beginen. **Smalltalk** und Transcript sind zwei prominente Beispiele

**konvention in**

fur globale Variablen. Lokale Variablen begininen hingegen mit einem

**Kleinbuchstaben und sind auf den Sichtbarkeitsbereich eines Objekts (oder auch nur Teilen davon) beschrankt. für die genaue Angabe der Sichtbarkeitsregeln SMALLtalkfs feht uns noch einiges; wir werden daher erst in den folgenden Abschnitten darauf eingehen; wir können aber schon hier schlussfolgern, dass in SMALLtalk der Unterschied zwischen lokal und global nicht relativ ist (es also nur zwei verschiedene Programmabschnitte gibt).**

**Selbsttestaufgabe 1.2**

Versuchen Sie, durch Experimentieren herauszufinden, was in der Variable Smalltalk zu finden ist.

### 1.6 **Zuweisung**

Damit eine Variable ein Objekt bezeichnet, muss ihr dieses durch eine sog. **Zuweisung**, in anderen Kontexten auch **Wertzuweisung** genannt, zugeordnet werden. Ursprunglich wurde als _Zuweisungsoperator_ das Symbol _"_" gewahlt; wegen der mangelnden Verfugbarkeit auf Tastaturen wurde es jedoch in den meistem SMALLtalk-Implementerungen durch das aus Algol und Pascal bekannte := ( englisch als _"becomes" gelesen) ersetzt.7 Die Variable lieblingszahl bezeichnet also in Folge der Zuweisung

Footnote 7: **Dass in C und allen davon abgeleiteten Sprachen (sowie in BASIC) das einfache Gleichheitszeichen = für die Zuweisung steht, darl s eine der Tagödien in der Geschichte der Programmiersprachen angesehen werden. Ich möchte nicht wissen, wie viele fatale Fehler auf die dadurch provozierte Verwechselung von Test auf Gleichheit und Zuweisung zurückzufuhren sind.**

**Tieblingszahl := 2**

ein Objekt _"2" (in der Zuweisung reprasentiert durch das Literal 2). Nach einer Zuweisungbezeichnen **x** und **y** das gleiche Objekt (genau welches ist hier nicht erischtlich); ob sie auch dasselbe bezeichnen, hangt von der Semantik der Zuweisung Variablen ab. Man beachte, dass in Smalltalk (anders als in typisierten Sprachen) aus Sicht des Compliers nichts dagegenspricht, der Variable **x** erst eine Zahl und dann einen String zuzuweisen. Auch Array-Literale können jeder beliebigen Variable zugewiesen werden.

Man beachte weiterhin, dass die Zuweisung (anders als der Test auf **zwei Seiten einer** Gleichneit = oder Identtat ==) nicht kommutativ ist: **x** := **y** hat nur dann **Zuweisung** dieselbe Bedeutung wie **y** := **x**, wenn **x** und **y** schon vor der jeweiligen Zuweisung densselben Wert hatten. Zur besseren sprachlichen Unterscheidung der Seite, der zugewiesen wird, und der, die zugewiesen wird, spricht man haufig von der _linken und der rechten Seite einer Zuweisung_.

Nach den drei Zuweisungen

Beispiel

Beispiel

Die Zuweisung ist ein elementares Konstrukt der objektorientierten Programmierung sowie der Programmierung Oberhaupt. Nur die wenigsten Sprachen kommen ohne sie aus. Neben der expliziten Zuweisung durch den Zuweisungsoperator kommt auch eine _implizite_ (bei _Methodenaufrufen_) vor; diese wird jedoch erst in Abschnitt 4.3.2 behandelt.

Der oben geschilderte Unterschied zwischen Wert- und Verweissemantik **Verweissemantik bei **Verweissemantik bei **Zuweisung** unter Wertsemantik muss, da die Variable das Objekt _zum Inhalt_ hat (also in der Variable gespeichert ist) und _ein_ Objekt nicht _in zwei_ Variablen gespeichert sein kann, eine Kopie angefertigt werden. Das hat zur Folge, dass die beiden Variablen **x** und **y** nach der Zuweisung aus Zeile 2 nicht dasselbe (also identische) Objekt bezeichnen (was ja unter Wertsemantik, wie oben Bereits gesagt, auch gar nicht geht), so dass z. B. Anderungen am in **x** gespeicherten Objekt das in **y** gespeicherte Objekt nicht betreffen. Bei einer Zuweisung unter Verweissemantik wird jedoch nur der Verweis der rechten Seite kopiert und in der Variablen auf der linken gespeichert. Wenn die Variablen auf der linken und der rechten Seite unterschiedliche Semantiken haben, dann liegt entweder eine _unzulassige Zuweisung_ (s. Kapitel 18) vor oder es muss, je nach Art der Variable auf der linken Seite, eine Kopie eines Objektes oder ein Verweis auf ein Objekt angefertigt werden (s. dazu auch Abschnitt 52.5.2 in Kursenheit 5).

Finden Sie (durch Experimentieren) heraus, welche Objekte hres Smalltalk-Systems per Wertsematik gespeichert werden. Nutzen Sie dabei aus, das Smalltalk vor der Erzeugung eines Objekts mit Ausnahme von Symbolen nicht pruft, ob das Objekt schon vorhanden ist.

Hinweis: Verwenden Sie den Identifatstest (==).

### 1.7 Pseudovariablen

Wahrend es für Variablen charakteristisch ist, dass sich ihr Wert andern kann, so sieht Smalltalk dennoch einige vor, für die das nicht der Fall ist. Hier sind vor allem die Variablen mit Namen true, false und nil zu nennen, die auf Objekte entsprechender Bedeutung verweisen.8 für diese Variablen ist die Zuweisung nicht zulasig.

Footnote 8: Die Pseudovariablen true, false und nil benennen spezielle, unveränderliche Objekte, auf denen Bedeutung wir noch ausführlich eingehen werden. Bis dahin kann die Leserin davon ausgehen, dass true und false für die Booleschen Werte _wahr” und _falsch” stehen und nil für ein spezielles Objekt, das meistens _kein Objekt” repräsentieren soll.

Eine ganze Reihe weiterer Variablen kann zwar ihren Wert andern (also zu unterschiedlichen Zeiten auf verschiedene Objekte verweisen), jedoch erhalten sie ihren Wert vom System; auch diesen kann durch den _Zuweisungsoperator_ := kein Wert zugewiesen werden. Dies sind z. B. die Variablen mit Namen **self** und **super** sowie alle _formalen Parameter_ von Methoden (s. Abschnitt 4.3). Nicht zuletzt sind auch alle Klassennamen (s. Kurseinheit 2) Variablen, denen man als Programmiererin nichts explizit zuweisen kann. All diese Variablen werden in Smalltalk einheitlich Pseudovariablen genannt.

### 1.8 Aliasing

Wenn Variablen keine Objekte enthalten, sondem lediglich auf sie verweisen, wenn sie also Verweissemantik haben, ist es moglich, dass mehrere Variablen gleichzeitig dasselbe Objekt benennen. Das nennt man **Aliasing**. Das Aliasing ist eines der wichtigsten Phanomene der objektorientierten Programmierung; zugleich ist es leider nur wenig als solches bekannt. Versuchen Sie trotzdem, es sich stets bewusst zu machen -- es wird Sie vor manch boser überaschung bewahren.

**Aliase**, also weitere Namen für ein bereits benanntes Objekt, entstehen immer bei der Zuweisung. Dazu ist es notwendig, dass die Variable auf **Aliasing** der linken Seite Verweissemantik hat. Da in Smalltalk die Semantik von Variablen nicht mit der Variablendeklaration (s. Kapitel 19) festgelegt wird, sondern von der Art eines Objekts abhangt, ist nicht immer klar, bei welcher Zuweisung ein Alias entsthent. Dabei kann beides, die falschliche Annahme von Verweissemantik bei tatsachlicher Wertsemantik und die falschliche Annahme von Wertsemantik bei tatsachlicher Verweissemantik, zu erheblichen (und schwer zu findenden) Programmierfehlern fuhren.

Nach den beiden Zuweisungen

Beispiel

* := #Smalltalk
* := #Smalltalk

hat das eine Objekt, das der Compiler für #Smalltalk erzeugt, zwei Namen, namlich x und y.

Das Aliasing ist zunächst erwunscht: Da jedes Objekt nur einmal im Speicher hinterlegt werden muss, ermoglicht es die extrem effiziente Informationsverarbeitung (es ist weder ein Kopieren notwendig, wenn ein Objekt weitergereicht werden soll, noch mussen die Anderungen an den verschiedenen Kopien zusammengefuhrt werden, die notwendig sind, wenn die Kopien immer noch dasselbe logische Objekt bezeichnen sollen). Doch diese Effizienz hat ihren Preis.

Dass die Veränderung des durch eine Variable bezeichneten Objekts zu-gleich die Veränderung der durch all seine Aliase bezeichneten Objekte (die ja alle dieselben sind) bewirkt, kann namlich unenwunscht, ja ein Programmierfehler sein. So konnte man beispielsweise bei den beiden Zuweisungen

* := 'Muller'
* := petersNachname

lediglich bezwecken wollen, dass Peter und Paula zunächst gleich heissen, z. B. weil sie Gschwister sind. Bei einer spateren Promotion Paulas fugt sie die Zeichen $D, $r und $. in den ihren Nachnamen reprasentierenden String ein, andert also das entsprechende Objekt. Man hat nun sicher nicht beabischtigt, dass das auch **peter**s**Nachname** betrifft, aber wenn die Anderung an einer weit entfernten Stelle im Programm erfolgt, ist die Identifat der von **peters**Nachname** und **paulas**Nachname** benannten Objekte nicht mehr offenschitlich. Tatsachlich hat man es dann mit einem recht subtilen und schwer zu findenden Programmierfehler zu tun. Deswegen (und aufgrund etwas überzeugenderer Beispiele, die zu verwenden aber noch mehr Vorbereitung bedarf) sind in einigen Smalltalk-Systemen alle auf Basis literaler Repräsentation erzeugten Objekte als unveränderlich markiert (wenn Sie es nicht schon, wie beispielsweise Zahlen, von Haus aus sind), so dass Programmierfehler dieser Art vermieden werden. Soltte wie im obigen Beispiel eine Zuweisung mit Wertsemantik benotigt werden, so schreibt man statt Zeile 28 in Smalltalk einfach

* := petersNachname copy

Dabei sorgt das hintangestellte **copy** dafur, dass von dem Objekt, das durch **peter**s**Nachname bezeichnet wird, eine Kopie angefertigt wird, also ein neues Objekt, das dem alten gleicht (mehr zur Syntax und dazu, wofur **copy** steht, folgt unten). Nicht notig wird das Kopieren, wenn ich die Anderung durch die Zuweisung eines neuen Objekts bewerkstellige, wie das beispielsweise in * [30]**paulasNachname := 'Dr. Muller'**

oder gar
* [31]**paulasNachname := 'Dr. '. paulasNachname**

der Fall ist (wobei das Komma hier für die _String-Konkatenation_ steht).

Fehler dieser Art sind haufig die Folge dessen, dass sich eine Programmiererin der aliasbildenden Wirkung der Zuweisung nicht bewusst war. Das ist insbesondere bei den Programmiererinnen der Fall, die nicht mit der objektorientierten Programmierung grosgeworden sind, die insbesondere bei einer Zuweisung **y** := x das Kopieren des Inhalts der Variablen auf der rechten Seite (**x**) vermuten. Tatsachlich muss man in anderen Sprachen (wie beispielsweise Pascal oder C) eine Variable explizit als _Pointervariable_ dekAlarieren, um einen Alias bilden zu können. In Smalltalk, genau wie in Java und C#, ist Aliasing jedoch der Regelfall und Kopie die Ausnahme. Wer das nicht verinnerlicht hat, schreibt hochstens zufallig korrekte Programme.

### _Lebenslauf von Objekten_

In Smalltalk beginnt der Lebenslauf eines Objekts mit seiner Erzeugung und endet mit seiner Entsorgung durch eine Speicherbereinigung, die sog. **Garbage collection**. Garbage collection ist ein Mechanismus, der Objekte aus dem Speicher entfermt, wenn diese nicht mehr zugereifbar sind. Da in Smalltalk auf Objekte nach ihrer Erzeugung ausschliesslich über Variablen (Namen) zugegriffen werden kann, kann ein solches Objekt genau dann entfermt werden, wenn keine Variable mehr auf es verweist. Es _kann_ entfermt werden, muss aber nicht; aus Sicht der Programmiererin ist es ausreichend, dass das Objekt nicht mehr bekannt/benannt ist -- es kann somit nicht mehr aufgefunden und durch eine Zuweisung einer Variable zugewiesen werden. Bei der Implementierung von Garbage-collection-Algorithmen besteht denn auch erhebliche Freiheit.

Wenn Peter und Michaela heiraten, dann schlagt sich dies u. a. in der Zuweisung

* [32]**petersNachname := michaelasNachname**

nieder. Wenn 'Muller' keine Aliase (wie beispielsweise paulasNachname) hatte, kann es nach der Zuweisung aus dem Speicher entfermt werden -- es ware selbst bei Bedarf nicht mehr auffindbar.

Von der automatischen Speicherbereinigung ausgenommen sind bestimmte Objekte mit eindeutigter literaler Repräsentation (wie z. B. kleine

**Sonderbehandlung**

**bestimmter Objekte**

Zahlen, Zeichen und Symbole). Im Falle von Zahlen und Zeichen liegt das jedoch weniger an der Natur dieser Objekte selbst als vielmehr an der Tatsache, dass diese in der Regel nicht als Objekte im Speicher angelegt werden (so dass Variablen darauf verweisen konnten),sondern dass sie selbst, als Werte (und anstelle von Zeigern), in Variablen gespeichert werden (Abschnitt 1.5.1). Sie werden,,entfernt", indem einer Variable ein neuer Wert zugewiesen wird. Symbolic werden schon deswegen nicht aus dem Speicher entfernt, weil sie in einer Symboltable abgelegt (und somit immer mindestens einmal referenziert; s. Fussnote 5) werden.

Der Mut zur Verabschiedung von der expliziten Speicherfreigabe war eine der wichtigsten Entscheidungen beim Entwurf Smalltalks. Man hat einfach anerkannt, dass die genaue Buchfuhrung darüber, auf welche Objekte noch zugegriffen wird, zu schwierig ist, um die Verantwortungsfort Anwendungsprogrammirerinnen zu überlassen. Wer das Problem nicht unmittelbar einschtig ist, die halte sich vor Augen, dass

* der Ort der Erzeugung eines Objektes und seine erste Zuweisung zu einer Variabl im Programm moglicherweise weit entfernt sind von der Stelle, an der dieser Variable ein anderes Objekt zugewiesen wird, dass
* es moglicherweise viele solcher Stellen gibt, von denen mal die eine, mal die andere zuerst erreicht wird, und dass
* in der Zwischenzeit beliebig viele Aliase auf das Objekt angelegt worden sein können, die alle mitterucksichtigt werden mussen, um zuentscheiden, ob das Objekt noch in Verwendung ist.

Eine vorzeitige Entfernung aus dem Speicher hingegen fuhrt dazu, dass Variablen ins Nichts zeigen (eine haufige Quelle von Programmabsturzen) oder dass, bei einer Wiedervenwendung des Speichers, die Variable plotzlich auf ein anderes Objekt verweist, das ihr aber nie explizit zugewiesen wurde -- ein quasi zufalliges Programmverhalten, das mit hoher Wahrscheinlichkeit zu schweren Programmfehlem fuhren wurde. Ein anderes Beispiel entsteht, wenn in einer Verzweigung eines Programms entweder ein neues oder ein bereits vorhandenes Objekt einer Variable zugewiesen wird. Woher weiss man bei der weiteren Benutzung dieser Variable, ob das Objekt schon vorher existierte und vielleicht schon andere Variablen auf es verweisen, oder ob es gerade erst neu erzeugt wurde und damit noch unbenutzt ist? Wer ist für die Entsorgung des Objekts verantwortlich? All diese Betrachtungen kann man sich in Gegenwart der Garbage collection persparen.

Im objektorientierten Jargon spricht man ubrigens haufig auch vom **Lebenszykus** (_,life cycle") eines Objekts. Genaugenommen ist dies aber irrefuhrend, denn das Wort,,Zylkus" verspricht, dass das Leben nach seinem Ende wieder neu beginnt. Gerade dies ist aber, wie eben erlautert, nicht der Fall: Objekte werden nicht recycelt, sondern hochstens der Speicherplatz, den sie belegen.

### Zusammenfassung

Objekte können also über textuelle Repräsentationen, die sog. _Literale_, in ein Programm eingefuhrt und _Variablen_ zugewiesen werden. Dabei speichern die Variablen die Objekte in aller Regel nicht, sondern benennen sie lediglich. Technisch gesehen enthalten die Variablen dann _Verweise_ (Referenzen, Zeiger, Pointer) auf die Objekte, die selbst durch Stellen im Speicher reprasentiert werden (sog. _Referenzsemantik_). Wenn mehrere Variablen dasselbe Objekt bezeichnen, spricht man von einem _Aliasing_. Aliasing erlaubt über die gemeinsame Nutzung von Objekten eine aüberordentlich speicher- und recheneffiziente Informationsverarbeitung. Gleichzeitig stellt es aber eine der grosten Fehlerquellen der objektorientierten Programmierung dar, da im allgemeinen nicht bekannt ist, ob und wie viele Aliase auf ein Objekt exstieren. Ein besonderes Problem liegt vor, wenn sich die Programmiererin nicht bewusst ist, dass sie (nur) mit Aliasen hantiert, und sich dann wundert, wenn sich an entfernten Orten plotzlich die (vermeintlichen, denn eigentlich sind es ja gar keine) Inhalte von Variablen andern.

## 2 Beziehungen

Kein Objekt ist eine Insel. Ganz im Gegenteil: Damit Objekte eine Bedeutung haben, mussen sie mit anderen in Beziehung stehen. Das Objekt,,1" beispielsweise ist ohne Bedeutung, solange es nicht eine bestimmte Eigenschaft eines anderen Objekts beschreibt, wie z. B. die Hausnummer eines Hauses oder die Anzahl der Elemente eines Arrays. Tatsachlich werden die meisten Objekte eines Systems erst durch ihre Beziehungen zu anderen zu etwas Nutzlichem. Ein Objekt, das beispielsweise eine Person reprasentiert, macht den String,,Hans Mustermann" zum Namen der Person, sobald er mit der Person in entsprechennder Beziehung steht; umgekehrt wird für die Benutzerin des Systems die Person erst über den Namen identifizierbar.

Tatsachlich wird, wie bereits eingangs dieser Kurseinheit envahnt, in der objektorientierten Programmierung samtliche Information als ein Geflecht von Objekten dargestellt. Dieses Geflecht kann

1. navigiert werden, um von einem Datum (Stuck Information) zu einem anderen zu kommen, oder auch
2. manipuliert werden, um die reprasentierte Information zu verändern.

Das Datenmodell der objektorientierten Programmierung ahnelt damit stark dem _Netzwerkmodell_, das ebenfalls ein navigerendes ist, das vor einigen Jahrzehnten einmal die Grund-lage grosser Datenbankmanagementsysteme war, das aber schnell vom _relationalen Datenmodell_ verdrangt wurde und das erst heute, im Zuge der Einfuhrung von objektorientierten Datenbanken, wieder an (theoretischer) Bedeutung gewinnt.

In der objektorientierten Programmierung werden Beziehungen zwischen Objekten über Verweise hergestellt, durch deren Verfolgung man von einem Objekt zum nachsten gelangen, eben,,navigieren" kann. Das Besondere dieser Verknupfung ist, dass sie stets gerichtet ist: Dass man von einem Objekt zum nachsten navigieren kann, heißt nicht, dass man auch wieder zuruckkommt. Dazu ist dann ein Zeiger in Gegenrichtung notig.

Nun enthalten ja Variablen ebenfalls Verweise. Wer also Zugriff auf die Variable hat, hat damit auch Zugriff auf das referenzierte Objekt -- und ist somit mit dem Objekt verknupft. Was noch fehlt, ist, dass Variablen Objekten so zugeordnet werden, dass nur noch die Objekte Zugriff darauf haben, und schon kann man auf einfache Weise Beziehungen ausdrucken.

### _Instanzvariablen_

Jedem Objekt kann eine Menge von _Iokalen Variablen_ zugeordnet werden. Aus Gründen, auf die wir noch zu sprechen kommen, heißen diese Variablen **Instanzvariablen**, sie werden aber manchmal auch _Felder_ oder _Attribute_ (zu Attributen s. Abschnitt 2.4) genannt. Die Instanzvariablen eines Objekts sind in gewisser Weise in seinem Besitz: Sie sind für andere Objekte nicht sichtbar und damit auch nicht zugerifugar. Die Sichtbarkeit ist also auf das jeweils besitzende Objekt eingeschrankt.9 Außerdem ist die Existenz dieser Variablen an die Existenz (oder Lebensdauer; s. Abschnitt 1.9) des besitzenden Objekts gebunden.

Instanzvariablen bestimmen den Aufbau, oder die **Struktur**, zusammengesetzter Objekte (die manchmal deswegen auch _strukturierte Objekte_ genannt werden) -- atomare Objekte haben keine Instanzvariablen. Jede Instanzvariable eines Objekts belegt dabei einen Teil des Speichers aus seiner Repräsentation(S. Abschnitte 1.1 und 1.5). Da Instanzvariablen in der Regel Verweise enthalten und Verweise immer den gleichen Platz belegen, ist die Grosse eines Objekts (der zu seiner Speicherung benotigte Platz) mit der Anzahl seiner Instanzvariablen festgelegt.

In Smalltalk werden zwei Arten von Instanzvariablen unterschieden: **benannte** und **indizierten**. Jede benannte Instanzvariable benennt (oder verweist auf) jeweils ein Objekt; der Name der Variable wird somit für die Dauer, die die Variable auf das Objekt verweist, auch zum Namen des Objekts. Da es sich bei Instanzvariablen um lokale Variablen handelt, muss der Name einer benannten Instanzvariablen in Smalltalk mit einem Kleinbuchstaben beginnen.

Indizierte Instanzvariablen haben keine Namen, sondern werden über einen Index relativ zu dem Objekt, zu dem sie gehoren, angesprochen. Damit ist der Index gewissermansen der Name der Instanzvariable. Der Index muss eine naturliche Zahl groBer 0 sein. Um den Inhalt der indiizierten Instanzvariable an der Indexposition **i** (genauer: an der Indexposition, die durch das Zahlobjekt bestimmt wird, auf das **i** verweist) zu erhalten, schreibt man
33at: **1**

Wer bei indiizierten Instanzvariablen an Arrays denkt, liegt richtig: Tatsachlich speichern Array-Objekte ihre Elemente in indizierten Instanzvariablen. So liefert beispielsweise
34#(Sa Sb Sc) at: **2**

das Zeichenobjekt,,b". Um den Wert einer indiizierten Instanzvariable an derselben Indexposition zu setzen, schreibt man z. B.
35#(Sa Sb Sc) at: **2** put: 'toll!'

(aber nur, wenn lhr Smalltalk die Anderung der Zusammensetzung für literale Arrays zulasst). Das resultierende Array-Objekt hat die literale Repräsentation **#**(Sa 'toll!' Sc).

Indizierte Instanzvariablen sind kein Unikat von Smalltalk: So bieten beispielsweise C# und Visual Basic sog. _Indexer_, die im wesentlichen indiizierten Instanzvariablen entsprechen (s. Abschnitt 50.3.2 in Kurseinheit 5). Auch verfugen manche Objekte in Visual Basic for Applications (VBA) über eine Variable Item, deren Elemente über Indizierung des Objekts, dem sie zugeordnet ist, angesprochen werden können.

Die Anzahl der inidizierten Instanzvariablen eines Objekts ist fix. Damit ist auch die Grosse eines Objekts mit indizierten Instanzvariablen fest; insbesondere können Array-Objekte nicht wachsen (und wenn doch, dann nur über den in Abschnitt 1.1 erwahnten Trick mit dem Wechsel der Identifat). Es mussen aber nicht alle inidizierten Instanzvariablen belegt sein; die,,leeren" enthalten dann nil (s. u.).

Es bleibt noch die Frage, wie Objekte in SMalltalk in den Besitz von Instanzvariablen gelangen. Um das zu erklaren, musste an dieser Stelle auf das Konzept der Klasse vorgegriffen werden, was aber aus didaktischen Gründen unterbleiben soll. Gelemte Pascal-Programmierrinnen können sich die Instanzvariablen aber wie die Felder eines Records vorstellen (oder C-Programmiererinnen wie die eines Structs), die in der Record-Definition festgelegt werden und die für jede Variable vom Typ dieses Records zur Verfugung stehen. für alle anderen mag es reichen, sich vorzustellen, jedes Objekt verfuge automatisch über zwei spezielle Variablen, die die Namen und die zugewiesenen Objekte aller seiner Instanzvariablen verwalten. Wie so etwas gehen kann, wird in der nachsten Kurseinheit klanwerden.

### Unterscheidung von :1- und :_n_-Beziehungen

In der Daten- und Softwaremodellierung werden Beziehungen (oder Relationen) haufig mit sog. _Kardinalitaten_ versehen. (Manchmal, besonders im Kontext der Softwaremodellierung mit der Unified Modeling Language _UML_ werden diese auch _Multiplizitaten_ genannt.) Sie geben an, mit wie vielen anderen Objekten ein Objekt gleichzeitig in derselben Beziehung stehen kann. Beispielsweise kann eine Person zu mehreren anderen Personen in einer Verwandtschaftsbeziehung stehen. Haufig sind die moglichen Kardinalitaten auf ein Intervall beschrankt; sie werden dann durch eben dieses Intervall beschrieben.

Von den theoretisch unendlich vielen moglichen Intervallen, die die Kardinalitat beschranken können, sind vor allem drei interessant: [0..1], [1..1] und [0..\(\infty\)). Dabei ist [1..1], also dass ein Objekt immer mit genau einem in Beziehung stehen muss, technisch nur schwer umzustzen, so dass [1..1] hier nicht weiter betrachtet wird11; die untere Schranke 0, die den beiden verbleibenden Intervallen gemeinsam ist und die ausdruckt, dass ein Objekt auch mit gar keinem anderen in der Beziehung stehen kann, muss daher nicht erwahnt werden. Im Fall von [0..1] sprechen wir also von **Zu-eins-Beziehungen** (im folgenden mit :**1-Beziehung** notiert), im Fall von [0..\(\infty\)) von **Zu-n-Beziehungen** (:**n-Beziehungen**), wobei \(n\) hier andeuten soll, dass es sich um eine nicht naher spezifizierte Zahl grosser als 1 handelt.12Die Beziehung eines Objekts zu einem anderen wird auf naturliche Weise :**1-Beziehungen durch eine benannte Instanzvariable ausgedruckt, wobei die Instanzvariable den Namen der Beziehung oder, besser noch, den Namen der Rolle des von der Variablen referenzierten Objektes in der Beziehung tragt. So zeigt die Instanzvariable arbeitgeber beispielsweise auf das Objekt, das in der Beziehung _Anstellung_ aus Sicht des Arbeitnehmerobjekts die Rolle des Arbeitgebers spielt. Hat auch das Arbeitgeberobjekt einen Verweis auf das Arbeitnehmerobjekt (die Ruckrichtung), so wird die entsprechende Variable sinnvollerweise nach der Gegenrolle arbeitnehmer genannt. Setht ein Arbeitnehmerobjekt zur Zeit in keinem Anstellungsverhaltnis, ist seine Instanzvariable arbeitgeber leer, was in Smalltalk durch den Verweis auf das Objekt nil ausgedruckt wird.13

Footnote 12: Diese Konvention wurde vom Turing-Preistrager Sir Charles Antony Richard Hoare eingeführt, der sie heute selbst als einen (seinen),,billion dollar mistake" bezeichnet.

Beziehungen sind nicht von Natur aus auf _ein_ Gegenüber eingeschrankt: :**_n-Beziehungen_ Ein Objekt kann, und wird haufig, in derselben Beziehung zu mehreren andern stehen. Genau dafur sind aber die indiizierten Instanzvariablen wie geschaffen: Sie erlauben es, von einem Objekt zu beliebig vielen anderen Objekten zu navigheren, ohne für jedes andere eine eigene (jeweils anders) benannte Instanzvariable vorsehen zu mussen. Die,,Namen" der Gegenüber sind einfach Indizes: 1, 2, 3 usw.

Es ergibt sich nun aber das Problem, dass bei durch indiizierte Instanzvariablen eines Objekts realisierten :_n-Beziehungen nicht zwischen verschielenen solchen Beziehungen desselben Objekts unterschieden werden kann -- die indizierten Instanzvariablen sind ja nicht benannt. Deswegen werden :_n-Beziehungen_ in der objektorientierten Programmierpraxis praktisch immer über **Zwischenobjekte** realisiert, deren Aufgabe es ist, mittels ihrer indiizierten Instanzvariablen jeweils _eine_ Beziehung zu mehreren anderen Objekten herzustellen. Dabei können diese Zwischenobjekte die :_n-Beziehung ggf. mit weiteren Attributen (z. B. Anzahl \(n\), Verweise auf ein bestimmtes Element, Art der Sortierung o. a.) versehen, die dann in den benannten Instanzvariablen der Zwischenobjekte untergebracht werden. Das Originalobjekt, das die :_n-Beziehung eigentlich haben sollte, steht dann statttdessen in einer von einer benannten Instanzvariable hergestellten :1-Beziehung zu dem Zwischenobjekt, das die :_n-Beziehung herstellt.

Wie wir noch sehen werden, erlaubt der Umstand, dass :\(n\)-Beziehungen

**Vorteile von**

über Zwischenobjekte realisiert werden, die vollwertige Objekte sind, die

**Zwischenobjekten**

Beziehungen beliebig auszugestalten. So kann beispielsweise eine (Sortier-)Reihenfolge vorgegeben oder ein ausgezeichnetes Element der Beziehung noch einmal gesondert referenziert werden (z. B. das oberste Element auf einem Stack). Auch besondere Zugriffsverfahren wie z. B. das Auffinden von Elementen (in Beziehung stehenden Objekten) anhand eines Schlussels können auf diese Weise realisiert werden. Da in Smalltalk Objekte auch eigene Kontrollstrukturen (wie z. B. spezielle Schleifen) anbieten können, sind der Ausgestaltung von Beziehungen über Zwischenobjekte praktisch keine Grenzen gesetzt.

Da :\(n\)-Beziehungen haufig vorkommen, ist ihre Handhabung von entscheidender Bedeutung für die Ausdrucksstarke der verwendeten Programmiersprache und die Produktivitat der Programmierung insgesamt. Wie sich schon in Abschnitt 4.6.4 zeigen wird, erlaubt die Ausgestaltung von Zwischenobjekten in Smalltalk Moglichkeiten, die bis heute Vorbilcharakter für andere objektorientierte Programmiersprachen haben.

### Teil-Ganzes-Beziehungen

Eine Sonderrolle unter den Beziehungen nimmt die sog. _Teil-Ganzes-Beziehung_, je nach Kontext und Jargon auch _Komposition_ oder _Aggregation_ genannt, ein. Teil-Ganzes-Beziehungen bestimmen ganz wesentlich unsere Weltsicht: Alles, was wir anfassen oder betrachten können, ist aus kleineren Teilen zusammengesetzt, die selbst wieder Zusammensetzungen (Aggregate, Komposita) sind bis hinner zu den Elementar-, d. h., unteilbaren Bausteinen.

Nun ist der Begriff der Teil-Ganzes-Beziehung leider nicht so klar definiert, wie es auf den ersten Blick scheint. Tatsachlich bestehen, je nach Art der Zusammensetzung, zum Teil vollig unterschiedliche Wechselwirkungen zwischen dem Ganzen und seinen Teilen. Zudem gibt es neben der physischen Teil-Ganzes-Beziehung auch eine logische: So ist z. B. der Deutsche Bundestag aus einer Anzahl von Abgeordneten zusammengesetzt und jede Familie aus ihren Mitgliedern. Tatsachlich gibt es so viele Varianten der Teil-Ganzes-Beziehung, dass der (philosophische) Diskurs darüber ganze Regale fullt und zu einer eigenen Disziplin gefuhrt hat (der sog. _Mereologie_). Verstandlichenweise kann dem eine Programmiersprache nicht folgen und für jede dieser Beziehungen ein eigenes Sprachkonstrukt anbieten.

Stattdessen bieten die meisten (objektorientierten) Programmiersprachen aber leider überbraupt kein Sprachkonstrukt an, das speziell für die Teil-Ganzes-Beziehung gedacht ware. Gleichwohl kann man die Unterscheidung zwischen Instanzvariablen mit Referenz- und Wertsemantik, falls vorhanden, dazu nutzen, um zumindest eine spezielle Form der Teil-Ganzes-Beziehung abzubilden: Da bei Wertsemantik mit der Entfernung eines Objekts aus dem Speicher auch alle Objekte, die als Werte seiner Instanzvariablen dienen, aus dem Speicher entfernt werden, kann man hier tatsachlich von der Umsetzung einer bestimmten Form von Teil-Ganzes-Beziehung sprechen, namlich einer solchen, bei der die Existenz der Teile von der Existenz des Ganzen abhangt (in der UML auch _Komposition_ genannt). für andere Formen, wie z. B. die Bildung einer Gruppe von Objekten als Objekt mit eigener Identiftat (einem Verein beispielsweise), ist dieses Modell aber nicht geeginet, da sonst mit Auflosung der Gruppe auch die Gruppenmitglieder verschwinden mussten. für die Smalltalk-Programmirerein sind diese überlegungen aber sowieso kein Thema, denn sie hat die Wahl erst gar nicht.

Mit der Teil-Ganzes-Beziehung auf Programmebene werden wir uns in Kurseinheit 6 (genauer: Kapitel 58 und 59) noch ausführlicher beschaftigen. Hier sei nur schon soviel gesagt, dass die Moglichkeit des (rekursiven) Aufbaus eines Software-Systems aus Teilen, die jeweils ihren inneren Aufbau (ihre Komposition) _kapseln_, also insbesondere die Nichtexistenz von Aliasen auf ihre Teile garantieren, genau das ist, was der objektorientierten Programmierung im wesentlichen bis heute fehlt.

### 2.4 Attribute

Logisch kann man Instanzvariablen in zwei Kategorien auftfeilen: solche, die Eigenschaften eines Objekts festhalten, und solche, die tatsachliche Beziehungen zwischen Objekten reprasentieren. Typische Eigenschaften sind beispielsweise die Farbe von etwas oder der Name; sie grenzen sich von Beziehungen inhatlich dadurch ab, dass das bezogene Objekt isoliert betrachtet seine Bedeutung verliert. So ist das Objekt **rot** allein nichts weiter als eine Farbe -- erst als Attribut eines Objekts (wie z. B. _,Apfel") bekommt es eine Bedeutung. Das gleiche gilt für _,Schmidtchen" oder _,1". Dazu kommt, dass Attributwerte wie die vorgenannnten in der Regel selbst keine Attribute haben oder Beziehungen mit anderen Objekteneineben. Man beachte jedoch, dass dieses Unterscheidungskriterium nicht absolut, sondern relativ zur jeweils betrachteten Domane ist: Wenn es z. B. um Farben geht, ist,,rot" ein Objekt, das für sich genommen schon eine Bedeutung hat und das mit anderen Objekten vollwertige Beziehungen eingeht, so z. B. mit,,grun" als seinem Komplementarkontrast.

Wenn wir eben von _Attributwerten_ sprachen, so ist das nicht ganz zufallig: Nicht selten haben Variablen, die Attribute reprasentieren, zumindest

**Attribute mit**

**Wertsemantik**

logisch eine Wertsemantik, d. h., sie halten (oder verweisen auf, je nach Implementierung der Sprache) eigene Kopien eines Objekts. Ein typisches Beispiel hierfur hatten Sie in Abschnitt 1.8 bereits kennengelernt: So ist es sinnvoll, dass die Anderung des Namens (genauer: des Namensobjekts) bei einer Person nicht gleichzeitig andere Personen, die den gleichchen (nicht denselben!) Namen haben, betrifft. Eine ahnliche überlegung spielt im Zusammenhang mit der Betrachtung des Zustandes eines Objekts eine Rolle.

## 3 Zustand

Wie bereits in Abschnitt 1.3 beschrieben, kann man zwischen _veränderlichen_ und _unveränderlichen Objekten_ unterscheiden. Veränderungen veränderlicher Objekte erfolgen über die Zeit und die Objekte wechseln dabei ihren **Zustand**, unveränderliche Objekte dagegen haben keinen Zustand.14 Was aber macht den Zustand eines Objektes aus?

Footnote 14: Wenn sie einen hatten, dann immer denselben. Da der Begriff des Zustandes jedoch ohne die Mölichkeit der Veränderung kaum einen Sinn hat, sprechen wir auch nicht vom Zustand unveränderlicher Objekte wie z. B.,,1". Manche Smalltalk-Dialekte sehen jedoch eine Instanzvariable immutable vor, die die Veränderlichkeit von Objekten festlegt und die, so ihr Wert denn geandert werden kann, die (Un-)Veränderlichkeit selbst zu einem Teil des Zustandes von Objekten macht.

Der Zustand eines Objektes ist die Summe der Belegungen seiner Instanzvariablen. Insofern Instanzvariablen Beziehungen ausdrucken, wird der Zustand eines Objektes ausschlieblich durch seine Verknupfung mit anderen Objekten definiert. Zudem folgt, dass die einzige Moglichkeit, den Zustand eines Objekts zu andern, der über die Zuweisung von Instanzvariablen, gleichbedeutend mit der Anderung seiner Beziehungen, ist.

### **Eingrenzung**

Eine etwas eingeschranktere Sicht vom Zustand eines Objektes bezieht nur seine _Attributwerte_ ein. Dies setzt jedoch voraus, dass überhaupt formal zwischen Attributen und Beziehungen unterschieden werden kann. In Ermangelung spezieller Schlusselworter konnte dies, wie bereits oben diskutiert, allenfalls über die Unterscheidung von Variablen mit Wert- und solchen mit Referenzsemantik erfolgen. Dies ist jedoch schon in Sprachen, die der Programmiererin eine entsprechende Entscheidung anbieten, nicht automatisch der Fall (z. B. Java, da hier Strings zwar unveränderlich sind und somit eigentlich zu den Werten Zahlen, aber dennoch Referenzsemantik haben); in SMALLtalk schlieslich ist, da alle Instanzvariablen Referenzen enthalten können, diese Einschrankung überhaupt nicht anwendbar.

Man konnte nun die obige Aussage, dass Zustandsanderungen eines Objektgeflecht der **Zeit**

**Raichweite von**

jekts ausschlieslich über Zuweisungen an seine Instanzvariablen erfolgen

**Zustandsanderungen**

können, anzweifeln und fragen, ob sich der Zustand eines Objektes auch dann andert, wenn sich der Zustand eines Objektes, auf das es (per Instanzvariable) verweist, andert? zunächst wurde man diese Frage mit nein beantworten, denn sonst wurde ja, da Objekte in der Regel stark miteinander verflochten sind, die Anderung des Zustandes eines Objektes fast immer zu einer wahren Kettenreaktion fuhren: Der Zustand aller Objekte, die direkt oder indirekt -- also über dritte -- darauf verweisen, wurde sich mit andern. Diese Definition von Zustand wurde jedoch kaum unserem Weltbild entsprechen: Die Anderung Ihres Familienstandes beispielsweise wurde kaum etwas an meinem Zustand anern, obwohl Sie meine Kurstexe geschickt bekommen, ich also in einer (direkten oder indirekten) Beziehung zu lhnen stehe. Wie aber ist es, wenn ich meinen Namen andere? Andert sich dann mein Zustand?

Wahrend man diese Frage sicher mit ja beantworten wird, ist doch mein

**Sonderfall Strings**

Name als String ein eigenstandiges Objekt, das seinen Zustand wechselt, wenn ich, wie im Beispiel von Abschnitt 1.8 geschehen, einzelne Buchstaben in ihm austausche oder erganze. Nach obiger Auffassung andert sich mein Zustand (als Besitzer des Namens) dadurch nicht, denn es bleibt ja dasselbe (per Identit) String-Objekt, das meinen Namen halt -- es hat lediglich seinen Zustand gewechselt. Etwas anderes ware es hingegen, wenn ich das String-Objekt, das meinen Namen reprasentiert, gegen ein anderes austausche: Dann verweist die entsprechende Instanzvariable auf ein anderes Objekt und mein Zustand hat sich sicher gednert. Gleichwohl wurde man dasselbe auch von der Namensanderung per String-Manipulation erwarten, nur technisch lasst sich dieser Sonderfall nicht begründen! Wie Sie sehen, ist das objektorientierte Denkmodell nicht ganz ohne Tucken, und Programmierfehler schleichen sich an Stellen ein, die so simpel aussehen, dass man dort nie einen Fehler vermuten wurde. Vielleicht auch deswegen ist es sinnvoll, wenn Strings, wie von einigen SMALLtalk-Dialekten (und ubrigens auch von Java) vorgesehen, immer unveränderlich (immutable) sind.

Auch wenn es nicht sinnvoll ist, für ein allgemeines Objektgeflecht den

**Zustand und**

Zustandsbegriff auf mehrere Objekte auszudehnen, so ist dies für Komponenten, also aus Teilen zusammengesetzten Ganzen (vgl. Abschnitt 2.3), durchaus angemessen: Wenn z. B. ein Dokument aus mehreren Seiten besteht, die wiederum jeweils aus Zeilen und Spalten bestehen, dann andert die Anderung einer Zeile auch den Zustand des gesamten Dokuments. Dies wird weiter unten noch eine Rolle spielen, vor allem im Zusammenhang mit Aliasing: Wenn man namlich davon ausgeht, dass Zustandsanderungen eines Objekts stets Sache des Objekts selbst sind, dann durfen keine externen Aliase auf seine Teile existieren, denn sonst konnte ihm eine Zustandsanderung von ausen quasi untergejubelt werden. Man sollte

den Zustand also kapseln.

### Kapselung

Die Unterscheidung von lokalen und globalen Variablen aus Abschnitt 1.5.2 dient u. a. dem Verbergen von Geheimnissen (das sog. **Geheimnisprinzip** engl. auch **Information hiding** genannt), genauer von **Implementationsgabeinmissen**. So ist es fast immer sinnvoll, die Struktur zusammengesetzter Objekte vor den sie benutzenden Objekten zu verbergen, damit man diese Struktur spater andern kann, ohne dass die benutzenden (abhangigen) Objekte davon betroffen waren. Derartige Anderungsbhangigkeiten werden verhindert, wenn die Variablen von außen gar nicht zugereifbar sind, was für lokale Variablen, die ja von aussen unsichtbar sind, automatisch der Fall ist.

Vom Geheimnisprinzip abzugrenzen ist der Begriff der **Kapselung**, den **Iokale Variablen und** man mit der objektorientierten Programmierung verbindet: Ein Objekt soll**Kapselung** seinen Zustand kapseln, so dass dieser nur von ihm selbst geandert werden kann. Anders als beim Information hiding geht es bei der Kapselung also nicht um Anderungen des Aufbaus von Objekten, sondem um Anderungen ihres Zustandes. Leider lasst sich die Kapselung nicht mit denselben Mittlein wie das Geheimnisprinzip umsetzen: Aufgrund des Aliasing kann ein Objekt, dessen einer Name (beispielsweise aufgrund des Geheimnisprinzips) unsichtbar ist, über einen anderen zugereifbar sein, ohne dass der erste Name etwas dagegen machen konnte. über lokale Instanzvariablen kann ein Objekt also verbergen, welche Objekte es kennt; es kann aber nicht verhindern, dass andere Objekte diese Objekte auch kenn und, ohne sein Wissen, manipulieren. Es ist somit wegen der etwaigen Existenz von Aliasen nicht moglich, dass ein Objekt seinen inneren Aufbau vor der Aussenwelt _abkapselt_, es sein denn, es hat ganz spezielle Vorkehrungen dafur getroffen. Da diese Vorkehrungen (derzeit noch) in keine gangige objektorientierte Programmiersprache eingbeaut sind15, sondern explizit programmiert werden mussen, werden wir uns hier (in dieser Kurseinheit) nicht weiter damit beschaftigen; eine weitergehende Betrachtung erfolgt in Kapitel 58 von Kurseinheit 6).

Footnote 15: Die Programmiersprache Rust ist hier vielleicht eine Ausnahme.

## 4 Verhalten

Wenn Objekte ihren Zustand kapseln, ist es ausschliesslich ihr Verhalten, welches ihn andert, welches also die Zustandsanderungen eines Objekts herbeifuhrt. Umgekehrt hangt das Verhalten eines Objekts in der Regel von seinem Zustand ab. Wie aber wird das Verhalten eines Objekts beschrieben? Bevor wir uns dieser Frage zuwenden, mussen wir erst wir zunächst den Begriff des _Ausdrucks_ klaren.

### **Ausdrucke**

In einem objektorientierten Programm können Objekte nicht nur durch Literale (Abschnitt 1.2) und Variablen (Abschnitt 1.5) reprasentiert werden, sondern auch durch **Ausdrucke**. Tatsachlich sind Literale und Variablen _primitive Ausdrucke_, also solche, die nicht aus anderen zusammengesetzt sind. Damit mit den Objekten aber etwas geschehen und ein Programm somit etwas tun kann, brauchen wir noch andere Ausdrucke, namentlich _Zuweisungsausdrucke_ und _Nachrichtenausdrucke_. Auch sie stehen jeweils für ein Objekt und können deswegen überall da auftreten, wo Objekte verlangt werden. Sie können insbesondere auch geschachtelt werden.

#### **Zuweisungsausdrucke**

Zuweisungsausdrucke hatten Sie schon in Abschnitt 1.6 kennengelernt. Sie verlangen auf der linken Seite eine Variable und auf der rechten einen Ausdruck:

```
36x=1
```
46etwaistein Zuweisungsausdruck. Wie bereits erwahnt, bewirken Zuweisungen als einzige Ausdrucke den Zustandswechsel von Objekten. So bewirkt etwa
57name:='Hanschen' wobei name eine Instanzvariable sein soll, die Anderung des Zustandes des Objektes, zu dem die Instanzvariable gehort. Da eine Zuweisung selbst ein Ausdruck ist, kann sie auf der rechten Seite einer anderen Zuweisung erscheinen:
38y:=x:=1 ```

ist also ein legaler Ausdruck (zu seiner Auswertung kommen wir spater, wenn wir -- in Abschnitt 4.1.4 -- über die Reihenfolge der Auswertung geschachtelter Ausdrucke sprechen).

#### **Nachrichtenausdrucke**

Neben der Zuweisung ist der **Nachrichtenversand** die zweite wichtige **Ausdrucksform** der objektorientierten Programmierung. SMALTLK verwendet hierfur eine Syntax, die stark an die der englischen Sprache angelehnt ist: Sie verlangt ein Subjekt (den Empfanger der Nachricht), ein Pradikat (die **Nachricht**) sowie eine optionale Liste von Objekten als Pradikatserganzungen (die Parameter der Nachricht). Dabei wird auf die in anderen Sprachen ubliche Verwendung des Punkts als Trennzeichen zwischen Empfanger und Nachricht und Klammern zum Umschliessen der Parameterliste verzichtet; stattdessen verwendet man beiZwei oder mehr Parametern Partikeln (Prapositionen oder Konjunktionen) ahnelnde Nachrichtenteile, die den Parametern vorangestellt werden. Die allgemeine Syntax lautet also
39<Empfanger><Nachricht> für parameterlose Nachrichten,
40<Empfanger><Nachricht><Parameters> furNachrichten mit einem Parameter,
41<Empfanger> <NachrichtTeil1><Parameter1> <NachrichtTeil2><Parameter2> furNachrichten mit zwei Parametern usw., wobei hier die in spitzen Klammern stehenden Namen _metasyntaktische Variablen_, also Platzhalter für Namen in einem konkreten Programm, sind und die Nachrichten(teile), die Parameter nach sich ziehen, immer mit einem Doppelpunkt enden mussen.
44einObjekt tueEtwas druckt beispielsweise den Versand einer parameterlosen Nachricht tueEtwas an das Objekt, auf das die Variable einObjekt verweist, aus.16 Ein etwas konkreteres Beispiel hierfur ist der Ausdruck
45#abc printString mit dem Objekt #abc die Nachricht printString gesendet wird. Soll einer Nachricht ein Parameter angehangt werden, so tut das
46einObjekt tueEtwasMit: einemParameter wobei einemParameter hier auch eine Variable ist (es konnte auch ein anderer Ausdruck dort stehen; s. u.). Ein konkretes Beispiel hierfur ist
47Transcript show:'Hallo' Ein zweiter Parameter wird durch einen weiteren Nachrichtentbestandteil wie in
48einObjekt tueEtwasMit: einemParameter und: zweitenParameter hinzugefugt und alle weiteren entsprechend, also etwa* [49] ein Objekt
* [50] tueEtwasMit: einemParameter
* [51] und: zweitemParameter
* [52] und: drittem Parameter

wobei sich die Nachrichtenteile wie oben ruhig wiederholen durfen. Es ist

**Nachrichtenselektor**

also insbesondere nicht so, dass die Reihenfolge der Nachrichtenteile beliebig umgestellt werden durfte, ohne dass sich dadurch die Bedeutung der Nachricht anderte. Tatsachlich ist die an das Objekt geschickte Nachricht, der sog. **Nachrichtenselektor** (engl. message selector), immer ein Symbol, das aus der Konkatenation (Aneinanderfugung) aller seiner Teile, also im Beispiel der Zeile 48 oben #tueEtwasMit:und:besteht. Die Namen der Nachrichtenteile sind frei wahlbar, beginnen jedoch per Konvention mit einem Kleinbuchstaben.

Parameterlose Nachrichten wie beispielsweise tueEtwas in Zeile 44

**unare und binare**

nennt man in Smalltalk ubrigens **unar** (unary messages): Obwohl sie

**Nachrichten**

keine expliziten Argumente haben, heissen sie trotzdem unar, weil der Empfanger das erste,

implizite Argument ist. So nehmen denn auch sog. **binare Nachrichten17** nur einen Parameter, was aber zwei Argumenten, namlich dem Empfanger und einem weiteren Argument, entspricht:

Footnote 17: nicht zu verwechseln mit den sog. _binaren Methoden_, bei denen Empfanger und Parameter den gleichen Typ haben

```
18Nur in Ausnahmefallen ist es sinnvoll, das Empfangerobjekt mit einer Nachricht als (zusatzlichen) Parameter zu übergeben; in den allermeistent Fallen handelt es sich dabei um einen Anfangerinnensteht für ein Objekt, namlich das Ergebnis der Auswertung der Nachricht durch den Empfanger. Der Nachrichtensender wird dem Empfanger überignes nicht mitgeteilt (es sei denn, er wird explizit als Parameter übergeben) -- das System weiss automatisch, wohin die Antwort auf die Nachricht zuruckgleiefert werden soll (namlich genau an die Stelle, an der der Nachrichtenversand steht). Mehr dazu gleich, wenn es um die Auswertung von Nachrichtenausdrucken geht (Abschnitt 4.1.3). Da ein Nachrichtenausdruck für ein Objekt steht, kann er selbst Teil eines **geschachtelte Nachrichtenausdrucks sein, also für den Empfanger der Nachricht oder **richtenausdrucke** einen ihrer Parameter stehen. Es ist dann allerdings u. U. notwendig, den so geschachtelten **Nachrichtenausdruck zu klammen, da er sonst nicht richtig erkannt werden kann:**

```
54aStackpush:((aStackpop)
56arg:(aStackpop)
57arg:(aStackpop))
```

beispielsweise schiebt das Objekt auf den Stack, das Resultat der Nachricht arg:arg:gesandt an das oberste Objekt des Stacks mit seinem zweiten und dritten als Parameter ist. (Zu den genauen Regeln zur Reihenfolge der Auswertungen siehe Abschnitt 4.1.4.)

Nicht selten mochte man eine Serie von Ausdrucken an dasselbe Empfangerobjekt senden. Smalltalk sieht dafur mit der Kaskadierung eine nette **ausdrucke** syntaktische Abkurzung vor, die es erlaubt, bei einer Sequenz von Nachrichten an dasselbe Objekt dieses nicht immer wiederholen z mussen. So sorgt beispielsweise

```
8Transcriptshow:1',show:#+,show:'2',cr.

anstelle des wesentlich wortreicheren
```
59Transcriptshow:1',
60Transcriptshow:#+.
61Transcriptshow:'2'.
62Transcriptcr ```
dafur, dass die Objekte_1",_+" und_2" nacheinander als Parameter der Nachricht show: an das von der globalen Variable Transcript benannte Objekt, eine Art Systemkonsole, gesendet werden. (Auf die Bedeutung des "." kommen wir in Kapitel 4.2 zu sprechen.) Das Beispiel ist ubrigens nicht besonders zwingend, da man in Smalltalk genauso gut auch hatte
```
63Transcriptshow:1',#+,'2',cr ```

fehler, bei dem durchcheint, dass die Programmiererin (die vermutlich noch in Kategorien der prozzeduralen Programmierung denkt) nicht verstanden hat, dass jede Nachricht einen Empfanger hat, ein Nachrichtenausdruck diesen also schon beinhaltet.

schreiben können (wobei, ein binarer Nachrichtenselektor ist, der für die Konkatenation steht). **cr** ist ubrigens eine (unare) Nachricht, die für einen Wagenrucklauf (carriage return) auf dem Transcript sorgt.

Man kann sich aber durch Verwendung der Kaskadierung haufig die Einfuhrung einer temporaren Variablen (s. Abschnitt 4.3) ersparen, und zwar immer dann, wenn anstelle einer Variable als Empfanger (Transcript in obigem Beispiel) ein Ausdruck steht, der das Empfangerobjekt liefert und der nur einmal ausgewertet werden soll. Anstelle von

```
64eineVariable:=<iregendein Ausdruck>.
65eineVariable<eineNachricht>.
66eineVariable<nocheineNachricht>
```

kann man also

```
67sigrendeinAusdruck><eineNachricht>:<nocheineNachricht>
```

schreiben, wenn man eineVariable hernach nicht mehr benotigt. Smalltalk unterstutzt also von Haus aus sog. _Fluent APIs_.

Wikipedia

#### Auswertung von Ausdrucken

Ausdrucke allein sind nur syntaktische Figuren -- um das Objekt zu liefern, für das sie stehen, mussen sie ausgewertet werden. Es ist die Auswertung, bei der ein Programm tatsachlich,,etwas tut".

Das Elementarste, das ein Programm tun kann, ist die Auswertung einer Zuweisung wie beispielsweise y := x. Diese Auswertung fuhrt dazu, dass die Variable y nach der Zuweisung auf dasselbe Objekt verweist wie vorher schon x. Dabei steht der gesamte Ausdruck y := x für (eine Referenz auf) das Objekt, auf das x (und nach seiner Auswertung auch y) verweist. Die Zuweisung dieses Objektes an y ist gewissermassen nur ein Seiteneffekt der Auswertung des Ausdrucks.19

Footnote 19: Über das Wort Seiteneffekt wird viel gestritten. Manche meinen, es müsste Nebeneffekt heißen, aber dieses Wort ist genaus unnötig, wenn Nebenwirkung das ist, was gemeint ist. Als stitting würde ich schon eher ansehen, ob man hier überhaupt von einer Nebenwirkung sprechen sollte, denn der sich einstellende Effekt ist ja das vornehmliche Ziel einer Zuweisung, so dass man eher von Wirkung (oder Effekt) sprechen sollte. für mich ist Seiteneffekt Jargon, bei dem jede weiss, was gemeint ist.

Man beachte, dass es sich beim Zuweisungsoperator := nicht um einen (binaren) Nachrichtenselektor handelt: Es wird hier namlich keine Nachricht an ein Objekt geschickt, sondern der Inhalt einer Variable manipuliert. Die Zuweisung ist tatsachlich eines der wenigen Primitive Smalltalk, also eine der Operationen, die nicht in sich selbst programmiert, sondern fest,,verdrahteter" Teil der Sprache sind (vgl. Abschnitt 1.6).

Nachrichtenausdrucke werden ausgewertet, in dem die Nachricht (das Pradikat des Satzes) an das Empfangerobjekt (das Subjekt) mit den Parametern (den Pradikatserganzungen) gesendet wird und das Empfangerobjekt als Ergebnis der Nachricht ein Objekt zuruckliefert. Wie das Empfangerobjekt das Ergebnisobjekt bestimmt, darauf kommen wir noch; hier ist nur wichtig, dass der Nachrichtenausdruck im Zuge der Auswertung gewissermassen durch das Objekt, für das er steht, ersetzt wird. Man kann sich das genauso vorstellen wie die Auswertung einer (mathematischen) Funktion f, deren Funktionsanwendung f(x) auf ein Objekt x ebenfalls für den Funktionswert steht.

Eine haufig gebrauchte, von allen Objekten verstandene unare Nachricht **Beispiele** ist **printString**, in Reaktion auf die das Empfangerobjekt eine textuelle Repräsentation von sich zuruckgibt:

```
6812printString
```

liefert den String '12', die Auswertung von Zeile 45 den String 'abc'. Der bereits in Zeile 53 angefuhrte binare Nachrichtenausdruck ```
6911+2
```

liefert wie erhofft das Objekt _3". Bei der Auswertung des Schlosselwortausdrucks

7012printOn:Transcript ```

bei dem als Seiteneffekt die Zahl _12" in ihrer textuellen Repräsentation, also als String '12' auf dem Ausgabestrom, auf den die Variable Transcript verweist, ausgegeben wird, wird das Empfangerobjekt _12" zuruckgeliefert.

Es ist in Smalltalk, anders als z. B. bei als void deklarierten Methoden in Java oder C#, nicht moglich, in Reaktion auf einen Nachrichtnervsand nicht s Zuruckzugegeben. Dies konnte man in Zeile 70 als sinnvoll erachten, da man hier eigentlich nur an dem _(Seiten-) Effekt_, der Ausgabe von _12" auf dem Transcript, interessiert ist. Wenn die zu einer Nachricht gehrende Methode keinen sinnvollen Ruckgabewert hat, wird _standardmagg immer das Empfangerobjekt zuruckgegeben_; auch das dient, da man Nachrichtenausdrucke so stets verketten kann, einem Fluent API_. Soltte es für das Ruckgabeobjekt im Kontext der Nachricht (des Nachrichtnervsands) keine Verwendung geben, es also nicht einer Variable zugeweiseen oder sonst wie Teil eines anderen Ausdrucks sein, verfallt es einfach. Da der Ruckgabewert aber technisch nur eine Referenz auf das Objekt ist, bleibt die Existenz des Objektes davon zunächst unberruhrt. Nur wenn es sonst keine anderen Referenzen auf das Objekt gibt, etwa weil es extra für die Ruckgabe erzeugt wurde, wird das Objekt bei der nachsten Speicherbereinigung entfernt.

Da die Auswertung eines Nachrichtenausdrucks zur Abarbeitung der Anweisungen des Rumpfs einer Methode fuhrt, nennt man ihn auch _Methodenauftr_uf. Warum diese Bezeichnung legitim ist, wird jedoch erst in Abschnitt 4.3 klar. Zusammenfassend wird also Zusammenfassung

\begin{tabular}{c c}  & Zusammenfassung \\ \end{tabular}

\begin{tabular}{c c}  & ein Literal zu dem Objekt ausgewertet, das es reprasentiert, \\  & eine Variable zu dem Objekt, das sie benennt, \\  & eine Zuweisung zu dem Objekt, zu dem der Ausdruck auf der rechten Seite der Zuweisung ausgewertet wird, \\  & ein Nachrichtenausdruck zu dem Objekt, das als Antwort auf die Nachricht zuruckgegeben wird, sowie \\  & ein kaskadierter Nachrichtenausdruck zu dem Objekt, zu dem sein letzter Nachrichtenausdruck ausgewertet wird. \\ \end{tabular}

#### 4.1.4 Reihenfolge der Auswertung von geschachtelten Ausdrucken

Da Ausdrucke andere Ausdrucke enthalten können, stellt sich die Frage nach der Reihenfolge der Auswertung von geschachtelten Ausdrucken. Diese wird, wie in anderen Sprachen auch, implizit über Prazedenzen und explizit über Klammerm geregelt.

Bei der doppelten Zuweisung in Zeile 38 oben ist zunächst vielleicht nicht klar, welche der beiden Zuweisungen zuerst ausgewertet (ausgewertet (ausgefuhrt) werden soll: **y** := **x** oder **x** := 1. Wenn man jedoch weiss, dass es sich bei **y** := **x** := 1 um einen geschachtelten Ausdruck handelt und jeder (Teil-)Ausdruck für ein Objekt steht, dann muss der zweite Ausdruck zuerst ausgewertet und durch das Ergebnis, _1", esetzt werden, denn andernfalls ware die _1" dem Ergebnis von **y** := **x** zuzuweisen, was aber nach Abschnitt 4.1.3 keine Variable, sondem ein Objekt ist. Zeile 38 weist also zuerst **x** und dann **y** das Objekt _,1" zu -- die Auswertung erfolgt von rechts nach links.

\begin{tabular}{c c}  & Das ist allerdings ein Sonderfall. Grundsatzlich werden in \begin{tabular}{c}  \\ \end{tabular} & \begin{tabular}{c}  \\ \end{tabular} & \begin{tabular}{c}  \\ \end{tabular} & \begin{tabular}{c}  \\ \end{tabular} & 
\begin{tabular}{c}  \\ \end{tabular} \\ \end{tabular}

\begin{tabular}{c c}  & **Auswertung von** \\  & **links nach rechts** \\  & **links nach rechts** \\  & **dings unare Ausdrucke Vorrang vor binaren und diese wiederum Vorrang vor Schlusselwortnachrichten, so dass nur bei gleichrangigen Ausdrucken die Auswertung von links nach rechts erfolgt. So wird beispielsweise in** \\
71\(\mathbf{x+1<y}\) & zunächst die Nachricht _,+" an das Objekt, auf das **x** verweist, mit Argument 1 geschickt \\  & und an das Ergebnis die Nachricht _,<" mit **y** **als Parameter. Umgekehrt wird bei \\
72\(\mathbf{x<y-1}\) & \\  & **d

[MISSING_PAGE_FAIL:59]

Die einzige andere Form der Anweisung in Smalltalk ist die **Return-Anweisung**. Auf sie werden wir im Zusammenhang mit Methoden im nachsten Kapitel noch ausführlicher zu sprechen kommen. Sie besteht in Smalltalk aus dem Sonderzeichen 1 (ursprunglich \(\uparrow\), jedoch genau wie \(\leftarrow\) auf den meisten Tastaturen nicht verfugbar), gefolgt von einem Ausdruck. Die Return-Anweisung,,retourniert" das Objekt, zu dem dieser Ausdruck auswertet.

Footnote 11: Der im Englischen gebrauchte Term,,actual parameter" wird auch manchmal mit,,_aktuelfer Parameter_" ins Deutsche übersetzt, was oft als falsch verfohnt wird, aber die Sache trotzdem trifft, zumindest, wenn man die zeitliche Dimension, die mit der Programmausfuhrung einhergeht, in Betracht zieht: Es gibt namlich in der Regel viele tatsächliche Parameter zu einem Methodenaufruf, von denen -- zu jedem Zeitpunkt -- höchstens einer der Aktuelle ist.

Da alle anderen Anweisungen Ausdrucke sind, die zu einem Objekt auswerten, brauchen Methoden (Abschnitt 4.3) und Blocke (Abschnitt 4.4) in Smalltalk keine Return-Anweisungen, um ein Objekt zurückzuliefern; sie liefern dann das Objekt, zu dem die letzte Anweisung auswertet.

### Methoden

Die Auswertung von Nachrichtenausdrucken, also von Nachrichten, die an Objekte verschickt werden, erfolgt mit Hilfe sog. **Methoden**. Was ein Objekt in Reaktion auf den Erhalt einer entsprechenden Nachricht tun soll, wird durch eine **Methodendefinition** beschreiben. Eine Methodendefinition besteht dazu aus einem _Methodenkopf_, der in Smalltalk auch als _Message pattern_, allgemein (und im folgenden) aber eher als **Methodensignatur** bezeichnet wird, einer optionalen Liste von _lokalen Variablen_ und einem _Methodenrumpf_. Letzterer enthalt die _Anweisungen_, die die Methode ausmachen, die also zur Auswertung eines Nachrichtenausdrucks ausgefuhrt werden. Es ist ublich, jede Methodendefinition mit einem in doppelte Anfuhrungsstriche gesetzten Kommentar zu versehen, der beschreibt, was diese Methode macht.

Die Methodensignatur besteht aus dem Namen der Methode und der Liste ihrer **formalen Parameter**. Formale Parameter sind _lokale Variablen_, denen beim Aufruf der Methode (s. Abschnitt 4.3.2) automatisch ein Wert, der sog. **tatsachliche Parameter**20, zugewiesen wird und deren Sichtbarkeit auf die Methode, in deren Methodensignatur sie vorkommen, beschrankt ist. Wie alle lokalen Variablen mussen sie mit einem Kleinbuchstaben beginnen. Außerdem sind sie _temporare Variablen_, was soviel heißt wie dass sie nur für die Dauer der Ausfuhrung der Methode exsiteren. Damit sind auch die Aliase, die durch formale Parameter gebildet werden können, immer temporar. In Smalltalk sind formale Parameter zudem _Pseudovariablen_ (s. Abschnitt 1.7), d. h., es kann ihnen innerhalb der Methode, für die sie sichtbar sind, nichts zugewiesen werden. Syntaktisch unterscheidet sich Smalltalk von den meisten anderen Programmiersprachen auch bei der Methodendefinition dadurch, dass die formalen Parameter nichtdurch Kommata getrennt in einer in Klammern eingeschlossenen Liste hinter dem Methodennamen stehen, sondern jeder für sich von einem Nachrichtenbestandteil eingeleitet wird.

Eine Methodedefinition folgt also dem Schema

**Methodendefinition**

*Kommentary\({}^{*}\)

\(|\)\(<\)Liste lokaler Variablen> \(|\)

\(<\)Folge von Anweisungen>

(in spitzen Klammern wieder _metasyntaktische Variablen_, also Platzhalter für entsprechende Programmelemente). Eine einfache Methode ware etwa

**helloWorld**

*das beruhnt-beruchtigte\({}^{*}\)

Transcript show: 'Hello World!': cr

oder, wer es generischer mag,

**sag: einenText**

*nicht so unflexibel\({}^{*}\)

\(|\)

Transcript show: einenText; cr

Die Methodensignatur als Teil einer Methodedefinition wird im folgenden immer fett hervorgehoben.

Die Methodensignatur dient der Auswahl der zu einer Nachricht passenden Methode; sie ist das Gegenstuck zum _Nachrichtenselektor_ Aus Abschnitt 4.1.2, anhand dessen die Auswahl der zu einem Nachrichtenausdruck passenden Methode durchgefuhrt wird. Anders als ein Nachrichtenausdruck nennt eine Methodensignatur aber kein Empfangerobjekt und die offenen Stellen eines Nachrichtenselektors werden ausschliesslich durch Variablen, eben die _formalen Parameter_, und nicht durch beliebige Ausdrucke besetzt. Typische Methodensignaturen sind z. B.

**printString**

fur Methoden ohne Parameter,

**einInteger**

fur binare Methoden\({}^{2}\)1 (mit einInteger als formalem Parameter) und* 94printOn: einStrom  für alle anderen Methoden mit einem oder mehreren Parametern (in diesem Fall mit nur einem formalen Parameter, einStrom). Die Methodensignaturen,,passen" ubrigens jeweils zu den entsprechenden Nachrichtenausdrucken aus den Zeilen 68, 69 und 70. Wenn der Nachrichtenselektor aus mehreren Teilen besteht, werden diese (entsprechend den Beispielen in den Zeilen 48 ff.) einfach angehangt.  Wie bereits erwahnt, besteht der Methodenrumpf aus einer Folge von Anweisungen, Ausdrucken, die jeweils durch einen Punkt getrennt sind.  Wenn die Anweisungen nichts anderes vorsehen, wird die Ausfuhrung  einer Methode nach Abarbeitung der letzten Anweisung explizit mit der Ruckgabe des Empfangerobjekts an den Sender der Nachricht beendet. für explizite Beendigungen und Ruckgabe eines anderen Objekts als des Empfangers ist die _Return-Anweisung_ (Abschnitt 4.2) vorgesehen.
* 95hellWorld 96Transcript show: 'Hello World!'; cr 97A'Hello World!' Eine Return-Anweisung darf an beliebigen Stellen innerhalb der Methode **explizite Beendigung** auftreten. Die Abarbeitung der Methode kann demnach auch vor Errei- **einer Methode**hen der textuell letzten Anweisung beendet werden. Die Return-Anweisung beeinflusst also den _Kontrollfluss_ des Programms. Wichtig ist, dass eine Methode immer ein Objekt zuruckgibt; ein Nachrichtenausdruck (oder _Methodenauftruf_; s Abschnitt 4.3.2) steht als Ausdruck also immer für ein Objekt. Prozeduren im Sinne Pascals oder Void-Methoden im Sinne von C, Java usw. gibt es in smalltalk nicht (vgl. a. Abschnitt 4.1.3).
* 98Solte eine Methode zur Durchfuhrung ihrer Berechnungen _temporare_ **temporare Variablen**_Variablen_ benotigen, so mussen diese zu Beginn der Methode (nach der Methodensignatur und vor der ersten Anweisung) deklariert werden. Die Werte dieser Variablen, die standard- **massig mit nil initialisiert werden, sind aüberhalb der Methode nicht sichtbar; die Variablen werden insbesondere nach Abarbeitung der Methode vom System wieder entfernt. Sie können sich also auch zwischen zwei Ausfuhrungen einer Methode nichts merken.
* 99hellWorldX2 99| einmal zweimal | 100einmal := 'Hello World!'.
* 101zweimal := einmal, einmal.
* 102Transcript show: zweimal; cr
* 103Umgekehrt können temporare Variablen, die nur einmal verwendet werden, eingespart werden, indem man kaskadierte Nachrichtenausdrucke (Abschnitt 4.1.2) verwendet.

Methoden sind die Einheiten des Programms, in denen Sie als Programmierrin Ihre Anweisungen unterbringen. Sie werden nach der Eingabe (und bei jeder Anderung) mit dem,,Speichem" kompliiert (,,Speichern" deswegen in Antifuhrungsstrichen, weil Methoden nicht in Dateien gespeichert werden, sondern in einer Datenstruktur smalltalks, und zwar in Form von Objekten). Tatsachlich besteht der Lowenantel eines jeden Smalltalk-Programms, ja des gesamten Smalltalk-Systems, aus Methodendefinitionen. Die Methodendefinitionen entsprechen im wesentlichen der Definition von Funktionen (oder, mit obiger Einschrankung, Prozeduren) in anderen Sprachen; jedoch ist es in Smalltalk nicht moglich (und in der objektorientierten Programmierung allgemein nicht ublich), Methoden zu schachteln, also eine Methode innerhalb einer anderen zu defuzieren. Ausserdem gibt es in Smalltalk keine,,Haptmethode" wie etwa die Main-Methoden in der C-Sprachfamilie. Sie mussen dem Smalltalk-System schon sagen, welche Methode Sie ausgefuhrt haben wollen, z. B. indem Sie einenentsprechenden Ausdruck eingeben und auswerten lassen.

#### 4.3.1 _Zuordnung von Methoden zu Objekten_

Methoden sind immer Objekten, den sogenannten Emfangerobjekten, zugeordnet. Wir wollen uns in dieser Kurseinheit noch nicht darauf festlegen, wie diese Zuordnung erfolgt; Sie durfen jedoch davon ausgehen, dass jedes Objekt über einen Katalog von Methoden verfugt und damit auf die entsprechenden Nachrichten reagieren kann. Diesen Katalog nennt man auch das **Protokoll** eines Objekts (s. Abschnitt 4.3.8).

Die Zuordnung von Methoden zu Objekten erlaubt, dass die Methoden **Zugriff auf die Instanzvariablen des jeweiligen Objekts zugreifen können. Da der **Instanzvariablen** Zustand eines Objekts durch die Belegung seiner Instanzvariablen reprasentiert wird (s. Kapitel 3) und weil in den Methoden das Verhalten eines Objektes spezifiziert ist, ergibt sich, dass das Verhalten vom Zustand des Objekts abhangen (durch Berucksichtigung seiner Instanzvariablen) und es ihn gleichzeitig beeinflussen (durch Zuweisungen an die Instanzvariablen) kann. Da Instanzvariablen lokale Variablen sind (lokal zum besitzenden Objekt), sind Methoden sogar die einzige Stelle, an der der Zustand von Objekten geandert werden kann. Mehr dazu in Abschnitt 4.3.4.

Neben den _formalen Parametern_ der Methode und den Instanzvariablen **die Pseudovariable** des Emfangerobjekts ist im Rumpf jeder Methode eine weitere Variable **self** zugreifbar, die den Namen,,**Self**" tragt. Diese Variable, die wie die formalen Parameter eine _Pseudovariable_ ist, verweist immer auf das Emfangerobjekt der Nachricht, also auf das Objekt, dessen Instanzvariablen gerade zugereifbar sind. Sie wird immer dann benotigt, wenn eine Nachricht aus einer Methode heraus (also per darin enthaltener Anweisung) an das Objekt geschickt werden soll, dem die Methode zugeordnet ist, also an sich selbst. **self** ist also gewissermassen der implizite erste Parameter einer Methode.

#### Methodenaufruf und dynamisches Binden

Wenn das Versenden von Nachrichten bislang als die übergabe eines entsprechenden Nachrichtenobjekts an den Empfanger dargestellt wurde, so ist das nicht ganz richtig: Vielmehr wird ein Nachrichtenausdruck auch in SMALLtalk aus EffizienzGründen vom Compiler in einen schnoden **Methodenaufruf** übersetzt, der mit dem Funktionsaufruf aus der prozenduralen Programmierung (also z. B. PASCAL oder C) vergleichbar ist. So fuhrt beispielsweise der Ausdruck

1031422

zum Aufruf der Methode +, wie sie für das Objekt _,1" (und alle Zahlen) definiert wurde. Dennoch wird, wohl aus didaktischen Gründen, das Mysterium vom Nachrichtenversand in der objektorientierten Literatur weiter gepflegt. Es gibt aber auch einen kleinen, feinen Unterschied zum gewohnlichen Prozeduraufruf.

Die Entscheidung, welche Methode in Reaktion auf einen Nachrichtenversand aufgerufen und abgearbeitet wird, hangt nicht von dem Nachrichtenselektor allein ab, sondern auch von dem Objekt, an das die Nachricht geschickt wird. Es ist namlich durchaus ublich, dass verschiedene Objekte mit gleichen Methodensignaturen unterschiedliche Methodenimplementierungen verbinden; so implementieren beispielsweise Zahlen und Symbole die Methode printString jeweils anders und selbst

10411.042

fuhrt zum Aufruf einer anderen Methode als 1 + 2,

1051+2.0

dagegen nicht.

Aus der Abhangigkeit des Methodenaufrufs vom Empfangerobjekt folgt,

dans nicht immer schon zur übersetzungszeit entschieden werden kann, welche Methodenimplementierung bei einem Methodenaufruf ausgewahlt werden muss. Wenn namlich das Empfangerobjekt durch eine Variable benannt oder von einem Ausdruck geliefert wird, kann die Zuordnung einer Methodedefinition zu einem Nachrichtenausdruck erst zum Zeitpunkt der Auswertung des Nachrichtenausdrucks und damit erst zur Laufzeit erfolgen. Man nennt diesen Vorgang **dynamisches Binden** (im Gegensatz zum **statischen Binden**, bei dem ein Aufruf schon zur übersetzungszeit an eine Implementierung gebunden wird); es handelt sich dabei um eine von den nur zwei _primitiven Kontrolstrukturen_ SMALLtalkS (s. Abschnitt 4.5.2).

Das dynamische Binden ist eine der charakteristischen Eigenschaften der

objektorientierten Programmierung. Sie wird auch als **Polymorphismus**

**zentrale Bedeutung des dynamischen Bindens**oder **Polymorphie22** bezeichnet. Auf die Details des dynamischen Bindens können wir erst in der nachsten Kurseinheit (Kapitel 12) zu sprechen kommen und auf Polymorphie erst in Kapitel 26, da uns hier noch zu viel fehlt. Wir vermerken aber schon jetzt, dass es sich dabei um eine _versteckte Fallunterscheidung_ handelt: Ein und derselbe Methodenaufruft kann fallweise unterschiedliche Methoden aufrufen (bzw. deren Ausfuhrung veranlassen). Auf diese Eigenschaft kommen wir schon in den Abschnitten 4.5 und 4.6 zuruck.

Steht einmal fest, welche (Implementierung einer) Methode aufgerufen wird, erfolgt als nachstes die Versorgung der formalen Parameter mit Objekten. Zu diesem Zweck findet mit dem Aufruft eine **implizite Zuweisung** (also eine ohne Vorkommen des Zuweisungsoperators im Programmtext) der _tatsachlichen Parameter_ des Aufrufs an die formalen Parameter der Methode statt. Tatsachliche Parameter sind dabei die Objekte, die an der Methodenaufruftstelle als Argumente an den Positionen der formalen Parameter der aufgerufenen Methode stehen. Manchmal werden auch die Variablen, die an den entsprechenden Stellen beim Methodenaufruft stehen, als tatsachliche Parameter bezeichnet, aber erstens mussen dort nicht unbedingt Variablen, sondern können beliebige Ausdrucke stehen und zweitens können diese Variablen selbst formale Parameter sein, namlich die der Methode, die den Methodenaufruft enthalt. So ist in der Methodedefinition

106m:a

107selfn:a

a der formale Parameter von m: Der tatsachliche Parameter von m: ist ein Objekt, das beim Aufruf von m: genannt wird (hier nicht zu sehen). Dieses Objekt ist dann auch tatsachlicher Parameter des Aufrufs von n:, da dieser von a, dem formalen Parameter von m:, geliefert wird.

Je nach Sichtweise erfolgt bei Ausfuhrung der Return-Anweisung eine weitere implizite Zuweisung, namlich die des Objekts, zu dem der Ausdruck der Return-Anweisung auswertet, an die,,Variable" Methodenname (der ja an der Stelle des Methodenaufrufs ahnlich wie eine Variable für ein Objekt steht). Dies ist vor allem im Zusammenhang mit der Typprufung, die es jedoch in Smalltalk nicht gibt (s. Kurseinheit 3), eine wichtige Vorstellung. An der Aufruftstelle selbst steht dann haufig noch eine _explizite Zuweisung_, namlich wenn das Ergebnis des Aufrufs (das Ruckgabeobjekt) einer Variable zugewiesen werden soll.

Selbsttesteaufgabe4.1

Benennen Sie die expliziten und impliziten Zuweisungen für 

[MISSING_PAGE_FAIL:67]

#### 4.3.4 Verbergen der Repräsentation des Zustands hinter Methoden

In SMALLTAK sind die Instanzvariablen eines Objekts nur für das Objekt selbst sichtbar (und damit auch zugeifbbar).23 Genauer sind seine Methoden die einzigen Stellen im ganzen Programm, an denen auf die Instanzvariablen des Objekts, dem die Methoden zugeordnet sind, direkt zugegriffen werden kann. Die Struktur des Objekts bleibt somit verborgen (das _Implementationsgeheimnis_) und sein _Zustand_ wird gekapselt_ (s. Abschnitt 3.2 sowie unten für ein praktisches Beispiel).

Um die Belegung der Instanzvariablen und damit den Zustand eines Objektes auszulesen oder verändern zu können, sind also Methoden notwendig. Um beispielsweise den Wert einer Instanzvariable mit Namen **a** auszulesen, muss das Objekt eine Methode vorsehen, die den Wert von **a** zuruckgibt. Diese (parameterlose) Methode wird in SMALLTAK ublicherweise wie folgt notiert:

Footnote 23: Dass dies in anderen Sprachen anders ist (z. B. in JAVA), kann man durchaus als Entwurfstehler ansheen. Auf der anderen Seite schützt die mangelnde Sichtbarkeit von Instanzvariablen ja nicht vor dem Zugriff auf Objekte, auf die sie verweisen (wegen des möglichen _Aliasing_), so dass man sich an dieser Stelle nicht versteigen sollte.

Sie entspricht im wesentlichem einem auch in Java gebrauchlichen sog. **Getter** einer ansonsten nicht zugeifbaren Variable. Die Namensgleichheit von Methode und Variable soll dabei nicht darüber hinwegtauschen, dass es sich bei beiden um verschiedene Dinge handelt -- Methode und Variable konnten genauso gut verschieden benannt werden.

Um den Wert von **a** zu setzen, definiert man ublicherweise die folgende, auch **Setter** genannte Methode:

```
117a:einWert
118"setzedenWertvonaufeinWert"
119a:=einWert
```

Getter und Setter werden zusammen auch als **Zugriffsmethoden** (oder **Accessoren**; engl. accessor methods) bezeichnet.

Die obigen Zugriffsmethoden werden aufgerufen, indem man dem Objekt, zu dem die Instanzvariable **a** gebort, die Nachricht **a** (zum Lesen) bzw. **a:** mit einem Objekt als Parameter (zum Schreiben) schickt. Das Empfangerobjekt anwortet darauf im ersten Fall mit Ruckgabe von **a** und im zweiten Fall mit Ruckgabe von sich selbst. Man beachte, dass bei der Ruckgabe keine Kopie, sondern der Inhalt der Variable (bzw. ein Verweis darauf) zuruckgegeben wird. Nach Auswertung des Ausdrucks* 120b:=einObjekt a verweisen also b und die Instanzvariable a von einObjekt (genauer: dem von einObjekt bezeichneten Objekt) auf dasselbe Objekt, genauso wie nach Auswertung von
* 121einObjekt a:b

Bei beiden ist hinterher b ein Alias auf a, was de facto die Kapselung des Zustandes von einObjekt durchbricht.

Es solnochmals darauf hingewiesen werden, dass im ersten Ausdruck a eine Nachricht darstellt und keinesfalls der Name der Instanzvariable des Objekts ist. Insbesondere handelt es sich bei dem (Teil-)Ausdruck einObjekt a mitrichten um das Aquivalent zu dem aus java bekannten einObjekt.a, sondern vielmehr dem von einObjekt.getA() (wobei man die Methode getA() in Java per Konvention naturlich genauso gut nur a() nennen konnte). Ein direkter Zugriff auf die Instanzvariable von aussen wie in Java ist in SMALLtalk nicht moglich. Man kann also den Zugriff auf eine Instanzvariable verhindern, indem man einfach keine Zugriffsmethoden dafur vorsieht; man kann ih auf _Nur-Lesen_ oder _Nur-Schreiben_ beschranken, indem man nur die jeweilige Zugriffsmethode zur Verfugung stellt.

Man beachte schliesslich, dass anders als benannte Instanzvariablen indizierte Instanzvariablen auch von dem Objekt, zu dem sie gehoren, nicht direkt, sondern nur über die beiden vordefinierten Nachrichten at: und at:put:gelesen und geschrieben werden können:

* 122einObjekt at:1

liefert den Wert der Instanzvariable mit dem Index 1,
* 123einObjekt at:1 put:einAnderesObjekt

setzt ihn. Es ist in SMalltalk also nicht moglich, indizierte Instanzvariablen eines Objekts (im Gegensatz zu benannten) durch Nicht-Dekaration von Zugriffsmethoden zu verbergen (vor Zugriff zu schutzen). Zugleich folgt aus der festen Vorgabe der beiden Zugriffsmethoden, dass jedes Objekt nur genau eine (unbenannte) Menge von indizierten Instanzvariablen haben kann.

Die ausschliessliche Abfrage und Anderung des Zustandes von Objekten über Methoden hat den Vorteil, dass man sich nicht festlegt, wie man den Zustand eines Objekts tatsachlich codiert. So kann man beispielsweise einem Punktobjekt Methoden zum Setzen und Abfragen sowohl von kartesischen als auch von polaren Koordinaten zuordnen, muss aber nur Instanzvariablen für eine Art von Koordinaten vorsehen und kann die anderen jeweils berechnen:

* 124kartesischX:a y:b
* 125setzt kartesische Werte*
* 126x:=a.
* 127y:=b128x
129"liefert die x-Koordinate"
130"x
131y
132"liefert die y-Koordinate"
133"y
134polarRadius: r winkel: a
135"setzt polare Werte"
136x:= acos * r.
137y:=asin * r
138radius
139"liefert die Radius-Koordinate"
140"(x*x+(y*y)) sqrt
141winkel
142"liefert die Winkel-Koordinate"
143"(x/self radius) arcCos

Man konnte die Koordinaten naturlich genauso gut in polarer Form speichern und die kartesischen berechnen -- für die Benutzerin dieser Objekte spielt das keine Rolle. Man betrachtet die Art und Weise, wie ein Objekt seinen Zustand codiert, als sein _Implementationsgeheimnis_ und die Menge der Methodensignaturen, die den Zugriff auf das Objekt (seinen Zustand) erlauben (das _Protokoll_), als sein _Interface_. Mehr dazu in Abschnitt 4.3.8.

#### Operationen auf zustandslosen (unveränderlichen) Objekten

Auf unveränderlichen Objekten ausgefuhrte Methoden oder Operationen können deren Zustand naturgemass nicht andern. So andert beispielsweise die Addition von Zahlen nichts an ihren Operanden, sondern liefert als Ergebnis ein anderes Objekt. Derratige Methoden (oder Operationen) sind also klassische Funktionen: Sie berechnen anhand eines oder mehrerer Argumente (wovon eines das Emfangerobjekt ist) ein Ergebnis, und das ohne _Seiten-effekte_ wie die Zustandsanderungen der Argumente.

Bei anderen Objekten wie z. B. den Punktobjekten des Abschnitts 4.3.4 ist es hingegen fraglich, ob Operationen wie die Addition den Zustand des Emfangers verändern oder ein neues Objekt zuruckgeben sollen: Bei einer Veränderung des Emfangers wurde die Addition dann eher einer Translation gleichkommen (weswegen die entsprechende Methode auch so genannt werden sollte). Um jedoch zu zeigen, wie man neue Objekte erzeugen und zuruckgeben kann, fehlt uns hier noch einiges; wir kommen erst in Abschnitt 7.3 darauf zuruck.

[MISSING_PAGE_FAIL:71]

zum ersten Problem: Die Identitat der von der konstanten Methode zuruckgegebenen Objekte bleibt erhalten, ihre Erscheinung andert sich aber (beim ersten Problem blieb die Erscheinung gleich, aber die Identitat anderte sich).

Zumindest das zweite Problem lasst sich eindammen, indem man auf Sprachebene durch Literale erzeugte Objekte als unveränderlich annimmt und Anderungen der Art von Zeile 150 entsprechend verbietet. Dies machen einige Smalltalk-Dialekte auch tatsachlich.26 Die eigentliche Erkenntnis ist aber, dass die Referenzsemantik von Variablen und das damit verbundene Aliasing von Objekten zu hochst subtilen Problemen fuhren kann, derer man sich immer gewahr sein sollte.

Footnote 26: In Java sind Array-Literale übrigens nur in New-Ausdrücken erlaubt; die dadurch beschriebenen Array-Objekte werden erst zur Laufzeit und dann immer wieder neu erzeugt, so dass sich keine Aliase ergeben.

#### Primitive Methoden

Zwar ist Smalltalk über weite Teile in sich selbst definiert (was sich darin aussert, dass praktisch die gesamte Sprachdefinition in Form von Methoden hinterlegt und damit für die Programmiererin nicht nur sichtbar, sondern auch anderbar ist), aber für einige primitive Operationen greift es doch auf native Implementierungen zuruck. Dazu zahlt z.B. die Addition (+) für kleine Integer oder auch der Zugriff auf indizierte Variablen mittels at: und at:put: Die entsprechenden Methoden sind in Squeak wie folgt implementiert:

```
152+aNumber
153<primitive:1>
154asuper+aNumber
155at:index
156<primitive:60>
157indexisIntegerifTrue:
158[selfclassisVariable
159ifTrue:[selferrorSubscriptBounds:index]
160ifFalse:[selferrorNotIndexable]].
161indexisNumber
162ifTrue:[^selfat:indexasInteger]
163ifFalse:[selferrorNonIntegerIndex]
164at:indexput:value
165<primitive:61>
166indexisIntegerifTrue:
167[selfclassisVariable
168ifTrue:[(index>=1and:[index<=selfsize])
169ifTrue:[selferrorImproperStore]
170ifFalse:[selferrorSubscriptBounds:index]]
171ifFalse:[selferrorNotIndexable]].
172indexisNumber
173ifTrue:[^selfat:indexasIntegerput:value]
174ifFalse:[selferrorNonIntegerIndex]Dabei stehen die in spitzen Klammern stehenden Ausdrucke jeweils für Aufrufe von primitiven Methoden, die, da man sie als Programmiereerin nicht selbst verwenden soll, nur durchnummeriert wurden. Die Anweisungen nach den Aufrufen der primitiven Methoden werden nur ausgefuhrt, wenn die primitive Methode nicht erfolgreich war. Das bedingt, dass aus einer primitiven Methode mittels Return direkt zuruckgesprungen werden kann, und zwar dorthin, wo die Methode +, at: bzw. at:put: aufgerufen wurde. Dieses Verhalten, das einigermassen ungewohnlich erscheint, wird uns im Kontext von Blocken (Abschnitt 4.4) wieder begegnen.

#### 4.3.8 Protokoll

In SMALLtalk ist das **Interface** eines Objekts die Menge der Nachrichten, die es versteht. Diese Interface wird in Form der sog. **Protokollbeschreibung** o. kurz des **Protokolls** spezifiziert, die aus den _Methodensignaturen_ und den _Kommentaren_ der zu den Nachrichten passenden Methoden besteht und der die **Implementation**, also die Liste der _Methodenrumpfe_, gegenübersteht. Letztere sind, zusammen mit den Instanzvariablen, das **Implementationsgeheimnis** eines Objekts, das hinter seiner Protokollbeschreibung (dem Interface) verborgen wird. Die Kommentare durfen ubtrigens, wie in den meisten anderen Sprachen auch, als (schwacher) Ersatz für eine formale Spezifikation des Verhaltens, das in einer Methode implementiert wird, angesehen werden (vgl. dazu Abschnitt 52.6 in Kurseinheit 5).

Um die Programmierung zu erleichtern, wird in den meisten SMALLtalkSystemen das Protokoll von Objekten in sog. **Nachrichtenkategorien** eingeteilt, die jeweils einen Namen tragen, der die in der Kategorie enthalten Namen zusammenfasst. Da jede Methode in genau eine Nachrichtenkategorie fallen muss, stellen diese eine Partitionierung des Interfaces eines Objekts dar. Unter den Kategorien sind solche, die das Wort,,private" enthalten; deren Methoden sollten dann nicht,,von ausserhalb", also nur vom Objekt selbst (über self) aufgerufen werden. Dies wird jedoch nicht vom Compiler erzwungen. Nachrichtenkategorien haben auch sonst keinerle die Programmausfuhrung betreffende Bedeutung, sondern dienen lediglich der besseren Lesbarkeit.

Wie Sie in der nachsten Kurseinheit lernen werden, werden Protokolle in SMALLtalk nicht auf Objektebene, sondern auf Klassenebene spezifiziert. In STRONGtalk, einer Enweiterung von SMALLtalk um ein (optionales) Typsystem, werden Protokolle dann zu Typen erhoben (s. Kurseinheit 3, Kapitel 20). Da Protokolle nur Methoden enthalten, sind sie den Interfaces javas sehr ahnlich. Tatsachlich werden Protokolle in STRONGtalk auch manchmal Interfaces genannt.

### Blocke

Wir kommen nun zu einer der wichtigsten Auspr\(\ddot{\text{a}}\)gungen von SMALLtalkS Alles-ist-ein-Objekt-Motto: den **Blocken**. Genau wie eine Methode ist einBlock eine abgegrenzte Sequenz, oder Folge, von Anweisungen. Anders als eine Methode ist ein Block jedoch nicht benannt; er kann aber benannt werden, indem er einer Variable zugewiesen wird.

Um auszudrucken, dass eine Sequenz von Ausdrucken ein Block ist, wird die Sequenz mit eckigen Klammern markiert. So ist

175L1 temp1 temp:=x.x:=y.y:=temp1 ```
die Definition eines Blocks, der aus der Deklaration der Variable temp und

Kontext eines Blocks, der Zuweisungen besteht. Die Variablen \(\mathbf{x}\) und \(\mathbf{y}\) seien dabei ausserhalb des Blocks, im **Kontext des Blocks**, deklariert. Dabei ist der Kontext des Blocks die Methode, in der er definiert wurde.27

Footnote 27: In einem Workspace definierte und mittels doIt usw. ausgefuhrte Blocke werden zu diesem Zweck in (temporäre) Methoden übersetzt, die keinem Objekt (oder nil) zugeordnet sind.

Bei der Ausfuhrung des obigen Blocks wird ein neues Blockobjekt er-

Ausfuhrung von

Blockausdrucken

178swap:=temp1 temp:=x.x:=y.y:=temp1
```

wird der Block einer Variable swap zugewiesen. Die Anweisungen, die den Block ausmachen, werden dabei _nicht_ ausgefuhrt, selbst dann nicht, wenn der Block (wie in Zeile 175) isoliert steht und ausgefuhrt wird (das dabei erzeugte Objekt bleibt namenlos und wird von der Speicherbereinigung wieder entfernt).

Um die Anweisungen, die einen Block ausmachen, zur Ausfuhrung zu

Auswertung von

Blocken

bringen, muss man ihn auswerten. Dazu schickt man ihm die Nachricht

**value**. Der Ausdruck

177swapvalue

bewirkt, dass die Variablen \(\mathbf{x}\) und \(\mathbf{y}\) aus dem Kontextt es Blocks ihren Wert tauschen. Das Objekt, zu dem swap value auswertet, ist das Objekt, zu dem die letzte Anweisung auswertet (s. Abschnitt 4.2; im obigen Beispiel also der Inhalt von \(\mathbf{temp}\), der derselbe ist wie der von \(\mathbf{x}\) aus dem Kontext).

Ruckgabewert der Methode **value** ist zunächst immer das Objekt, zu

Wert eines Blocks

dem der letzte Ausdruck eines Blocks auswertet, im obigen Beispiel das durch temp be-

nannte Objekt.

#### Home context und Closure

Da Blocke Objekte sind, die Variablen zugwiesen werden können, können sie auch an andere Methoden übergeben werden. Werden sie dort (mittels **value**) ausgewertet, dannfindet die Auswertung in einem anderen Kontext start. In diesem sind die <<freien" Variablen des Blocks (also die, die nicht selbst als lokale Variablen deklariert wurden; **x** und **y** in Zeile 175) aber gar nicht zugerifugar. Der Block nimmt deswegen seinen Kontext mit (oder, richtiger, der Kontext ist im Block miteingeschlossen). Der Kontext, in dem ein Block definiert wurde (in dem das ihn reprasentierende Objekt erzeugt wurde), nennt man seinen **Home context**. Die Auswertung eines Blocks erfolgt stets in seinem Home context, insbesondere auch dann, wenn ihm **value** in einem anderen Kontext gestendet wurde.

Das folgende Beispiel zweier Methoden soll den Sachverhalt erlautern:

```
178homeContext179|x|x|x:=2.
181selfotherContext:[Transcript show: x printString]
182otherContext:x
183xvalue
```

gibt auf dem Transcript 2 aus, obwohl im Kontext von otherContext: die Variable **x** einen Block und nicht 2 zum Wert hat. Die (Werte der) Pseudovariableen self und super zahlen ubrigens auch zum Home context; dies ist vor allem im Zusammenhang mit dem dynamischen Binden (Kapitel 12 in Kurseinheit 2) interessant.

Dass ein Block aus seinem Home context herausgelost und in einem anderen gespeichert werden kann beinhaltet das Problem, dass die lokale Variablen des Home contexts schon verschwunden sein können, wenn der Block ausgewertet wird. Die durch den Block <<eingefangenen" lokalen Variablen (inkl. formale Parameter) mussen daher unabhangig von der Ausfuhrung der Methoden, die sie definieren, weiterleben. Die Umsetzung von Blocken durch den Smalltalk-Compiler ist alles andere als trivial und verschiedene Smalltalk-Systeme unterscheiden sich darin zum Teil erheblich voneinander, was sich (leider) auch in unterschiedlichem Verhalten ausBert.

Die Blocke Smalltalks heißen in anderen Sprachen ubrigens (lexikalische) Blocke in anderen Closures; sie werden für die sog. Lambda-Ausdrucke, also (anonyme) Sprachen Funktionen, die selbst Objekte oder Werte sind und die deswegen aus ihrem Kontext herausgelost und in andere verschoben werden können, gebraucht. Dabei unterscheiden sich die Sprachen zum Teil erheblich darin, was alles in eine Closure einbezogen werden kann; so können die lokalen Namen (Variablen) beispielsweise auf Konstanten eingeschrankt werden, um zu vermeiden, dass temporare Variablen weiterleben mussen, weil sie in einer Closure enthalten sind.

#### Continuation

Das Konzept des Home context eines Blocks geht aber noch weiter: Es gehoren nicht nur die sichtbaren Variablen aus dem Kontext der Definition des Blocks dazu, sondem auch der sog. Call stack, also der Speicher, in dem die Rucksprungadressen von Methodenaufrufenabgelegt werden. Entsprechend bedeutet eine _Return-Anweisung_ innerhalb eines Blocks bei seiner Auswertung auch stets die sofortige Ruckkehr in den den Block definierenden _Home context_ (der Methode) und nicht in den Kontext (in der Methode), in dem (in der) der Block, durch Senden von **value**, ausgewertet wird. Das nachfolgende Beispiel zeigt das:

```
184homeContextxt
185selfotherContext:[^Transcript show: ^home^]
186otherContext: x
187xvalue.
188Transcript show: ^other'
```

Der Aufruf der Methode homeContext gibt _,home", aber nicht auch noch _,other" auf der Konsole aus. Man nennt dieses Konzept, das ebenfalls aus der Welt der _funktionalen Programmierung_ stammt, auch **Continuation**. Continuations spielen bei der Implementierung von Kontrollstrukturen in Smalltalk eine entscheidende Rolle (s. Kapitel 4.6).

Das Prinzip der Continuation gilt ubrigens auch für geschachtelte Blocke:

```
189[I^true]value.[^false]valuevalue
```

lieferttrue, nicht false. Return-Anweisung verlasst auch alle umschlie@senden Blocke, und zwar sofort. Dies liegt daran, dass explizite Return-Anweisungen aus Blocken immer dahin zuruckkehren, von wo die Definition des Blocks angestosen wurde.

Continuations können zu Laufzeitfehlern fuhren, namlich wenn durch sie

```
190merkwuerdig
191A[^self]
```

verfugt, dann fuhrt
1920merkwuerdigvalue ```

zu einem Laufzeitfehler, da die Auswertung des von merkwuerdig mit ihrer Beendigung zuruckgegebenen Blocks merkwuerdig noch einmal beenden musste, was aber nicht geht. Return-Anweisungen in Blocken sind u. a. deswegen ein umstrittenes Konzept. für Smalltalk sind sie aber unverzichtbar, da mit ihnen fast alle _Kontrollstrukturen_ implementiert werden (s. Kapitel 4.6).

#### Parametrisierte Blocke

Die Blocke von Smalltalk können auch als anonymme Funktionen aufgefasst werden, wobei alle bisherigen parameterlos waren: Der Bezug zu ihrer Umwelt wurde ausschlie@lich über den Home context hergestellt. Es aber auch moglich, Blocke mit Parametern zu versehen,die bei ihrer Auswertung an Objekte aus dem Kontext der Auswertung gebunden werden können. Den obigen Swap-Block konnte man also auch wie folgt definieren wollen:

193 swap:= [ x x y y temp temp temp := x. x x := y y y := temp temp] wobei die jeweils von einem Doppelpunkt eingeleiteten und vom Rest des Blocks durch einen senkrechten Strich abgetrennten Variablen x und y die _formalen Parameter_ des Blocks sind und das -- analog zu einer Methode -- in Strichen eingeschlossene temp eine lokale Variable ist. Der Variable swap vie oben zugewiesen kann der Block mittels

194 swap value: a value: b ausgewertet werden, wenn a und b Variablen aus dem Kontext der Auswertung sind.

**Selbsttestaufgabe 4.2**

(a) Versuchen Sie, durch Oberlegen oder Ausprobieren herauszufinden, ob die Auswertung des Blocks swap aus Zeile 193 seinen (mutmasslichen) Zweck erfullt, also beispielsweise in Zeile 194 den Wert der Variablen a und b tauscht.

(b) Wie sieht das beim Parameterlosen swap aus Zeile 176 (in einem geeigneten Kontext) aus?

(c) begründen Sie, warum es sinnvoll ist, die explizite Zuweisung an die formalen Parameter eines Blocks (im obigen Beispiel \(\mathbf{x}\) und \(\mathbf{y}\)) innerhalb des Blocks zu verbieten.

### Kontrollstrukturen

Kontrollstrukturen regeln den Ablauf des Programms, also die Reihenfolge der Schritte, aus denen seine Ausfuhrung besteht. Anders als in anderen Programmiersprachen gibt es in SMALLtalk nur zwei Kontrollstrukturen, namlich die Sequenz und den dynamisch gebundenen Methodenaufruf; alle anderen, inklusive der Verzweigung und der Wiederholung (Schleife), mussen durch diese simuliert werden. Dies ist moglich, weil SMALLtalk Blocke hat und weil in SMALLtalk (so wie in allen anderen objektorientierten Programmiersprachen) der Methodenaufruf variabler ausfallt als der gewohnliche Prozedur- oder Funktionsaufruf, wie Sie ihn vielleicht von Sprachen wie Pascal oder C her kennen: Er enthalt, wie bereits in Abschnitt 4.3.2 angedeutet, eine _versteckte Fallunterscheidung_ in Form des _dynamischen Bindens_.

#### Sequenz

Die Sequenz als Kontrollstruktur besagt lediglich, dass textuell aufeinanderfolgende Anweisungen eines Programms (einer Methode) auch zeitlich nacheinander ausgefuhrt werden. Die zeitliche Sequenz aufeinander folgender Anweisungen kann lediglich durch andere Kontrollstrukturen (in SMALLtalk nur durch den Methodenaufruf; s. u.) unterbrochen werden.

Dies gilt auch für _parallele Ausfuhring_, die man sich wie die die Gleichzeitige Abarbeitung zweier sequentieller Programme auf denselben Objekten vorstellen kann (s. Kapitel 16).

#### Dynamisch gebundener Methodenaufruf

Wie bereits in Abschnitt 4.3.2 erlautert, verbirgt sich hinter dem Nachrichtenversand in Smalltalk der Methodenaufruf. Wann immer ein Objekt eine Nachricht an ein Emfangreobjekt verschickt, wechselt der Kontrollfluss damit zum Empfangerobjekt, genauer zu der Methode des Empfangerobjekts, das zur Reaktion auf die Nachricht vorgesehen ist. Nach der Abarbeitung der Methode kehrt der Kontrollfluss an das sendende Objekt (genauer: zu der Methode, aus der die Nachricht versandt wurde) zuruck und setzt seine Arbeit dort fort. Bei der Ruckkehr wird auch das Ergebnis der Methode, (eine Referenz auf) ein Objekt, gelierft, das dann an der Stelle des Nachrichtenausdrucks, der den Methodenaufruf bewirkt hat, eingesetzt wird. Der genauer Mechanismus des dynamischen Bindens in Smalltalk wird in Kapitel 12 von Kurseinheit 2 untersucht.

### _Abgeleitete Kontrollstrukturen_

Wenn Sie schon in anderen Programmiersprachen wie z. B. Pascal, C oder Java programmert haben, dann kennen Sie sicher _Schlusseworter_ wie **if**, **else**, **for** und **while**. Diese Schlusselworter stehen für Kontrollstrukturen, feste Bestandteile der Sprache, die für die Steuerung des Ablaufs eines Programms durch die Programmiereerin vorgesehen sind. Man hat sich irgendwann einmal (im Zuge der Diskussion zur sog. _strukturierten Programmierung_) darauf festgelegt, dass jede Programmiersprache über die Kontrollstrukturen Sequenz, Verzweigung, Wiederholung (_Iteration_) und Aufruf verfugen sollte. Wahrend die wikipedia einfache Sequenz von Anweisungen wahrend der Ausfuhrung durch die lineare Folge der Anweisungen im Programmtext vorgegeben ist, sind für alle Abweichungen vom linearen Kontrollfluss, also für Verzweigung, Wiederholung und Aufruf, spezielle Flusssteuerungskonstrukte vorgesehen. Das Goto gehort ubrigens nicht dazu; es gilt seit dem Aufkommen der strukturierten Programmierung als verpont.

In Smalltalk hat man die durch die Syntax der Sprache vorgesehenen Ssmalltalks zwei Kontrollstrukturen auf die Sequenz und den Aufruf, letzteres ausgedruckt Kontrollstrukturen durch das Versenden einer Nachricht an ein Objekt, beschrankt. Alle anderen Kontrollstrukturen mussen mit den Mitteln der Sprache simuliert werden. Was zunächst wie eine erhebliche Einschrankung aussehen mag, erweist sich in der Praxis als gewichtiger Vorteil: Die Programmiereerin kann namlich selbst, wenn ihr danach ist, neue Kontrollstrukturen einfuhren.

#### 4.6.1 Verzweigung

Die einfache Verzweigung wird in SMALLTAK durch das Versenden eine Nachricht, die die bedingt auszufuhrenden Anweisungen in Form eines Blocks als Parameter enthalt, an einen Wahrheitswert realisiert:

```
195x>5ifTrue:[Transcript show:"x>5"]
```

beispielsweise gibt genau dann die Meldung_x>5" auf der Konsole aus, wennx>5zu trueauswertet.

Um zu verstehen, wie das funktioniert, sehen wir uns zunächst die Implementierung der Verzweigung mittels ifTrue:an. Sie wird durch eine Methode ifTrue:aBlockrealisert, die als Parameter aBlock, also eine Folge von Anweisungen, erhalt, das sie, der Bedeutung von If entsprechend, entweder ausfuhrt oder eben nicht ausfuhrt. Diese Methode ist für die beiden Objekte true und false (genauer: für die beiden Objekte, die die Pseudovariable true und false benennen; siehe Abschnitt1.7) jeweils unterschiedlich implementiert:

```
196ifTrue:aBlock197AaBlockvalue
197furtrueund
198ifTrue:aBlock199Anil
199furfalse. Wenn also der Empfanger der Nachricht ifTrue:aBlockdas Objekttrueist, dann bewirkt die Auswertung, dass der Block aBlock ausgefuhrt wird; ist das Objekt hingegen false, wird aBlock nicht ausgefuhrt, was genau der Bedeutung der Nachricht entspricht. So hat
20011=1ifTrue:[Transcript show:"Eins bleibt Einstilt";er]
```

genau den erwarteten Effekt. Aufgrund der _Continuation_ bei Blocken (s. Abschnitt4.4.2) ist es moglich, aus einer Methode mittels ifTrue:bedingt zuruckzukehren:

```
201returnEarly
20211=1ifTrue:[^true].
203Afalse
```

liefert true zuruck, da durch die Auswertung des Blocks[^true] per value in Zeile197 nicht der Block, sondern die Methode returnEarly, beendet wird. Wie man sieht, hat das zunächst etwas eigenwillig anmutende Konzept der Continuation in Kombination mit Return eine erhebliche programmierpraktische Relevarz.

Aus SymmetrieGründen wird auch die Methode ifFalse:aBlockangeboten, die wie folgt implementiert ist:

[MISSING_PAGE_FAIL:80]

#### 4.6.2 Wiederholung

Etwas weiter ausholen mussen wir für die Implementierung von Wiederholungen (Schleifen): Da das Abbruchkwriterium von Schleifen immer wieder (bei jedem Schleifendurchlauf) ausgewertet werden muss, kann nicht einfach einmal eine Nachricht an (eine Variable mit Inhalt) **true** oder **false** gesendet werden. Vielmehr muss die Auswertung des Abbruchkwriteriums selbst in einem Block stattfinden, der bei jedem Schleifendurchlauf neuerlich ausgewertet wird. Aber auch das ist kein Problem: Der Nachrichtenempfanger ist einfach ein Block, dessen Auswertung entweder true oder false zuruckliefert; der Parameter der Nachricht ist dann der Block, der den Schleifenrumpf darstellt, wie in:

```
211x<5whileTrue:x:=x+1
```

whileTrue:ist dazu als Methode für Blocke wie folgt implementiert (beachten Sie, dass Sie den Empfanger, einen Block, in der Methodedefinition nicht direkt sehen; er wird durch self reprasentiert und ist nicht mit dem Parameter aBlock, ebenfalls ein Block, zu verwechseln):

```
213whileTrue:aBlock
214self value
215ifTrue:[
216aBlock value.
217selfwhileTrue:aBlock].
218
219
220\(\Lambda\)nil
```

Wie man sieht, wird hier die Schleife durch eine sog. _Endrekursion_ simuliert: whileTrue:ruftwhileTrue: am Ende selbst wieder auf. Wegen der Performanz (oder moglicher Beschrankungen der Anzahl der Schleifendurchlaufe durch die Grosbe des Aufrufstacks) braucht man sich dabei keine Sorgen zu machen: Da hinter dem rekursiven Aufruf nichts mehr passiert (deswegen ja Endrekursion), kann dieser vom Compiler in eine echte Schleife überestrd werden. für die Implementierung von whileFalse: (mitentsprechender Semantik) braucht (brigens nur das ifTrue:aus Zeile 215 durch ifFalse: ersetzt und der rekursive Aufruf entsprechend angepasst zu werden.

Fur die ebenfalls aus anderen Sprachen bekannten For-Schleifen hat SMALLtalk eine andere elegante Losung parat, auf die wir im nachsten Abschnitt eingehen werden.

#### 4.6.3 Iteration

Wenn Sie If und While schon kennen, kennen Sie sicher auch For. Die klassische Form der For-Schleife verwendet eine Zahlvariable, einen Anfangswert, ein lhrement (das auch negativ, also ein Dekrement sein kann) sowie einen Endwert. Solche For-Schleifen gibt es in SMALLtalk auch:

```
2195to:1by:-2do:[:i1Transcriptshow:iprintString]

[MISSING_PAGE_FAIL:82]

* [236]**do: aBlock**
* [237]**1**to: self size do:
* [238]**238**[:index] aBlock value: (self at: index)]

Dabei ist to:do: für Ganzahlen analog zu obigem to:by:do implementiert. Die Zahlvariable index des Blocks von Zeile 238 lauft so von 1 bis zur Anzahl der indizierten Instanzvariablen des Empfangers von do: (im obigen Beispiel ein Array), die über den Aufruf von size auf dem Empfanger (reprasentiert durch self) abgefragt wird. Der Inhalt der indizierten Instanzvariablen des Empfangers wird dann der Reihe nach als Parameter mittels value: an den Block aBlock zur Auswertung geschickt.

#### 4.6.4 Iterieren über :\(n\)-Beziehungen

Bei Zu-1-Beziehungen schickt man haufig dem von der betreffenden Variable referenzierten Objekt eine Nachricht. Der Ausdruck

* [239]**freund einladen**

beispielsweise besagt, dass das Objekt, mit dem der Besitzer der Variable freund über diese Variable in :1-Beziehung steht, die Nachricht einladen erhalten soll. Wenn man dasselbe mit :\(n\)-Beziehungen machen mochte, so erreicht die Nachricht -- bei qleicher Vorgehensweise -- nicht die logisch in Beziehung stehenden Objekte, sondern das die Beziehung selbst reprasentierende Zwischenobjekt (das ja Wert der Variable ist), das mit dieser Nachricht jedoch nichts anfangen kann. Um die Nachricht stattdessen an alle durch das Zwischenobjekt referenzierten Objekte zu senden, schickt man dem Zwischenobjekt die Nachricht do: aBlock, wobei ablock ein mit einem Parameter parametrisierter Block ist, der für jedes Element des Arrays genau einmal (mit dem Element als tatsachlichem Parameter) aufgerufen wird. Wenn also z. B. die Instanzvariable freunde heilst und eine :\(n\)-Beziehung ausdruckt, dann schreibt man statt Zeile 239
* [240]**freunde do: [freund freund einladen]**

Man kann sich fragen, warum die Smalltalk-Syntax nicht erlaubt, die Nachricht doch direkt an das Zwischenobjekt zu schicken, das die :\(n\)-Beziehung reprasentiert (also im gegebenen Beispiel freunde einladen), und dies dann intern so umsetzt, dass die Nachricht an alle Objekte geschickt wird. Der einfache Grund dafur wird gleich offenbar: Weil man haufig die Nachricht gar nicht an alle Objekte schicken will, sondern nur an ausgewahlte, und weil dazu dann noch weitere Angaben notwendig sind, so dass im allgemeinen Fall nichts gewonnen ware.

Auf Basis von do: lassen sich nun zahlreiche weitere naturliche und ausferst praktische Kontrollstrukturen erzeugen. So ist wie im obigen Beispiel recht haufig eine Nachricht gar nicht an alle Elemente einer :\(n\)-Beziehung zu senden,sondern nur an solche, die bestimmte Kriterien erfullen. Dazu ist es moglich, die Beziehung quasi im Vorübergehen einzuschranken und den Block dann nur auf der Einschrankung auszufuhren:

```
241(freundeselect:[:fretund|freundeng==true])do:[:freund|freundeinalden]
```

Dabei ist die Methode select: wie folgt implementiert:

```
242select:aBlock
243answer:=selfspeciesnew.
245selfdo:[:element|
246(aBlockvalue:element)
247iftrue:[answeradd:element]].
248answer
```

Zeile 244 mussen Sie hier noch nicht verstehen; der Rest sollte lhnen aber inzwischen klarsein. answer ist eine _temporare Variable_, die nur innerhalb der Methode Gultigkeit hat; ihr werden in der Do-Schleife mittels add:(einer Methode mit offensichtlicher Funktion) alle die Elemente des Empfangers hinzugefugt, für die der Parameterblock aBlock zu true auswertet.

Auf ahnlich einfache Weise lassen sich nahezu beliebig weitere Kontrollstrukturen realisierren. Zu select: komplementar ist beispielsweise die Methode reject:, die aus einer:n-Beziehung alle die Elemente entfernt, die eine genannte Bedingung nicht erfullen:

```
249reject:aBlock
250aselfselect:[:element|
251(aBlockvalue:element)not]
```

Kaum zu glauben, dass mit so wenig Aufwand der Verwendung eine neue Kontrollstruktur hinzugefugt werden kann.

Eine weitere praktische Methode, die eine Sammlung von Objekten zuruckgibt, über die dann (mittels do:) iteriert werden kann, ist collect:, sie sammelt all die Elemente, die die Auswertung des ihr als Parameter übergebenen Blocks auf den Elementen der ursprunglichen Sammlung zuruckliefert, und ist wie folgt implementiert:

```
252collect:aBlock
253|answer|
254answer:=selfspeciesnew.
255selfdo:[:element|
256answeradd:(aBlockvalue:element)].
257Aanswer
```

Aber auch einzelne Elemente einer Beziehung lassen sich bestimmen: detect:mit einem Block aBlock als Parameter aufgerufen liefert z. B. aus einer Sammlung von Elementen das erste Element zuruck, auf dem aBlock ausgewertet den Wahrheitswert true ergibt (wobei bei Fehlen eines solchen Elements ein Fehler geliefert wird). Das erlaubt z. B. den Ausdruck258 (freunde detect:[ :freund[ freund eng]) treffen

zu formulieren, der besagt, dass man sich mit dem ersten engen Freund, und nur mit dem, trifft. für die Pravis wichtiger ist die Variante detect:aBlockifNone:exceptionBlock, die detect:aBlockum einen (parameterfosen) Block erganzt, dessen Wert bei Fehlen eines geeigneten Elements zuruckgegeben wird.

**Selbsttestaufgabe 4.5**

Versuchen Sie, eine Implementierung der Methode detect:aBlock selbst zu entwerfen.

Eine ganze Klasse von immer wiederkehrenden Anweisungsequenzen zu

**Kumulation**

ersetzen erlaubt schliesslich die Methode inject:into::Es erganzt die Funktionsweise von **do:** darum, das Ergebnis der Auswertung eines Blocks in einem Iterationsschritt als ersten Parameter in die Auswertung des nachsten Schritts einzuspeisen. So lasst sich beispielsweise das ode Akkumulieren von Eigenschaften (inkl. der gern vergessenen Initialisie- rung des Akkumulators) elegant wie folgt ausdrucken:

259freunde

260inject:true

261into:[ :einsam :freund[ einsam and:[freund eng not]]

So einfach kann Programmieren sein!

Fur Interessierte: Methoden wie do:, collect:, select:und inject:sind allesamt (als Funktionen hoherer Ordnung) aus der funktionalen Programmierung bekannt. In die objektorientierte Programmierung mit Sprachen wie JAVA oder C# haben sie jedoch erst sehr kurs spat Einzug gehalten.

## 5 Zusammenfassung der Smalltalk-Syntax

Sicher ist Ihnen aufgefallen, dass uns bislang keine _Schlusseworter_ in Smalltalk begegnet sind (bis auf die sog. _Schlusselwortnachrichten_, die aber frei wahlbar und deswegen eben gerade keine Schlusselworter sind; vgl. Abschnitt 4.1.2). Der Grund hierfur ist einfach: Es gibt keine Schlusselworter_, lediglich ein paar _Symbole mit spezieller Bedeutung._ Es sind dies:

\begin{tabular}{l l} \hline \hline Symbol & Bedeutung/Verwendung \\ \hline := & Zuweisung \\  & Trennzeichen zwischen zwei Anweisungen sowie \\  & Dezimalpunkt für Gleitkommazahlen \\  & Trennzeichen zum Kaskadieren von Nachrichten \\  & Markierung von Parametem in Nachrichten und Blocken \\  & Klammerung von Ausdrucken zur Festschreibung der Reihenfolge der Auswertung \\  & Bildung von Blocken \\  & Trennzeichen zwischen den Parametern eines Blocks und seinen Anweisungen \\ \end{tabular}

\begin{tabular}{l|l} \hline Symbol & Bedeutung/Verwendung \\ \hline \(\mid\mid\) & Deklaration von temporaren Variablen in Methoden (und Blocken) \\ \(\mid^{n}\) & Markierung von Kommentaren \\ \(\mid^{n}\) & Markierung von String-Literalen \\ \(\$\) & Markierung von Zeichenliteralen \\ \(\#\) & Markierung von Symbol- und Array-Literalen \\ \(\^{\Lambda}\) & Ruckgabe-Operator (Return) \\ \end{tabular}

Das ist alles! Die resverierten Namen true, false, nil, self und super sind die von _Pseudovariablen_; alle aus anderen Sprachen bekannten Schlusselworter sind als Methoden in SMALLtalk selbst definiert.

## 6 Losungen zu den Selbsttestaufgaben

\begin{tabular}{l l} \hline
262 & Sa == Sa == true \\
263 & 1 == 1 \(\Rightarrow\) true \\
264 & 1.0 == 1.0 \(\Rightarrow\) false (true in Squeak) \\
265 & 100000000 == 100000000 \(\Rightarrow\) false (true in Squeak) \\
266 & \#(1 2 3) == \#(1 2 3) \(\Rightarrow\) false (true in Squeak) \\ \end{tabular}

Es fallt auf, dass bei manchen Zahlen (syntaktisch) gleiche Literale identische Objekte reprasentieren, manche nicht. In Squeak ist das ubrigens nur anders, weil der Compiler eine Art _Literaloptimierung"_ betreibt: Zwei gleiche Literale, die gemeinsam übersetzt werden, liefern das identische Objekt.

\begin{tabular}{l} \hline
**Selbsttestaufgabe 1.3 (Seite 23)** \\ \end{tabular}

Das ist im wesentlichen dieselbe Aufgabe wie Selbsttestaufgabe 1.1, also auch dieselbe Losung.

Dies erklart auf einfache Weise, warum der Test auf Identitat (==) bei gleichen Literalen für verschiendene Arten von Objekten zu verschienden Ergebnissen fuhrt: Er vergleicht einfach die systeminterne Repräsentation. Handelt es sich bei der linken und der rechten Seite um den Verweis auf dieselbe Stelle im Speicher, ergibt der Test true; handelt es sich bei der linken und der rechten Seite um denselben Wert (im Falle von Zeichen und kleinen Ganzzahlen), ergibt der Test ebenfalls true. In allen anderen Fallen ergibt er false.

\begin{tabular}{l} \hline
**Selbsttestaufgabe 1.2 (Seite 21)** \\ \end{tabular}

Wie Squeak so nett sagt: _._lots of globals", so u. a. Transcript und sich selbst. Zugleich enthalt es offenbar auch ein Symbol für jede Klasse (so z. B. \(\#\)Object).

[MISSING_PAGE_EMPTY:87]

* [277]**detect:**einBlock
* [278]**self do:**[:elem | (einBlock value: elem) iftrue: [^^elem]]

[MISSING_PAGE_EMPTY:89]

Kurseinheit 2: Systematik der objektorientierten Programmierung

In der vorangegangenen Kurseinheit haben Sie die Grundkonzepte der objektorientierten Programmierung mit Smalltalk kennengelernt. Neben den Objekten selbst zahlen dazu vor allem die Beziehungen zwischen diesen (durch Instanzvariablen ausgedruckt), der davon abgeleitete Zustand von Objekten sowie das in Form von Methoden definierte Verhalten. Was bislang verschwiegen wurde, ist, wie Objekte, für die es keine literale Repräsentation gibt, entstehen und wie ihnen ihre Instanzvariablen und ihre Methoden zugeordnet werden.

Wie das zu geschehen hat, ist mit dem Begriff der objektorientierten Programmierung nicht grundsatzlich festgelegt. Eine gewisse Anerkennung und Verbreitung erfahren haben aber drei verschiedene Ansatze:

1. der Konstruktoransatz, bei dem der Aufbau eines Objekts in einer Methode beschrieben wird, in der dem Objekt bei seiner Erzeugung Instanzvariablen und Methoden zugeordnet werden; verschiedene Konstruktoren erzeugen dann verschieden aufgebaute Objekte;
2. der Prototypenansatz, bei dem ein schon existierendes Objekt samt seiner Instanzvariablen und Methoden geklont wird; ein Klon kann bei Bedarf um weitere Instanzvariablen und Methoden erganzt werden oder geklonte können abgeandert oder entfernt werden; und
3. der Klassenansatz, bei dem alle Objekte als _Instanzen_ vonbestimmten Vorlagen, die entweder selbst keine Objekte oder Objekte auf einer anderen Ebene sind, erzeugt werden.

Den Konstruktoransatz findet man in Sprachen wie Emerald, den Prototypenansatz in Sprachen wie Self oder JavaScript und den Klassenansatz in Sprachen wie Smalltalk, C++, Eifel, Java, C#, Scala und vielen anderen mehr.

Aus verschieden Gründen hat sich die dritte Variante, die **klassenbasierte Form der Objektorientierung** (wobei die Klassen die erwahnten Vorlagen sind) gegenüber der zweiten, der **prototypenbasierten Form der Objektorientierung** weitgehend durchgesetzt. Die erste Variante findet im Zuge einer gewissen Eruchterung bzgl. der objektorientierten Programmierung zunehmed Anhanger, und zwar da, wo Objekte und _dynamics Binden_ (s. Abschitt 12) im Kontext traditioneller imperativer Programmierung angeboten werden sollen. Sie liegt damit aber aüberhalb des Gegenstands dieses Kurstekes.

Die Dominanz der klassenbasierten Form der objektorientierten Programmeriung liegt vermutlich zum einen daran, dass Klassen ein klassisches, in anderen Disziplinen wie der Mathematik oder der Biologie fest etabliertes Ordnungskonzept darstellen, mit dessen Hilfe sich auch objektorientierte Programme gut strukturien lassen, und zum anderen daran, dass Klassen sich als (Vorlagen fur) Typen eignen und somit die objektorientierte Programmierung Eigenschaften anderer, nicht objektorientietter, dafur aber typisierter Sprachen (also Sprachen, bei denen alle Variablen und Funktionen bei der Deklaration einen Typ zugeordnet bekommen und der Variableninhalt immer vom deklarietten Typ sein muss) übernhehmen kann (der Gegenstand von Kursenheit 3). Die prototypenbasierte Form der Objektorientierung hat hingegen den Charme, dass sie mit weniger Konzepten auskommt und dass sie sehr viel flexibler einzelne Objekte an ihren jeweiligen Zweck anpassen kann, z. B. indem sie eine Methodende-finition nur für ein einziges Objekt abzuandern erlaubt. Letzteres ist z. B. bei der Programmeriung von grafischen Bedienoberflachen, bei der das Drucken verschiedener Buttons jeweils verschiedene Ereignisse auslost (Methoden aufruft), sehr praktisch. Nicht umsonst ist JavaScript als Programmiersprache für interaktive Webseiten so erfolgreich.

Auch wenn es gute Gründe für die prototypenbasierte Form der objektorientierten Programmerung gibt (und sich deswegen jedes Werk zum Thema objektorientierte Programmierung -- so wie auch das lhnen vorliegende -- gemubBigt fuhlt, darauf hinzuweisen, dass es sie gibt), werden ich mich im folgenden vornehmlich Klassen als strukturbildenden Konzepten der objektorientierten Programmierung zuwenden und nur hier und da Prototypen kurz die Referenz erweisen.28

Footnote 28: Interessanterweise war der prototypenbasierten Sprache Self bei Sun Microsystems ursprünglich der Platz zugedacht, den dann spater Java einnehmen sollte. Self war zwar für die Entwicklung der Java Virtual Machine ein wichtiger Ideenlieferant, ist jedoch außerhalb dieser Kreise kein Erfolg beschieden gewesen. Der Erfolg von JavaScript zeigt aber, dass das Konzept der prototypenbasierten Programmierung zumindest kein Irweg war.

## 7 Klassen

Sprachphilosophisch gesehen ist eine Klasse ein _Allgemeinbegriff_ wie etwa _Person_, _Haus_ oder _Dokument_. Diese Allgemeinbegriffe stehen in der Regel für eine ganze Menge von Objekten, also etwa alle Personen, Hauser oder Dokumente. Gleichwohl ist die Klasse selbst immer ein Singular -- sie ist namlich selbst ein Objekt, das unter den Allgemeinbegriff _Klasse_ fallt. Diese Sprachregelung wird auch in der objektorientierten Programmierung eingehalten (obwohl sie naturlich nicht, da Computer unsere Sprache nicht kennen, überprüt werden kann und deswegen Abweichungen immer wieder vorkommen): Alle Klassennamen sind Singulare.

Mit jedem Allgemeinbegriff verbinden wir eine ganze Reihe von _Eigenschaften_, die für ihn charakteristisch sind, die wir aber nicht dem Begriff selbst, sondern den Objekten, die dartunter fallen, zuordnen. Mit _Person_ etwa ist _Name_ verbunden sowie _Geburtstag_ und ggf. weitere Attribute, aber auch bestimmtes, für Personen charakteristisches _Verhalten_. Das gleiche gilt für _Haus_, _Dokument_ und alle anderen Allgemeinbegriffe. Existenz und Adaqutheit von Allgemeinbegriffen sind Thema grosser philosophischer Diskurse wie etwa dem sog. _Universalienstreit_ und stehen hier nicht zur Debatte. Wichtig ist, dass mit ihnen stets Satze wie,,cein Individum> ist ein <ein Allgemeinbegriff>" gebildet werden können, also etwa,,Peter ist eine Person". Mit solchen Satzen verbindet sich namlich die übertragung aller Eigenschaften, die mit einem Allgemeinbegriff verbunden sind (s. o.), auf das Individum. So hat Peter, wenn er eine Person ist und _Person_ wie oben definiert wurde, eben auch einen Namen und einen Geburtstag.

### **Klassifikation**

Durch die Zuordnung von Individuen oder Objekten zu Allgemeinbegriffen oder Klassen findet eine **Klassifikation** statt. Diese Klassifikation erlaubt eine Ordnung oder Strukturrie- rung der Anwendungsdomane, indem bestimmte Aussagen nur noch für die Klassen teroffen werden mussen und nicht mehr für jedes einzelne Objekt. Anstatt also wie in der vorangegangenen Kurseinheit Instanzvariablen und Methoden direkt Objekten zuzuordnen, verbindet man sie mit Klassen und vereinburt, dass alle mit einer Klasse verbundenen Eigenschaften und Verhaltenspezifikationen nicht die Klasse in ihrer Gesamtheit, sondern die einzelnen Objekte, die zu der Klasse gehoren, beschreiben.

In diesem Zusammenhang ist es sinnvoll, die Unterscheidung von Extension und Intension eines Begriffs ins Spiel zu bringen. Unter der **Extension** (Ausdehnung oder Erstreckung) eines (Allgemein-)Begriffs versteht man die Menge der Objekte, die dartunterfallen. Im Fall von _Person_ etwa ist das die Menge aller Personen, im Fall von _Dokument_ die Menge aller Dokumente. Die **Intension** (nicht zu verwechseln mit Intention!) eines (Allgemein-)Begriffs hingegen ist die Summe der Merkmale, die den Begriff ausmachen und die die Objekte, die dartunter fallen, charakteristieren. Sie ist gewissermanessen das Auswahlpradikat oder die charakteristische Funktion, die zu einem beliebigen Element entscheidet, ob es unter den Begrifft fallt. Schon Aristoteles fiel auf, dass Intension und Extension in einem inversen Grossenverhaltnis zueinanderstehen: Mit wachsender Intension schrumpft die Extension und umgekehrt. Dies ist freilich nicht weiter verwunderlich: Je umfangreicher die Charakterisierung einer Menge von Objekten ist, d. h., je strenger die Bedingungen sind, die ein Objekt erfullen muss, um dazuzugehoren, desto weniger Objekte erfullen diese Bedingungen und desto kleiner ist entsprechend die Menge. Wir werden in Kapitel 9 noch einmal darauf zuruckkommen.

Allgemeinbegriffe sind die Vorbilder für Klassen in der objektorientierten Programmierung. Interessantenweise bildet eine wichtige philosophische Abweichung vom Glauben an die Adaquatheit von Allgemeinbegriffen, die Idee der _Familienahnlichkeiten_, wie sie von Ludwig Wittgenstein in seiner spaten Philosophie entworfen wurde, die Grundlage für die schon enwahnte Alternative zu den Klassen, namlich die **Prototypen**. Die Idee Wittgensteins, wie auch der prototypenbasierten Programmierung, ist, dass ein Allgemeinbegriff (eine Klasse) niemals eine adaquate Beschreibung aller Individen (Objekte) sein kann, die man mit dem Begriff verbindet. Wittgenstein verwendet dafur das Beispiel vom Spiel: Auch wenn es Spiele gibt, die einander stark ahneln, so ist der Begriff vom Spiel doch nicht so scharf getasst, dass es eine Grenze gabe, innerhalb derer etwas ein Spiel wie alle anderen, ausserhalb derer es aber kein Spiel mehr ist. Vielmehr gibt es, nach Wittgenstein, mehr oder weniger,,spielhaftte" Spiele, also prototypische Spiele und solche, die diesen mehr oder weniger gleichen.

Zwar gibt es Anwendungsdomanen, in denen Wittgensteins Familienahnlichkeiten die Sachlage besser beschreiben als die traditionellen Allgemeinbegriffe (man denke z. B. an Musik, in der es zwar Tone und Noten gibt, aber dennoch zwei Tone selten genau gleich klingen sollen und die Notenzeichen entsprechend vielfältig varieren), aber insgesamt sind die ublicen Anwendungen doch eher der Natur, dass es von einigen wenigen Sorten eine grose Menge von Objekten gibt, die alle mehr oder weniger gleich zu behandeln sind. Und so vereinfachen Allgemeinbegriffe, oder Klassen, unsere Weltsicht ganz erheblich und damit auch die Programme, die wir schreiben, um unsere Weltsicht zu reflektieren.

Nachdem wir uns also auf Klassen festgelegt haben, können wir nun endlich zur Luftung des Geheimisses kommen, wo in einem smalltalk-Programm die Instanzvariablen und Methoden, die Objekte ihr eigen nennen, vereinbart (deklariert) und im Falle der Methoden auch definiert (mit Inhalt versehen) werden: in Klassen.

### Klassendefinitionen

Eine **Klassendefinition** liefert die _Intension_ einer Klasse. Sie besteht in

Smalltalk zunächst aus der Angabe eines nicht anderweitig verwendeten, durch ein Symbol reprasentierten Klassennamens sowie der Angabe der die Objekte der Klasse beschreibenden _Instanzvariablen_ und _Methodendefinitionen_. Anders als in vielen anderen objektorientierten Programmiersprachen erfolgt in Smalltalk die Klassendefinition nicht in einer Datei (was hatte eine Datei auch mit den Konzepten einer Programmiersprache zu tun?), sondern durch Eintragungen in eine dafur vorgesehene Datenstruktur (genauer: durch Erzeugung eines die Klasse beschreibenden Objekts). Es gibt also auch insbesondere keine Syntax für eine Klassendefinition, sondern nur ein Schema. Ein solches, wenn auch noch unvollstandiges, Schema ist das folgende:Alle Instanzen einer Klasse verfugen somit über den gleichen Satz von Instanzvariablen, aber nicht denselben, was soviel bedeuttet wie dass jede Instanz der Klasse (jedes Objekt, das zur Extension der Klasse gehort) diese Variablen individuell belegen kann. Im Gegensatz dazu verstehen alle Instanzen einer Klasse nicht nur dieselben Nachrichten, sie verwenden auch dieselben Methodendefinitionen, um auf die Nachrichten zu reagieren. Instanzen einer Klasse können sich also nur insoweit in ihrem Verhalten unterscheiden, wie sich die Methodendefinitionen auf die Werte der Instanzvariablen beziehen, wie also das in den Methoden spezifizierte Verhalten vom Inhalt der Instanzvariablen abhangt. Insbesondere ist es nicht vorgesehen, dass verschiedene Instanzen einer Klasse über verschiedene Definitionen einer Methode (genauer: über verschiedene Definitionen von zu der Nachricht passenden Methoden) verfugen. Das unterscheidet die klassensbaisierte von der prototypenbasierten Form der objektorientierten Programmierung.

Die beiden Eintrage,,indizierte Instanzvariablen" und,,atomar" stehen ubrigens dafur, ob eine Instanz der Klasse indizierte Instanzvariablen haben soll (klar) und falls ja, ob diese Variablen dann eine binare Repräsentation (ja) oder Referenzen (nein) enthalten. Mit Hilfe von indizierten Instanzvariablen, die binare Repräsentationen enthalten, werden z. B. Zahlen, Strings, aber auch Bitmaps wie Fensterinhalte, der Cursor oder Fonts interm dargestellt. Da man als Programmiererin solche Klassen in der Regel nicht selbst anlegt, werde ich den Eintrag,,atomar" zukunfttig unter den Tisch fallen lassen.

Eine Klasse (das Objekt, das die Klassen reprasentiert, nicht ihr Name) **Repräsentation von**

wird in Smalltalk nach ihrer Erzeugung ubrigens durch eine globale Pseudovaniable reprasentiert, deren Name der Name der Klasse ist. Da die Variable global ist, muss sie (und damit auch der Name der Klasse) immer mit einem Großbuchstaben beginnen (s. Abschnitt 1.5.2 in Kursenheit 1). Die Variable wird automatisch mit der Klassendefinition eingefuhrt (vereinbart); ihr,,Wert", die Klasse, auf die sie verweist, ist das Objekt, das ihr bei der Anlage der Klasse zugewiesen wird. Da Klassennamen globale Variablen sind, da sie insbesondere absolut global sind und nicht nur in Bezug auf irgendeine Programmentiheit (wie etwa eine Methodendefinition), sind sie von überall her zugereifbar. Ausserdem wird jede neue Klasse in eine Art Systemworterbuch namens,,Smalltalk" (reprasentiert von der globalen Variable Smalltalk; s. Selbsttestestaufgabe 1.2) eingetragen und ihr Name (als Symbol) in die Symboltable SymbolTable.

Vergewissern Sie sich, dass die Klasse Class in Smalltalk enthalten ist und das Symbol #Class in SymbolTable (nur Smalltalk Express). Enthalt Smalltalk auch andere Objekte als Klassen?

Mittels einer solchen Klassendefinition ist man nun in der Lage, das Smalltalk-System um neue, eigene Klassen zu erweitern. Ein Beispiel für eine solche neue Klasse gibt die folgende (wie gesagt noch unvollstandige) Klassendefinition, die auf einfache Weise einen Stapelspeicher (Stack) implementiert, der seine Elemente in indiizierten Instanzvariablen und den Stapelzeiger (Stack pointer) in einer benannten halt:

\begin{tabular}{l l} \hline \hline \multicolumn{1}{l}{Rasse} & Stack \\ \hline benannte Instanzvariablen & stackpointer \\ \hline nnditerle Instanzvariablen & ja \\ \hline
279 push: anElement & \\
280 "left neues Element auf Stapel" & \\
281 stackpointer := stackpointer + 1. & \\
282 self at: stackpointer put: anElement & \\
283 pop & \\
284 "entfernt oberstes Element vom Stapel" & \\
285 stackpointer := stackpointer - 1 & \\
286 top & \\
287 "liefert oberstes Element des Stapels" & \\
288 " self at: stackpointer & \\ \hline \hline \end{tabular}

Nur zur Wiederholung: Die Pseudovariable self in den Zeilen 282 und 288 steht jeweils für das Objekt, das die die Methode auslosende Nachricht erhalten hat (das Empfangerobjekt): Sie ist notwendig, da der Zugriff auf die indizierten Instanzvariablen in Smalltalk immer über die Methoden at: und at:put:erfolgt, deren Aufruf (als Nachrichtenausdruck) stets einen Empfanger benotigt. Anders als z. B. in Java (wo this die Rolle von **self** einnimmt) wird bei fehlendem Empfanger innerhalb einer Methode nicht einfach das Empfangerobjekt angenommen, sondem ein Syntaxehler gemeldet.

Bei genauem Hinsehen bemerkt man, dass die obige Implementierung eines Stacks einen Schonheitsfehler besitzt: Wahrend die Manipulation der benannten Instanzvariable stackpointer, deren Wert ja von den Methoden von **Stack** aktualisiert wird, durch andere Objekte noch verhindert werden kann, ist dies für die indizierten Instanzvariablen eines Stack-Objekts nicht der Fall. Eine Benutzerin eines solchen Objekts kann stattdessen mittels at: und at:put: jederzeit auf jedes beliebige Element des Stacks zugreifen, und zwar unabhangig davon, ob dies geradeoben auf dem Stack liegt. Eine Instanz der Klasse Stack verbigt also nicht wie in Kurseinheit 1, Abschnitt 4.3.4 gefordert die Repräsentation ihres Zustands, der Stack-Elemente. Um dies zu bewirken, muss man anstelle der indizierten Instanzvariablen eine benannte verwenden, die selbst ein Objekt mit indizierten Instanzvariablen halt (ein Zwischenobjekt; s. Abschnitt 2.2), und die Speicherung der Elemente des Stacks diesem zweiten Objekt übertragen. Die Implementierung s ahe dann wie folgt aus:

\begin{tabular}{l l} \hline \hline Klasse & Stack \\ \hline benannte Instanzvariablen & stackcontent stackpointer \\ \hline indizierte Instanzvariablen & nein \\ \hline Instanzmethoden & \\ \hline
289 push: anElement & \\
290 "legt neues Element auf Stapel" & \\
291 stackpointer := stackpointer + 1. & \\
292 stackcontent at: stackpointer put: anElement & \\
293 pop & \\
294 "entfent oberstes Element vom Stapel" & \\
295 stackpointer := stackpointer - 1 & \\
296 top & \\
297 "liafert oberstes Element des Stapels" & \\
298 "stackcontent at: stackpointer & \\ \hline \end{tabular}

Auf die Variable stackcontent kann von anderen Objekten nicht direkt zugegriffen werden -- sie ist verborgen (und nur noch indirekt, über push:, pop und top manipulier- bzw. lesbar). Das bedeutet jedoch nicht, dass auf das von stackcontent benannte (Zwischen-)Objekt nicht zugegriffen werden kann -- aufgrund der oben dargestellten Klassendefinition ist namlich noch unklar, wo das Objekt, das den Stack-Inhalt fasst, herkommt, so dass nicht ausgeschlossen werden kann, dass bereits _Aliase_ existieren (s. Abschnitt 1.8). Eine Moglichkeit, dies auszuschliessen, ist, das Stack-Objekt sein Zwischenobjekt selbst erzeugen zu lassen. Dem wenden wir uns als nachstes zu.

### Instanziierung

Klassendefinitionen bilden also eine Art Vorlage für Objekte. Um nun von einer solchen Vorlage Objekte mit Eigenschaften (Instanzvariablen und Methoden), wie sie durch die Definition (Intension) festgelegt sind, zu erzeugen, muss man sie **instanziieren**. Die Instanziierung ist ein Vorgang, bei dem ein neues Objekt entsteht -- sie ist gewissermangen die Umkehrung der _Klassifikation_, also des übergangs vom Individuum zu seiner Klasse (wobei die Klassifikation, anders als die Instanziierung, in der Programmierung kein Vorgang ist). Vorm erzeugten Objekt sagt man dann, es sei **Instanz** dieser Klasse. Tatsachlich spricht man in Smalltalk, da ja auch Klassen Objekte sind, haufig von Instanzen anstelle von Objekten, wenn keine Klassen gemeint sind. Wie wir schon im nachsten Kapitel sehen werden, sind in Smalltalk jedoch auch Klassen Instanzen. So gesehenhandelt es sich bei den Begrifffen _Instanz_ und _Klasse_ also eher um Rollen von Objekten, die im Verhaltnis der Instanziiering zueinander stehen. Die Begriffsbildung der objektorientierten Programmierung ist an dieser Stelle aber leider nicht besonders gelungen.29

In SMALLtalk ist jedes Objekt Instanz genau einer Klasse. (Genaugenommen ist es **direkte Instanz** genau einer Klasse, aber zum Unterschied zu **Klassen** _indirekten Instanzen_ kommen wir erst in Abschnitt 9.1.) Dabei weiss jedes Objekt, von welcher Klasse es eine Instanz ist; diese Information lasst sich dem Objekt durch Senden der Nachricht **class** _entlocken; der entsprechende Ausdruck liefert das Objekt, das die Klasse reprasentiert, zuruck.

Mit der Instanziiering wird der _Extension_ einer Klasse ein neues Element

**mengentheoretische** hinzugefugt. Das Elementsein auf Mengenebene entspricht also in etwa

**Interpretation**

dem Instanzsein auf programmiersprachlicher Ebene (in _UML_ wie im obigen Diagramm durch einen gestrichelten Pfeil angedeutet). Wir werden noch ofter auf diese mengentheoretische Interpretation zuruckkommen.

Die Objekte, die wir in Kurseinheit 1 kennengelernt haben, wurden samt-

**Instanziiering mit**

**new und new:**

**new und new:**

**new**

**und new:**

**new**

**und**

**new**

**:

**Instanziiering und Klassen hat man nun die Moglichkeit, neue -- und neuartige -- Objekte programmatisch, also per Programmausfuhrung, zu erzeugen. Dies geschieht standardm-

Big, indem man der Klasse, von der man eine Instanz haben mochte, die Nachricht **new** (fur Klassen ohne indizierte Instanzviablen) oder **new:** (fur Klassen mit indizierten Instanzviablen) schickt. Das neue Objekt wird in Reaktion auf die Nachricht (durch eine entsprechende _primitive Methode_ des SMALLtalk-Systems; s. Abschnitt 4.3.7) im Speicher angelegt und seine Instanzvariablen werden alle mit nil initialisiert. Der Parameter der Nachrichtnew: muss immer eine naturliche Zahl sein und legt die Anzahl der indizierten Instanzvariablen fest, über die ein Objekt verfugt. Hat ein Objekt (per Klassendefinition; s. Abschnitt 7.2) keine indizierten Instanzvariablen, fuhrt **new:** zu einem Laufzeitfehler.

Einen neuen Stack mit Platz für 100 Elemente erhalt man, indem man, bei obiger erster Klassendefinition von **Stack**, den Ausdruck

299Stack new: 100

auswertet. Dabei ist **Stack** wie gesagt eine Pseudovariable, die den Klassennamen tragt, die auf das Objekt verweist, das die Klasse reprasentiert, und der ihr Wert beim Anlegen der Klasse vom Systemz zugewiesen wurde. In der zweiten Form der Implementierung ware eben dieser Ausdruck verbboten: Stattdessen durfte der Ausdruck dann nur noch

300Stack new: heissen. Dass der Stack dann trotzdem 100 Elemente halten kann, muss in diesem Fall bei der Instanzierung des Zwischenobjekts, auf das die Variable **stackcontent** verweist, mittels eines entsprechenden New-Ausdrucks angegeben werden. Diese Instanzierung hatten wir jedoch oben unterschlagen; wo und wie sie durchgefuhrt wird, wird Gegenstand des nachsten Kapitels sein, wenn es um Konstruktoren und Initialisierung geht.

Eine Alternative zum Instanziieren ist ubrigens das **Klonen**. Beim Klonen

wird ein neues Objekt auf der Basis eines bereits existierenden erzeugt. Der Klon stellt also eine Kopie dar. Beim Klonvorgang ist festzulegen, wie

wiet (tief) das Kopieren gehen soll, also ob nur das Objekt oder auch seine Attributobjekte und die, zu denen es in Beziehung steht (auf die die Instanzvariablen verweisen; s. Kapitel 2 in Kurseinheit 1) kopiert werden sollen. Wahrend in prototypenbasierten objektorientierten Programmiersprachen, die das Konzept der Klasse ja nicht kennen, Klonen die einzige Moglichkeit ist, neue Objekte zu erstellen, mussen bei Programmiersprachen mit Klassen, in denen jedes Objekt Instanz einer Klasse sein muss, Klone in der Regel durch Instanziierung und übertragung der Inhalte der Instanzvariablen erzeugt werden. Da wir hier aber die klassenbasierte Linie verfolgen und auf klassenlose objektorientierte Programmiersprachen nur eingehen, wo dies interessant erscheint, werden wir das Klonen, das in klassenbasierten objektorientierten Programmiersprachen eine untergeordnete Rolle spielt, erst in Abschnitt 14.1 vertiefen.

## 8 Metaklassen

Da in Smalltalk auch eine Klasse ein Objekt ist, kann die Klasse selbst, genau wie alle anderen Objekte, Instanzvariablen und -methoden haben. Aber wo werden diese definiert? Der Analogie der Objekte, die Instanzen der Klasse sind, folgend musste das in der jeweiligen Klasse der Klasse, also der Klasse, von der die Klasse (als Objekt) eine Instanz ist, erfolgen. Und so ist es tatsachlich auch.

zunächst konnte man annehmen, dass alle Klassen Instanzen einer speziellen Klasse, nennen wir sie **Class**, sind. Jede Klasse hatte dann (als Instanz dieser Klasse) die Instanzvariablen und Methoden, die in **Class** definiert sind. Inbesondere hatte jede Klasse dieselbe Menge von Instanzvariablen und Methoden. Dies scheint zunächst auch sinnvoll, den bei den Klassen handelt es sich ja um Objekte derselben Art, namlich einheitlich um Klassen.

Es stellt sich dann die Frage, welche die Instanzvariablen und Methoden, die alle Klassen gleichermassen charakterisieren, sein konnten. Es konnte z. B. jede Klasse eine Instanzvariable haben, die alle von der Klasse instanziierten Objekte enthalt, sowie eine weitere, die diese Objekte zahlt.31 Eine typische Methode jeder Klasse ware z. B. new, die eine neue Instanz dieser Klasse zuruckgibt. Was aber, wenn man weitere Eigenschaften (Instanzvariablen oder Methoden) für eine Klasse haben mochte, die diese nicht mit allen anderen teilt? Was, wenn man eine Methode wie z. B. new für eine Klasse anders definieren will als für andere? Im Fall von **new** z. B. ist es denkbar, dass man sie für bestimmte Klassen so umschreiben mochte, dass die Instanzvariablen der neu erzeugten Instanzen bestimmte Startwerte zugeweisen bekommen (so wie die eine oder andere es vielleicht von den Konstruktoren von C++, Java oder C# schon kennt und wie es beim Beispiel mit **Stack** oben naturlich gewesen ware).

Footnote 31: Tatsächlich gibt es solche Variablen. Sie können ja mal zum Spaß versuchen, sie zu finden.

Tatsächlich hat die Programmierpraxis gezeigt, dass es gunstig ist, wenn jede Klasse (als Instanz) ihre eigenen Instanzvariablen und Methoden besitzt und wenn die Programmiererin diese jeweils frei bestimmen kann, ohne dabei gleichzeitig an andere Klassen denken zu müssen. Um dies zu ermöglichen, muss aber jede Klasse Instanz einer eigenen Klasse sein, in der diese Variablen und Methoden nur für sie angelegt werden können. Und genau das ist in smalltalk der Fall.32

Footnote 32: In früheren Versionen Smalltalks war das übrigens nicht so und Alan Kay, der das Projekt bereits vor der Veroffentlichung von Smalltalk-80 verlassen hatte, ist selbst einer der Größten Krtiker dieser Festlegung. Tatsächlich ist sie, wie Sie noch merken werden, nicht immer ganz leicht zu durchblicken.

Zu jeder Klasse des Smalltalk-Systems gehort namlich genau eine Klasse, von der erstere (und nur diese) eine Instanz ist. Diese zweite Klasse wird **Metaklassenkonzept** in Smalltalksen und ihren Metaklassen besteht, ist es nicht sinnvoll, ihre Benennung den Programmierrinen zu überlassen; sie wird in Smalltalk stets durch den Ausdruck <Klassenname> class, also beispielsweise **Stack** class, bezeichnet. Daraus folgt bereits, dass die Programmiererin die Metaklasse nicht selbst anlegen muss (denn dabei musste sie ja auch einen Namen vergeben) -- sie wird vielmehr automatisch mit angelegt, wenn die Programmiererin eine neue Klasse definiert.

Im Prinzip ist die Definition einer Metaklasse genauso aufgebaut wie die einer normalen Klasse: Sie besteht aus der Angabe einer Menge von be 

[MISSING_PAGE_FAIL:100]

**<Liste von Methodedefinitionen>**

besorgt also nicht nur die Definition der genannten Klasse, sondern gleichzeitig auch die ihrer Metaklasse; es ersetzt damit die zwei zuvor prasentierten getrennten Schemata. Klassenvariablen sind ubrigens relativ zu den Instanzen der Klassen global; sie beginnen deswegen mit einem Grossbuchstaben. Klassenmethoden schreibt man jedoch wie Instanzmethoden klein. Beachten Sie, dass Klassenvariablen nur einmal pro Klasse angelegt werden -- sie sind also für alle Instanzen einer Klasse dieselben.33

Ein Beispiel für eine Klassenvariable ist **DependentsFields** in der Klasse **Deispiel Object** (zu ihrer Verwendung s. Abschnitt 14.3), eins für eine Klassenmethode ist **pi** in der Klasse Float:

**304 pi 305**: **Ai**

Sie retourniert (den Inhalt der) Klassenvariable Pi und ist, da sie eine Klassenmethode ist, allen Instanzen der Klasse Float zugeordnet. Dazu, wie der Wert in **Pi** hineinkommt, s. Abschnitt 8.2.

Wir sehen also, dass die Bezeichnungen _Klassenvariable_ bzw. _-methode_ **Terminologisches** und _Instanzvariable_ bzw. _-methode_ eigentlich nur relative Bedeutung haben, da es sich in beiden Fallen um Variablen und Methoden handelt, die Objekten zugeordnet sind. Da man von Instanzen einer Klasse aus aber auch haufiger auf die Variablen und Methoden ihrer Klassen zugerift, ist es guter Brauch (und vermeidelt umstandliche Formulierungen), stets die langen Bezeichnungen zu fuhren. Zudem gibt es neben Instanz- und Klassenvariablen ja auch noch andere Variablentypen (_formale Parameter_ und _temporare Variablen_), so dass die Verwendung von _,Variable" allein meist mehrdeutig ware. Lediglich bei Methoden hat es sich eingeburgert, anstelle von Instanzmethoden nur von Methoden zu sprechen. Wenn der Kontext nichts anderes nahelegt, können Sie dann immer davon ausgehen, dass Instanzmethoden gemeint sind.

### **Konstruktoren**

Mit Hilfe von Metaklassen lassen sich nun in **SMALITALK** auf naturliche Art und Weise sog. **Konstruktoren** definieren. Ein Konstruktor ist eine Methode, die, auf einer Klasse aufgerufen, eine neue Instanz dieser Klasse zuruckgibt (es handelt sich also aus Sicht der Instanzen der Klasse um eine Klassenmethode). Wir haben bereits zwei Konstruktoren von **SMALITALK**kennengelernt: Sie werden über die Selektoren new (fur Objekte ohne indizierte Instanzvariablen) und new : (fur Objekte mit indizierten Instanzvariablen) aufgerufen. Da Klassen selbst Objekte sind, sind new und new : Instanzmethoden der Klassen. Sie sind in Squeak als

```
386new
387*selfbasicNewinitialize
388new:sizeRequested
389*(selfbasicNew:sizeRequested)initialize
```

implementiert. Dabei sind basicNew und basicNew: ebenfalls Instanzmethoden der Klasse, deren Implementierung allerdings primitiv ist (s. Abschnitt 4.3.7 in Kursenheit 1). Sie geben eine neue Instanz (ein neues Objekt) der Klasse, auf der sie aufgerufen wurden, zuruck. Da durch basicNew und basicNew: alle Instanzvariablen der erzeugten Objekte den Wert nil zugewiesen bekommen, wird auf den neuen Objekten, bevor sie (mittels \({}^{\text{A}}\)) zuruckgegeben werden, noch die Methode initialize aufgerufen, die eine Instanzmethode des neuen Objekts ist und die Instanzvariablen je nach Klasse, in der die Methode definiert ist, anders belegt.

### Initialisierung

Konstruktoren sind in SMALLtalk also Klassenmethoden, die neue Instanzen der jeweiligen Klasse zuruckliefern. Dabei haben zunächst alle Instanzvariablen nach der Erzeugung einer Instanz den Wert nil. Sollen diese Instanzvariablen mit sinnvollen Anfangswerten belegt werden, mussen ihnen diese explizit zugewiesen werden. Man spricht dann von einer **Initialisierung** der Instanz.

Nun sollen nicht immer alle Instanzen einer Klasse gleich initialisiert werden. Es ist daher moglich, für eine Klasse mehrere alternative Konstruktoren (als Klassenmethoden) zu definieren, die die neuen Objekte jeweils unterschiedlich initialisieren. Zwei Beispiele für die Klasse Time sind mit

```
310midnight
311*selfseconds:0
312noon
313*selfseconds:(SecondsInDay/2)
```

gegeben, die jeweils die Klassenmethode (den Konstruktoren) seconds : auf Time (vertreten durch self) aufrufen, die wiederum mittels basicNew eine Instanz von Time erzeugt und anschlie@send initialisiert:

```
314seconds:seconds
315*selfbasicNewticks:(Durationseconds:seconds)ticks
```Dabei ist ticks: eine Instanzmethode der Klasse Time, die auf der (mit basicNew) frisch erzeugten Instanz aufgerufen wird und diese initialisiert:

```
316ticks:anArray
317"ticksisanArray:{days.seconds.nanoSeconds}"
318seconds:=anArrayat:2.
319nanos:=anArrayat:3
```

Parameter der Initialisierung ist hierbei (Duration seconds: seconds) ticks, wobei Duration eine Klasse und seconds: ein Konstruktor dieser Klasse ist.

Da die Instanzvariablen eines Objekts nur für die Instanzen des Objekts selbst zugereifbar sind, kann auch eine Klassenmethode wie new nicht auf se zugereifen. Die Initialisierung muss daher von Instanzmethoden wie ticks: vorgenommen werden, die jedoch nicht der Initialisierung vorbehalten sind, sondern jederzeit auf Instanzen der Klasse aufgerufen werden können. Das ist immer dann ein Problem, wenn auch Instanzvariablen initialisiert werden mussen, deren Existenz nach aussen verborgen werden soll (s. Abschnitt 4.3.4) und die deswegen nicht direkt über Zugriffsmethoden gesetzt werden können sollen. Aus diesem Grund sehen new und new: standardmagig den Aufruf der Methode initialize vor (s. Zeilen 307 und 309 oben), in der alle Initialisierungen vorgenommen werden können, ohne dass etwas über den Aufbau der Instanzen nach aussen verraten wurde. In anderen Sprachen wie beispielsweise C++, Java oder C# sind Konstruktoren daher auch keine Klassenmethoden, sondern haben eine Art Zwitterstatus: Sie werden auf einer Klasse aufgerufen, werden aber wie Instanzmethoden auf der neuen Instanz ausgefuhrt und können somit auch auf die Instanzvariablen der neu erzeugten Instanz zugereifen. Man beachte jedoch, dass die Instanzmethode ticks: kein _Implementationsgeheimnis_ preis gibt: Dass Objekte der Klasse Time die Zeit in Sekunden und Nanosekunden speichern ist an der Methode ticks: nicht zu erkennen.

Vor diesem Hintergrund können wir das Beispiel der zweiten Implemen- tierung von Stack aus Abschnitt 7.2 wieder aufgreifen und die noch feh- lende Initialisierung der Variablen stackcontent und stackcounter nachliefern:

```
316ticks:anArray
317"ticksisanArray:{days.seconds.nanoSeconds}"
318seconds:=anArrayat:2.
319nanos:=anArrayat:3
```

Parameter der Initialisierung ist hierbei (Duration seconds: seconds) ticks, wobei Duration eine Klasse und seconds: ein Konstruktor dieser Klasse ist.

Da die Instanzvariablen eines Objekts nur für die Instanzen des Objekts selbst zugereifbar sind, kann auch eine Klassenmethode wie new nicht auf se zugereifen. Die Initialisierung muss daher von Instanzmethoden wie ticks: vorgenommen werden, die jedoch nicht der Initialisierung vorbehalten sind, sondern jederzeit auf Instanzen der Klasse aufgerufen werden können. Das ist immer dann ein Problem, wenn auch Instanzvariablen initialisiert werden mussen, deren Existenz nach aussen verborgen werden soll (s. Abschnitt 4.3.4) und die deswegen nicht direkt über Zugriffsmethoden gesetzt werden können sollen. Aus diesem Grund sehen new und new: standardmagig den Aufruf der Methode initialize vor (s. Zeilen 307 und 309 oben), in der alle Initialisierungen vorgenommen werden können, ohne dass etwas über den Aufbau der Instanzen nach aussen verraten wurde. In anderen Sprachen wie beispielsweise C++, Java oder C# sind Konstruktoren daher auch keine Klassenmethoden, sondern haben eine Art Zwitterstatus: Sie werden auf einer Klasse aufgerufen, werden aber wie Instanzmethoden auf der neuen Instanz ausgefuhrt und können somit auch auf die Instanzvariablen der neu erzeugten Instanz zugereifen. Man beachte jedoch, dass die Instanzmethode ticks: kein _Implementationsgeheimnis_ preis gibt: Dass Objekte der Klasse Time die Zeit in Sekunden und Nanosekunden speichern ist an der Methode ticks: nicht zu erkennen.

Vor diesem Hintergrund können wir das Beispiel der zweiten Implemen- tierung von Stack aus Abschnitt 7.2 wieder aufgreifen und die noch feh- lende Initialisierung der Variablen stackcontent und stackcounter nachliefern:

```
320new
321"liefertneue,gebrachsfertigeInstanzvonStack"
322"selfbasicNewinitialize
32benamteInstanzvariablen
33stockcontentstackpointer
33nichtzeInstanzmethoden
333initialize
334"setztAnfangswerte"
335stackcontent:=Arraynew:100.
336stackpointer:=0
```* 327A self"kannentfallen"
* 328push:anElement
* 329"legtneuesElementaufStapel"
* 330stackpointer=stackcontentsize
* 331ifTrue:[selferror:'Stackleidervoll']
* 332ifFalse:[stackpointer:=stackpointer+1.
* 333stackcontentat:stackpointerput:anElement]
* 334pop
* 335"entfrentoberstesElementvomStapel"
* 336stackpointer=0
* 337ifTrue:[selferror:'Stackleiderleer']
* 338ifFalse:[stackpointer:=stackpointer-1]
* 339top
* 340"liafertoberstesElementdesStapels"
* 341stackpointer=0
* 342ifTrue:[selferror:'Stackleiderleer']
* 343ifFalse:['stackcontentat:stackpointer]

Man beachte, dass das Zwischenobjekt eine Instanz der Klasse Arrayist, die hier (in Zeile 325) nicht wie noch in Kurseinheit 1 notwendig durch ein Literal, sondern durch eine explizite, programmatische Instanziierung (mittels new:) erzeugt wurde.

Altemativ zu obiger Konstruktion kann die Initialisierung von Instanzvari-

**Lazy initialization**

ablen auch zu einem spateren Zeitpunkt nach der Instanzierung durchgefuhrt werden. Man spricht dann von einer **Lazy initialization** (lazy oder faul deswegen, weil man die Initialisierung solange hinausschiebt, wie irgend moglich). Dazu muss jedoch vor jedem lesenden Zugriff auf die (faul initialisierte) Instanzvariable gepruft werden, ob der Wert der Variable immer noch nil ist -- falls ja, muss er durch den gewunschten Anfangswert (der sonst in der Standardinitialisierungsmethode zu finden ware) ersetzt werden. Um nicht jeden lesenden Zugriff auf die Variable im Programm mit einer entsprechenden Abfrage versehen zu mussen, empfiehlt es sich bei Verwendung von _Lazy initialization_, alle, also auch klasseninterne, Zugriffe auf Instanzvariablen über einen entsprechenden Getter durchzufuhren, der den Inhalt der Variable vor seiner Preisgabe pruft und ggf. erst setzt. Statt

```
34push:anElement
34"legtneuesElementaufStapel"
34stackpointerisNilifTrue:[stackpointer:=0].
34stackcontentisNilifTrue:[stackcontent:=Arraynew:100].
34stackpointer=stackcontentsize
34ifTrue:_
35pop
36"entfrentoberstesElementvomStapel"
37stackpointerisNilifTrue:[stackpointer:=0].
38stackpointer=0
39ifTrue:_
40
41
42
435top
44"liafertoberstesElementdesStapels"* stackpointer isNil ifTrue: [stackpointer := 0].
* stackpointer = 0
* ifTrue: _ ```
* wo bei jeder Verwendung ggf. faul initialisiert wird, wurde man also
* stackpointer
* "lazy: liefert den ggf. zuvor initialisierten Stack pointer"
* stackpointer isNil ifTrue: [stackpointer := 0].
* stackpointer
* stackcontent
* stackcontent
* stackcontent isNil ifTrue: [stackcontent := Array new: 100].
* stackcontent
* stackcontent
* push: anElement
* "legt neues Element auf Stapel"
* self stackpointer = self stackcontent size
* ifTrue: _
```
* "entfent oberstes Element vom Stapel"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "lieferstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "liefert oberstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "lieferstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "lieferstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "lieferstes Element des Stapels"
* self stackpointer = 0
* ifTrue: _ ```
* "lieferstststes Element des Stapels"
* self stackpointer = 0
* ifTrue: _
```

* "begründen Sie, warum eine Kapselung der Lazy initialization durch eine Zugriffsmethode dem Sinn der Standardfinitialisierung per initialize moglicherweise entgegensthett.

Nachdem nun hinlanglich klargeworden sein sollte, welche Moglichkeiten

es zur Initialisierung von Instanzvariablen gibt, bleibt noch die Frage nach

der Initialisierung von Klassenvariablen. Klassenvariablen werden namlich, genau wie Instanzvariablen, standardmassig zu nil initialisiert und soll eine Klassenvariable einen anderen Anfangswert haben (z. B. weil es sich dabei um eine Konstante handelt, die für alle Instanzen der Klasse eine Rolle spielt), dann muss ihr dieser Wert explizit zugewiesen werden. Da Klassen ja Instanzen ihrer Metaklassen sind, diese Metaklassen aber automatisch mit der Erzeugung der Klassen angelegt werden und das Klassendefinitionsschema keine Moglichkeit vorishett, einen Konstruktor für die Metaklasse vorzugeben, muss eine spezielle Klassenmethode (haufig ebenfalls,,initialize" genannt) für die Initialisierung der Klassenvariablen vorgesehen werden. Diese ist dann nach Anlegen der Klasse einmalig aufzurufen. Da das aber leicht vergessen werden kann, ist _Lazy initialization_ für Klassenvariablen eine sinnvolle Alternative. Allerdings stellt sich hier wieder das Problem des direkten Zugriffs auf die (Klassen-)Variable (aus dem Kontext der Klasse selbst und ihrer Instanzen), der in Smalltalk nicht unterbunden werden kann (vgl. Selbsttestaufgabe 8.1).

Schreiben Sie eine Methode new, die dafur sorgt, dass alle mit ihr erzeugten Instanzen in einer Klassenvariable MeineInstanzen gespeichert werden.

### Factory-Methoden

Da in Smalltalk Konstruktoren ganz normale Klassenmethoden sind, sind sie an keine besonderen Konventionen gebunden. Sie mussen also insbesondere nicht ein neues Objekt genau der Klasse, der sie angehoren, zuruckgeben. Dies nutzen die sog. Factory-Methoden aus.

Eine **Factory-Methode** ist eine Methode, die wie ein Konstruktor eine

**Instanzen beliebiger**

als nur der Klasse, zu der die Methode gehort, abhangig macht. Zum Beispiel konnte eine Klasse **Number** eine (Klassen-)Methode fromString: vorsehen, die anhand eines zu analysierenden Strings entweder eine Instanz der Klasse Integer oder eineder Klasse Float zuruckgibt. Die Implementierung solcher Factory-Methoden ist in SMALLtalk leicht moglich; sie unterscheiden sich formal auch überhaupt nicht von Konstruktoren -- es sind einfach alles Klassenmethoden.34

Folgende Klassenmethode der Klasse Number (fur beliebige Zahlen) ist eine Factory-Methode:

```
1388fromString:aString
281"FactoryfurZahlen"
382(aStringincludes:$.)
383ifTrue:[^aStringasFloat]
384ifFalse:[^aStringasInteger]
```

Wenn der Parameter aString einen Dezimalpunkt enthalt, wird eine neue Flie8kommazahl zuruckgegeben (mittels der Methode asFloat, die, in der Klasse String implementiert, eine Instanz der Klasse Float zuruckliefert), sonst eine Ganzzahl.

### Erzeugung von Klassen in Smalltalk

Da Instanzen, für die es keine literale Repräsentation gibt, in SMALLtalk grundsatzlich über Konstruktoren erzeugt werden und jede Klasse Instanz ihrer Metaklasse ist, kann man sich fragen, wie in SMALLtalk eigentlich Klassen erzeugt werden. Die Tatsache, dass es einen Browser mit einer entsprechenden Funktion gibt, reicht als Erklarung hierfur nicht aus. Andererseits kann es auch keine Losung sein, einfach new o. a. an die Metaklasse der Klasse zu senden, da diese ja zunächst noch gar nicht existiert. Es stellt sich hier tatsachlich die sprichwortliche Frage nach der Henne und dem Ei, genauer, wer von beiden zuerst existiren muss.

Dieses Dilemma wird von SMALLtalk intern gelost. Eine Klasse wird in SMALLtalk namlich erzeugt, indem man einer anderen Klasse eine entsprechende Nachricht schickt. Der Protokleintrag der dazugehorigen Methode (je nach System in der Klasse Class oder Behavior zu finden) für Klassen ohne indizierte Instanzvariablen sieht in SQUEAK wie folgt aus:

```
385subclass:tinstanceVariableNames:fclassVariableNames:dpoolDiictionaries:scategory:cat
386"Thisisthestandardinitializationmessageforcreatinganew
387classasasabclassofanexistingclass(thereceiver)."
3889"(ClassBuildernew)
389superclass:self
390subclass:tinstanceVariableNames: f classVariableNames: d poolDictionaries: s category: cat Durch Ausfuhrung dieser Methode wird eine neue Klasse und zugleich ihre Metaklasse angelegt. Dabei kann man dem Kommentar entnehmen, dass die neue Klasse _Subklasse_ des Emptangers (einer Klasse) werden soll. Was das heiStr, wird Gegenstand von Kapitel 11 sein. Hier wenden wir uns lieber der Frage zu, von welchen Klassen die miterzeugten Metaklassen Instanzen sind.

### Die Metaklassenleiter Smalltalks

Es mussen nach der Smalltalk-Philosophie auch Metaklassen (als Objekte) Instanzen von Klassen sein. Da es aber nicht mehr sinnvoll erscheint, jeder Metaklasse eigene Instanzvariablen und Methoden zu geben, ist es nicht notwendig, dass jede Metaklasse (als Klasse) ihre eigene Meta-Metaklasse (als Metaklasse der Klasse) hat. Vielmehr reicht es für die Praxis aus, eine gemeinsame Meta-Metaklasse, von der alle Metaklassen Instanzen sind, vorzusehen. Smalltalk-Benennungspraxis, nach der jede Klasse so heiStr, dass ihre Instanzen als Subjekt den Satz,,ceine Instanz> ist ein <Klassenname> " korrekt erganzen, folgend heiStr diese Klasse Metaclass (da eben alle ihre Instanzen Metaklassen sind).

Es ergibt sich sofort die Frage, von welcher Klasse die Klasse Metaclass

eine Instanz ist -- tatsachlich muss ja nach der Philosophie Smalltalk,

nach der Klassen Objekte und jedes Objekt Instanz einer Klasse ist, auch Metaclass Instanz einer Klasse sein. Um dieses Spiel nicht bis ins Unendliche fortsetzen zu mussen, hat man in SMALLTAK zu einem einfachen Trick gegriffen: Man betrachtet die Klasse von Metaclass, also Metaclass class, selbst nur als einfache Metaklasse (obwohl sie ja eigentlich eine Meta-Meta-Metaklasse ist), die, genau wie alle anderen Metaklassen, Instanz von Metaclass sein muss. Es gilt also für Metaclass

395Metaclass class class == Metaclass

Nachfolgendes Diagramm veranschaulicht die Zusammenhange. Man beachte, dass alle Objekte bis auf die der Ebene 0 gleichzeitig Klassen und Instanzen sind. Der gestrichelte Pfeil bezeichnet ubrigens die lst-eine-Instanz-von-Beziehung (in UML-Notation).

Die theoretisch ambitionierte Leserin wird sofort bemerken, dass der Kunstgriff der Terminierung der lst-eine-Instanz-von-Beziehung es verbietet, Klassen als Mengen von Objekten und deren Instanzen als Elemente dieser Mengen im Sinne von Abschnitt 7.3 zu interpretieren: Sonst ware namlich die zu Metaclass gehorende Menge von Objekten indirekt ein Element von sich selbst, was schlectrdings unmoglich ist. Außer einem etwas faden Beigeschmack hat das jedoch keine praktischen Auswirkungen.

Wir haben es also in Smalltalk mit einem mehrstufigen Zusammenspiel von Klassen und Instanzen zu tun. Auf der untersten Stufe, der Ebene 0, stehen konkrete Objekte, die nicht instanziierbar sind. Diese Objekte reprasentieren in der Regel Dinge aus dem Anwendungsbereich eines Programms, also zum Beispiel konkrete Personen, Dokumente, Adressen etc. Eine Stufe darüber, auf Ebene 1, stehen die Klassen, die die Definition (Instanzvariablen und -methoden) dieser Objekte liefern und anhand derer die Objekte der Ebene 0 (per Instanziierung) erzeugt werden. Diese Klassen reprasentieren die Objekte der Ebene 0 in ihrer Gesamtheit, sie reprasentieren die Konzepte oder Allgemeinbegriffe des Anwendungsbereichs. Zu jeder Klasse der Ebene 1 werden im Laufe des Programms in der Regel mehrere Objekte der Ebene 0 erzeugt -- es besteht also eine 1:\(n\)-Beziehung zwischen ihnen.

Nun sind auch die Klassen der Ebene 1 Objekte und damit selbst Instanzen von Klassen, die eine Stufe hoher, also auf Ebene 2 stehen. Die Klassen der Ebene 2, die Metaklassen, geben die Definition der Klassen vor. Da es nicht sinnvoll ist, von Klassen der Ebene 1 mehrere Exemplare zu haben, die, analog zu den Objekten der Ebene 0, alle über die gleiche Definition verfugen, hat jede Metaklasse genau eine Instanz. Es besteht also eine 1:1-Beziehung zwischen Metaklassen und ihren Instanzen, den Klassen der Ebene 1, die die Objekte der Anwendung beschreiben.

Auf Ebene 3 bekommen alle Metaklassen eine gemeinsame Klasse spendiert, von der sie eine Instanz sind, namlich die Klasse Metaclass. Man beachte, dass hier wieder eine 1:\(n\)-Beziehung vorliegt. Anders als auf Ebene 2, auf der man für die unterschiedlichen Konzepteeiner Anwendung jeweils eine Klasse vorfindet, hat man hier, auf Ebene 3, die Vielfalt auf genau eine Klasse verdichtet. Diese hat dann wieder genau eine Metaklasse.

Das nachfolgende Diagramm zeigt noch einmal die Reduktion durch die ersten vier Stufen. Eine ahnliche Verdichtung über vier Ebenen findet man ubrigens auch beim Information Resource Dictionary System (IRDS) der ISO.

### 8.6 Praktische Bedeutung der Metaklassen für die Programmerung

Dadurch, dass in Smalltalk Klassen Instanzen von Metaklassen sind, die selbst Instanzen einer weiteren Klasse und diese alle zusammen Objekte

**Metaprogrammeris**, ist jedes Smalltalk-Programm, ja das ganze Smalltalk-System,

nichts weiter als ein Objektgeflecht (sieht man einmal von den primitiven Methoden ab). Smalltalk ist damit nicht nur ein Programmiersystem, sondern auch ein **Metaprogrammiersystem** in der Tradition funktionaler und logischer Programmiersprachen wie LISP und Prolog. In der imperativen und objektorientierten Programmiersprachenlandschaft sucht diese Machtigkeit bis heute ihrespleichen.

Fur Sie als Programmireerin, die nicht gleich eine neue Sprache erschaffen will, sind Ebene 2 und 3 sind vor allem dann interessant, wenn Sie sich im Inneren von Smalltalk umsehen oder es vielleicht sogar selbst verändern wollen. Wenn Sie z. B. erreichen wollen, dass beim Anlegen einer neuen Klasse für alle benannten Instanvariablen dieser Klasse automatisch _Zugriffsmethoden_ wie in Abschnitt 4.3.4 definiert werden, dann ist dies leicht moglich, indem Sie an entsprechender Stelle (z. B. in der Klasse Class bzw. **Behavior**, die auf der Ebene der Metaklassen steht und die für das Anlegen neuer Klassen zustandig ist) eine neue Methode zur Klassendefinition einfugen, die die bereits existierenden um die automatische Erzeugung der Zugriffsmethoden erganzt.

**Selbstestestaufgabe 8.3**

Erganzen Sie die Klasse Class um eine Methode zur Anlage neuer Klassen, die für ausgewahlte Instanvariablen automatisch Zugriffsmethoden (Accessoren; einen Setter und einen Getter) zum Methodenkatalog hinzufugt. Teilen sie dazu die bei einer Klassendefinition angegebene Liste der Instanvariablen in zwei auf, von denen die eine ohne, die andere mit Accessoren angelegt wird.

Im Programmieralltag werden Sie das aber nicht tun. Vielmehr beschrankt

**Programmieralltag** sich Ihre Tatigkeit da auf das Anlegen und Andern einfacher Klassen, also solcher, deren Instanzen selbst keine Klassen sind. Die dazu notwendigen Metaklassen erzeugt Smalltalk automatically selbst -- im Klassenbrowser erscheinen sie nur über die Unterscheidung zwischen Instanz- und Klassenvariablen bzw. -methoden.

Generalisierung und Spezialisierung

Es gibt in Smalltalk also eine Hierarchie, die auf dem Konzept der Klassifikation aufbaut. Aufgrund praktischer überlegungen ist diese Hierarchie beschrankt; sie ist mit der Sprachdefinition festgelegt und stellt gewissermanessen einen Teil derselben dar. Konzeptionell ist diese Hierarchie eine _Abstraktionshierarchie_: Von den konkreten Objekten der Ebene 0 geht es über die Allgemeinbegriffe oder Konzepte der Ebene 1 zu den Definitionen dieser Konzepte auf Ebene 2 hin zur Fassung von Definitionen allgemein auf Ebene 3. Mit jeder Stufe mit Ausnahme der mittleren wird die Zahl der Objekte, die unter die darin angesiedelten Konzepte fallen, drastisch reduziert: von Ebene 0 auf Ebene 1 von theoretisch unendlich vielen Objekten einer Anwendungzur Zahl der Anwendungsklassen, von Ebene 2 auf Ebene 3 von der Zahl der Anwendungsklassen zu einer Klasse **Metaclass**. Als Programmiererin bewegen Sie sich jedoch vor allem auf Ebene 1: Sie definieren Anwendungsklassen, von denen zur Laufzeit des Programms die Anwendungsobjekte erzeugt werden. Direkt nutzen Sie also nur eine Abstraktionsstufe für die Programmierung.

### Generalisierung

Nun entspricht, wie eingangs (in Abschnitt 7.1) enwahnt, die Klassifikation sprachlich der _lst-ein-Abstraktionsbeziehung_ zwischen Individuen und ihren Klassen:,,Peter ist ein Mensch",,,Smalltalk ist eine Programmiersprache" usw. sind alles Beispiele für eine Art der Abstraktion, bei der man von einem Individuum zu seinem Allgemeinbegriff übergeht. Es gibt aber noch eine zweite Form der lst-ein-Abstraktion, die sich von der ersten fundamental unterscheidet, die aber ebenfalls eine charakteristische Rolle in der objektorientierten Programmierung spielt: die **Generalisierung**. Sprachlich offenbart sich diese in Satzen wie,,ein Mensch ist ein Saugetier",,,ein Saugetier ist ein Lebewesen" oder,,eine Programmiersprache ist ein Werkzeug". Der Unterschied zur ersten Form der Abstraktion liegt dabei offensichtlich darin, dass hier zwei Allgemeinbegriffe und nicht ein Individuum und ein Allgemeinbegriffe miteinander ins Verhaltnis gesetzt werden. Ein weiterer, etwas subtilerer, aber sehr wesentlicher Unterschied ist der, dass die Klassifikation nicht transitiv ist, die Generalisierung hingegen schon. So folgt aus,,ein Mensch ist ein Saugetier" und,,ein Saugetier ist ein Lebewesen" wohl,,ein Mensch ist ein Lebewesen", aber aus,,Peter ist ein Mensch" und,,Mensch ist eine Art" nicht,,Peter ist eine Art".

**Selbstestestaufgabe 9.1**

Ord nen Sie der nachfolgenden Sequenz von lst-ein-Satzen die jeweilige Form der Abstraktion zu:

1. Clyde ist ein Elefant.

2. Elefant ist ein Saugetier.

3. Saugetier ist ein Wirbeltier.

4. Wirbeltier ist ein Stamm.

5. Stamm ist ein Taxon.

[MISSING_PAGE_FAIL:112]

herausfaktorisieren, deren Definition, als Ergebnis der Generalisierung der Klassen Mensch und Vogel, genau die gemeinsamen Eigenschaften (Instanzvariablen und Methoden) enthalt.

Da die Eigenschaften, die einer Generalisierung als Klasse zugeordnet

**Okonomie der Generalisierung**

sind, per Definition automatisch auch für alle Klassen, von denen die Generalisierung abstrahiert, gelten (denn das war ja die Bedingung für die Konstruktion der Generalisierung), brauchen diese die Eigenschaften nicht zu wiederholen, sondem stattdessen nur noch ihre Generalisierung anzugeben. Diese Klassen mussen dann nur noch die Unterschiede, die sie von Zweibeiner sowie von einander unterscheiden, definieren:

\begin{tabular}{l l} \hline \hline Klassen & Mensch \\ Generalisierung & Zweibeiner \\
2 & benannte Instanzvariablen \\  & verstand \\  & nichtare lestanzvariablen \\  & nein \\  & nistanzmethoden \\ \hline \hline \end{tabular}

Diese zweite Form der Abstraktion, die Generalisierung, ist also genau wie die Klassifikation Bestandteil der klassenbasierten objektorientierten Programmierung. Anders als bei der Klassifikation ist bei der Generalisierung aber die Hohe der Abstraktionshierarchie nicht durch praktische überlegungen beschrankt, sondern kann von der Programmiererin nach Belieben angelegt werden. Sprachphilosophisch sind Generalisierungen namlich genau wie Klassen Allgemeinbegriffe; sie sind nur noch allgemeiner. Generalisierungen können somit selbst Generalisierungen haben und so weiter; wie sich das für eine Abstraktionshierarchie gehort, werden die Definitionen, die _Intensionen_, dabei immer knapper. Gleichzeitig wachstjedoch die _Extension_ (das bereits in Abschnitt 7.1 enwahnte Prinzip vom inversen Zusammenhang der beiden).

Abgeschaut ist das Prinzip der Generalisierung übergens von _Aristoteles_'

Prinzip von _Genus et differentia_, der gemeinsamen Abstammung und den

Unterschieden: Das Genus ist die nachst allgemeinere Kategorie, unter die Objekte der zu generaliserenden Klassen (der Spezies) auch fallen, und die Differentia sind die Kriterien, nach denen sich die Objekte aufgrund ihrer Natur, wie sie in den verschiedenen Klassende-

Wikipedia

finitionen festgelegt (und nicht etwa durch spezielle Werte von Instanzvariablen bestimmt) ist, unterscheiden. So haben eben die Klassen _Mensch_ und _Vogel_ das gemeinsame Genus _Zweibeiner_ als (biologisch nicht ganz korrekte) Generalisierung: In ihr ist festgelegt, dass alle Exemplare von Zweibeinern (und damit auch von Menschen und Vogel) ein links und ein rechtes Bein sowie einen Aufenthaltsort haben. Die Unterschiede (Differentia) sind dann in den jeweiligen Klassen herausgearbeitet. Man beachte, dass Genera keine eigenen Individuen haben, also keine Individuen, die nicht Individuen einer ihrer Spezies waren. So gibt es keine Zweibeiner, die nicht entweder Mensch oder Vogel waren.35

Footnote 35: Biologinnen möchten vielleicht Mensch durch Primatin ersetzen.

Genau wie die Klassifikation hat das Ordnungsprinzip der Generalisierung

**mengentheoretische**

eine einfache mengentheoretische Interpretation. Dennach enthalt die

**Interpretation**

Menge der Instanzen einer Generalisierung alle Instanzen der Klassen, von denen sie eine Generalisierung ist. Wenn also **Mensch** und **Vogel** Ausgangsklassen einer Generalisierung

**Zweibeiner** sind, dann ist die Menge der Instanzen, die Zweibeiner reprasentiert (fur die Zweibeiner den Allgemeinbegriff abgibt) eine Obermenge der Vereinigung der Menge der Instanzen von **Mensch** und **Vogel**. Die Menge der Instanzen von **Zweibeiner** ist eine echte Obermenge, wenn **Zweibeiner** auch noch eigene Instanzen hat (also Instanzen, die nicht Instanzen von **Mensch** und **Vogel** sind; im Kontext der Instanziierung wurde man von _direkten Instanzen_ sprechen; s. Abschnitt 7.3); sonst ist sie nur eine unechte Obermenge (also genau gleich der Vereinigung). Die nachfolgende Grafik zeigt den Zusammenhang (wobei die schwarzen Punkte die Instanzen und die Ellipsen die Klassen darstellen sollen). Gute Pravis (und hier angedeutet) ist, wenn Generalisierungen keine eigenen, direkten Instanzen haben, also Genera im obigen Sinne sind. Dies ist in der objektorientierten Pravis aber (leider) langst nicht immer selbstverstandlich, wie sich im nachsten Kapitel noch zeigen wird (vgl. dazu auch Kapitel 69 in Kurseinheit 7).

Die mengentheoretische Interpretation von Generalisierung als Obermengenbildung legt nahe, dass Instanzen von **Mensch** und **Vogel** (als Elemente der entsprechenden Extensionen) auch Instanzen von **Zweibeiner** sind. Wenn man das so sehen will, dann sollte man aber zur notwendigen Unterscheidung von **indirekten Instanzen** (anstelle von _direkten Instanzen_; s. Abschnitt 7.3) sprechen.

Bei der Generalisierung können also Eigenschaften, die verschiedene, aber ahnliche Klassen unterscheiden, weggelassen (_wegabstrahiert") werden. Das Weglassen ist aber nicht die einzig mogliche Form der Generalisierung: Es können auch Eigenschaften generalisiert werden, wobei dann der Begriff der Generalisierung rekursiv zur Anwendung kommt. Dabei versteht man unter der Generalisierung von Attributen (oder allgemeiner von Instanvariablen; s. Abschnitt 2.4), dass ihr Wertebereich von einem spezielleren (kleineren) zu einem allgemeineren (grosseren) aufgeweitet wird. So wurde beispielsweise das Attribut **aufenthalstort**, das mit (Instanzen der) Klasse **Mensch** assoziiert ist, beim **übergang zur Generalisierung Zweibeiner** von Punkten auf der Erdoberflache zu Punkten einschliesslich des Luftraums darüber generalisiert, so dass es auch den Wertebereich für Vogel abbeckt. In **SMALLtalk** gibt es aber keine Moglichkeit, Attributen per Deklaration Wertebereiche zuzuordnen; wie Sie noch sehen werden, erlauben zudem aus gutem Grund die wenigsten Programmiersprachen, die die Moglichkeit der Wertebeschrankung von Variablen vorsehen, Attributwertebereiche bei der Generalisierung ebenfalls zu generalisierten (die sog. _kovariante Redefinition_; s. dazu auch die Kapitel 25 und Abschnitt 26.3 in Kurseinheit 3).

Auch wenn bislang so getan wurde, also sei die Generalisierung etwas in der Natur des betrachteten Gegenstandes liegendes, so gibt es in der Praxis jedoch oftmals verschiedene Gesichtspunkte, nach denen man Generalisierungen durchfuhren kann. So ist z. B. die Generalisierung von **Vogel** bzw. Mensch zu **Zweibeiner** nicht die einzig mogliche (und sicher nicht die einzig sinnvolle). Es konnte also durchaus sein, dass man mehrere, voneinander unabhangige Generalisierungshierachien konstrueren mochte, in denen durchaus dieselben Klassen auftauchen. In der Praxis verliert man dadurch jedoch die strikte Hierarchieform der Generalisierung (da sich mehrere Hierarchien überlagern), es sei denn, man erlaubt, verschiedene Arten der Generalisierung voneinander zu unterscheiden. Beides bringt jedoch einiges an Komplikationen mit sich, so dass wir hier auf,,Mehrfachgeneralisierungen" nicht eingehen werden.

### 9.2 Spezialisierung

Ahnlich wie bei der Klassifikation kann man das Prinzip der Generalisierung umkehren. Man redet dann von der **Spezialisierung**. Wahrend die Generalisierung Eigenschaften weglassst oder generalisiert (Abstraktion), fugt die Spezialisierung Eigenschaften hinzu oder spezialisiert bereits vorhandene. Man kann also von jeder Klasse sagen, dass sie eine Spezialisierung ihrer Generalisierungen ist (so sie denn welche hat).

Dass eine Generalisierung bereits über Spezialisierungen verfugt, hindert

\begin{tabular}{c c c}  & **Spezialisierung von** \\ eine nicht daran, neue hinzuzufugen. So ist es beispielsweise im obigen & **Generalisierungen** \\ Beispiel von **Zweibeiner** denkbar, dass man im Nachhinein noch **Menschenaffe** & als Spezialisierung erganzt. Als Differentia kame z. B. eine Methode hangeln in Frage, die **Mensch** und **Vogel** fehlt. Sie zu erganzen stellt überhaupt kein Problem dar -- ja es ist sogar eine der grossten Errungenschaften der objektorientierten Programmierung, dass solche Programmerweiterungen modular, also ohne andere Teile des Programms zu betreffen, immer moglich sind. Mehr dazu in Kapitel 26 in Kurseinheit 3. \\ \end{tabular}

Leider ist es in der Programmierpraxis nicht immer ganz so einfach. Vielmehr findet man haufig Klassen (bzw. Instanzen) vor, die ungefahr das **Generalisierungen**, was man mochte, und denen man nur noch ein wenig hinzufugen **mochte**. Man mochte dann von einer Klasse spezialisieren, die selbst keine Generalisierung im obigen Sinne ist. Um beim obigen Beispiel mit Menschen und Vogeln zu bleiben, konnte man beispielsweise auf den Gedanken kommen, Pinguine als Spezialisierung von Vogeln einzufuhren:

Es ist nun fraglich, ob damit auch **Vogel** zu einer Generalisierung von **Pinguin** wird. Die Tatsache, dass **Vogel** eigene, _direkte_ Instanzen hat, spricht schon einmal dagegen (auch wenn der Begriff der Generalisierung landlaufig nicht so streng gefasst wird). Weiterhin kann man sich fragen, was man von der Intension von **Pinguin** weglassen musste, um zur Intension von **Vogel** zu gelangen. Dies konnte z. B. schwimmeNach: sein. Spatestens dann fallt einer jedoch auf, dass Pinguine gar nicht fliegen können, also die Intension von **Vogel** die Methode **fliegeNach:** gar nicht enthalten durfte, wenn **Vogel** eine Generalisierung von **Pinguin** sein sollte. Dieses Problem, das in der Praxis standig vorkommt, lasst sich auf elegante Weise dadurch losen, dass man eine Klasse **NichtPinguin** parallel zu **Pinguin**spezialisiert und alle eigenschaften, die andere V\(\ddot{\text{o}}\)gel von Pinguinen unterscheidet (wie z. B. fliiegeAn:), dort hineinpackt.

\begin{tabular}{c c}  & **Spezialisierung darf** \\ \end{tabular}

\begin{tabular}{c c}  & **Spezialisierung darf** \\ \end{tabular}

\begin{tabular}{c c}  & **mokhent** \\ \end{tabular}

## 10 Vererbung und abstrakte Klassen

Generalisierung und Spezialisierung wie oben dargestellt sind eher theoretisch motivierte Konzepte. In der Programmierung geht man jedoch haufig, wie im obigen Beispiel von Pinguinen schon angedeuttet, an praktischen Gesichspunkten orientiert vor. So haben denn auch nicht Generalisierung und Spezialisierung die Entwicklung objektorientierter Programmiersprachen gepragt, sondern _abstrakte Klassen_ und _Vererbung_. Diese pragmatische Orientierung ist jedoch nicht ohne Probleme und so werden uns die Oberlegungen zu Generalisierung und Spezialisierung spatestens in Kurseinheit 3 wieder begegnen.

### Vererbung

Unter **Vererbung** versteht man in der objektorientierten Programmierung die übertragung der Definition von Eigenschaften und Verhalten (Intension) von einer Klasse auf eine andere. Vererbung dient vor allem der Wiederverwendung von Code und damit der Okonomie in der Softwareentwicklung.

Wenn man das Prinzip von Generalisierung und Spezialisierung vor Augen hat, dann ist die Vererbung eigentlich nur noch ein Mechanismus, der Definitionen von einer Klasse auf eine andere übertragt. So wird jede benannte Instanzvariable, die in einer Generalisierung deklariert ist, nicht nur für Instanzen dieser Generalisierung (so sie denn welche hat) angelegt, sondern auch für die Instanzen all ihrer Spezialisierungen. Analog stehen Methoden, die in einer Generalisierung definiert werden, auch ihren Spezialisierungen zur Verfugung, und zwar beinhae so, als waren sie in den Spezialisierungen definiert.

Spezialisierung und Vererbung scheinen also Hand in Hand zu gehen. Doch ist dies nur solange der Fall, wie man von der Spezialisierung ausgeht und die Vererbung als okonomisches Abfallprodukt erhalt. In der Praxis lasst man sich doch leider haufig von vordergrundigen Gewinnenwartungen leiten und folgt der (vermentitlichen) Okonomie der Vererbung, ohne dabei auf die Prinzipien von Generalisierung und Spezialisierung einzugehen. Obiges Beispiel von Pinguinen und Vogeln hatte schon gezeigt, zu welchen Komplikationen eine unbedachte Spezialisierung fuhren kann; nachfolgendes soll zeigen, zu was eine Fixierung auf Ausnutzung der Vererbung fuhrt.

Ein Klasse Quadrat sei etwa wie folgt definiert:

\begin{tabular}{l|l} \hline Klasse & Quadrat \\ \hline benannte Instanzvariable & laenge \\ \hline nistanzmethoden & \\ \hline
415 & flaeche \\
416 & laenge \(\star\) laenge \\ \hline \end{tabular}

[MISSING_PAGE_FAIL:119]

ist. Sie lasst dabei insbesondere den Zusammenhang der Extensionen der beteliligten Klassen, der für Generalisierung/Spezialisierung wesentlich ist, ausser acht. Diese Ignoranz hat aber weitreichende Konsequenzen, die wir in Kapitel 26 von Kurseinheit 3 noch kennenlernen werden.

Man hatte nun auch umgekehrt verfahren und dabei das Prinzip von Generalisierung und Spezialisierung hochhalten können, indem man

**Umkehrung der Verebrungsrichtung**.

**Quadrat** von **Rechteck** erben lasst (wenn man akzeptiert, dass die Generalisierung

**Rechteck** eigene Instanzen hat). Der Nachteil dieses Entwurfs ware jedoch, dass dann auch

**Quadrat** zwei Instanzvariablen für Seitenlangen hatte, obwohl ja eine ausgereicht hatte. Auf der anderen Seite hatte man die Methoden für Flache und Umfang nicht überschreiben mussen, denn wenn **laenge** und **breite** gleich sind, unterscheiden sich die beiden obigen Implementierungen von flaeche und umfang im Ergebnis nicht. Man muss nur sicherstellen, dass in Instanzen von Quadrat laenge und **breite** tatsachlich immer gleiche Werte haben.

Nun kann man aber auch auf die Idee kommen, die zu viel geerbte Instanzvariable **breite** einfach wieder zu loschen. Tatsachlich ist dies vom

**Geerbtem**.

Standpunkt der Verebrung aus kein Problem: Genauso, wie man Teile der Definition überscheiben kann, kann man sie auch loschen. Im konkreten Fall der Klasse Quadrat, die von

**Rechteck** erbt, musste man mit dem Loschen von **breite** aber auch die Methoden

**flaeche** und **umfang** überschreiben. (Das Loschen von Methoden ware auch moglich, wird hier aber nicht gebraucht.)

Was bleibt, ist ein Eindruck von Beliebigkeit bei der Verebrungsrichtung,

**Außen- und die für Generalisierung/Spezialisierung nicht existiert. In gewisser Weise**

**Innesicht**. Spiegeln Generalisierung/Spezialisierung und Verebrung auch zwei verschiedene Weltschten wider: Generalisierung/Spezialisierung steht für die Ordnung eines Systems von Klassen mit Blick _von aussen_ und für das Ganze (die sog. _Client-Schnitstelle_), Verebrung für die Pragmatik des Programmierens mit Blick _von innen_ und einem Fokus auf Wiederverwendung (die _Verebrungsschnitstelle_). Verebrung stellt eine Art genetischen Zusammenhang zwischen Klassen dar, der deren Entstehung aus Vorhandenem widerspiegelt, Generalisierung/Spezialisierung eher eine abstrakte Ordnung. Verebrung bringt Komplexitat in ein System, Generalisierung/Spezialisierung versucht, sie durch Strukturierung zu reduzieren. Wie Sie gesehen haben, fuhren beide Sichten nicht automatisch zum selben Ergebnis; sie zu vereinen ist die hohe Kunst des objektorientierten Entwurfs.

### 10.2 Verebrung in prototypenbasierten Sprachen

In der klassenbasierten Form der objektorientierten Programmierung ist die Verebrung an Klassen gebunden: Selbst wenn sich die Definitionen eigentlich auf die Instanzen der Klassen beziehen, so ist es doch die Klasse, die Teile ihrer Definition (Intension) von anderen erbt. Im Gegensatz dazu ist die Verebrung in prototypenbasierten objektorientierten Programmiersprachen, in denen es ja keine Klassen gibt, vollstandig zwischen Objekten definiert: Jedes Objekt gibt eines oder mehrere andere an, deren Eigenschaften und Verhalten es übernimmt. Dabei kann es gewrte Teile der Definition überschreiben und auch loschen.

Auf den ersten Blick scheint es so, als sei dies sogar der naturlichere Weg der Vererbung: Schliesslich findet in der Natur Vererbung ja auch ausschliesslich zwischen Individuen statt, ja genaugenommen gibt es so etwas wie biologische Klassen (Arten etc.) in der Natur überhaupt nicht36, denn es differenzieren sich standig einzelne,,Arten" zu neuen und es ist nicht ausgeschlossen, dass einmal ausdifferenzierte Arten irgendwann wieder verschmelzen. Abgesehen davon ist, wie bereits in Kapitel 7 enwahnt, die reale Existenz von Allgemeinbegriffen strittig (der _Universalienstreit_).

Footnote 36: 5o ist zwar die Definition einer Art als diejenige biologische Kategorie, deren Exemplare (Individuen) unteinander fortpflanzungsfahige Nachkommen zeugen können, sinnvoll, doch unterliegen derart angelegte Artendefinitionen dem erdgeschichtlichen Wandel, wie sich schon daraus ableiten lasst, dass alleben aus den ersten Einzellem entstanden ist.

Man kann dem freilich entgegenhalten, dass man als Programmiererin ja auch keine einzelnen Objekte, sondern Klassen entwirft, die damit die eigentliche,,Schopfung" der objektorientierten Welfsicht abgeben. Auch sind objektorientierte Programme nicht für die Ewigkeit gemacht, sondern unterliegen der standigen Anpassung, eben der Evolution, und somit sind auch Klassendefinitionen im standigen Wandel. Eine übertragung der Vererbung auf Klassen ist also nicht vollkommen unnaturlich.

Nicht zuletzt muss man auch erkennen, dass viele Anwendungsdomanen, für die programmiert wird, aus massenhaft gleichen Objekten bestehen, die durch den klassenbasierten Ansatz besser abgedeckt werden als durch den prototypenbasierten (vgl. die entsprechenden Kommentare zur Klassifikation in Abschnitt 7.1). Und so macht denn auch die Vererbung unter Instanzen das Nachvollziehen (und Debuggen) eines Programms eher noch schwieriger als die Vererbung unter Klassen ohnehin schon (s. Kapitel 56 in Kurseinheit 6).

### Abstrakte Klassen

Die Genera Aristoteles' sind allesamt abstrakt -- es gibt keine Saugetiere, die nicht Mensch oder Hund oder Katze oder was Konkretes auch immer waren. übertragen auf die objektorientierte Programmierung hi Bese das: Generalisierungen, also Klassen, die aus Generalisierungen hervorgegangen sind, haben selbst keine Instanzen, sind also insbesondere nicht _instanziierbar_.

In der objektorientierten Programmierung nennt man nicht instanziier-

**abstrakte und** bare Klassen **abstrakt**. Der Grund für die mangelnde Instanziierbarkeit

**konkrete Klassen**

[MISSING_PAGE_FAIL:122]

[MISSING_PAGE_FAIL:123]

Man mag sich fragen, warum es eine _abstrakte Klasse_ wie **Collection** überhaupt gibt, wenn sie doch keine Instanzen haben soll.40 Bereits das objige Beispiel gibt eine erste Antwort: Weil es auch in abstrakten Klassen Methoden gibt, die voll ausimplementiert sind (z. B. **addAll:**) und die dann in den Subklassen, auf die sie verebt werden, nicht wiederholt werden mussen. Tatsachlich ist alles, was eine erbende Klasse tun muss, um in den Genuss einer funktionierenden Methode **addAll:** zu kommen, eine Implementierung von **add:** zu liefern. Die abstrakte Klasse faktorisiert also die Genneinsamkeiten mehrerer Klassen heraus und markiert gleichzeitig, was ihre erbenden Klassen noch nachtragen mussen: Alle Methoden, die von anderen Methoden der Klasse aufgerufen werden (wie eben **add:** von **addAll:**), die aber (z. B. mangels Instanvariablen wie im Fall von **Collection**) in der Klasse noch nicht implementiert werden können, deren Aufruf auf Instanzen der abstrakten Klassen somit einen entsprechenden Fehler liefern wurde.

Der Aufruf einer abstrakten, d. h. in der Klasse nicht implementierten Methode aus der Klasse selbst heraus wie in Zeile 430 (mit self als Empfanger) ist ein gangiges Muster der objektorientierten Programmierung. Man nennt es auch **offene Rekursion** (engl. open recursion), da der Aufruf auf dem Objekt selbst erfolgt (also gewissermansen rekursiv ist), aber an der aufrufenden Stelle noch nicht klar (offen) ist, welche (erbende) Klasse die Implementierung liefert. Dieses Muster, auf das wir in Abschnitt 12.1 im Rahmen des dynamischen Bindens noch einmal zuruckkommen werden, lasst sich auch einsetzen, um das oben beschriebene Dilemma von **Quadrat** und **Rechteck** aufzulosen:

\begin{tabular}{l|l} \hline \hline BASE & **Rechteck** \\ \hline benannte Instanzvariablen \\ \hline
432laenge \\
433*self implementedBySubclass \\
434breite \\
435*self implementedBySubclass \\
436flaeche \\
437*selflaenge*selfbreite \\
438umfang \\
439*selflaenge+selfbreite*2 \\ \hline \hline \end{tabular}

Die Definitionen von Quadrat und **Rechteck** fallen dann knapp aus und kommen ohne inhaltliche Veränderungen daher (lediglich die noch nicht implementierten Methoden mussen nachgeliefert werden):

\begin{tabular}{l|l} \hline \hline BASE & **Quadrat** \\ \hline \hline \end{tabular}

[MISSING_PAGE_EMPTY:125]

von einer **direkten Superklasse**, wenn es keine weitere Klasse gibt, die in der Subklassenbeziehung dazwischen steht. Die Subklassenbeziehung ist (anders als die Subtyppenbeziehung; vgl. Kapitel 26) nicht reflexiv (irreflexiv) -- eine Klasse kann also keine Subklasse von sich selbst sein.

### Bedeutung der Subklassenbeziehung

Die Bedeutung der Subklassenbeziehung variiert von Sprache zu Sprache. Wie Sie sich vielleicht schon gedacht haben, kann man die Subklassenbeziehung mit der Spezialisierungsbeziehung gleichsetzen oder auch mit der Vererbung; es sind aber auch noch andere Definitionen moglich. Tatsachlich wird die hier als Subklassenbeziehung eingefuhrte Beziehung zwischen Klassen auch gar nicht immer so genannt; entsprechend heissen dann die Rollen auch nicht Sub- und Superklasse, sondern z. B. **abgeleitete Klassen** und **Basisklassen**. Im Englischen sind hierfur neben _Derived class_ und _Base class_ auch die Begriffe _Child class_ bzw. _Parent class_ in Gebrauch.

In Smalltalk wird die Subklassenbeziehung mit der Vererbungsbeziehung gleichgesetzt. Eine Subklasse erbt demnach alle Instanzvariablen in Smalltalk und Methoden ihrer Superklasse. Dass sie darüber hinaus auch noch ihre Klassenvariablen und -methoden erbt, ist nicht selbstverstandlich; dies wird in Abschnitt 11.4 noch genauer beleuchtet. Wichtig ist hier, festzuhalten, dass durch eine existierende Subklassenbeziehung zwischen zwei Klassen nicht ausgedruckt wird, dass die Subklasse eine Spezialisierung der Superklasse ist oder gar die Superklasse eine Generalisierung der Subklasse. Dies sicherzu-stellen obliegt der Verentwortung der Programmiererin.

Jede neue Klasse, die in einem Smalltalk-System angelegt wird, muss direkte Subklasse genau einer Klasse sein -- es ist deshalb notwendig, dass beim Erzeugen einer neuen Klasse die Superklasse mit angegeben wird. Da wie bereits mehrfach erwahnt die Smalltalk-Programmierung nicht dateibasiert ist, sondern mittels eines dafur vorgesehenen Browsers erfolgt, gibt es zum Zweck der Angabe der Superklasse auch kein spezielles Schlussewort wie beispielsweise **extends**, das die Subklassenbeziehung ausdruckt: Man legt vielmehr eine neue Klasse an, indem man ihrer Superklasse eine entsprechende Nachricht schickt. Eine dazugehorige Methode hatten Sie bereits in Abschnitt 8.4 gesehen.

Damit eine Subklassenbeziehung zwischen zwei Klassen zulassig ist, muss deren Definitionen bestimmte Bedingungen einhalten. In Smalltalk **Sublassenbeziehung**, dass die nicht dieselben Namen haben durfen wie Variablen, die bereits in (direkten oder indirekten) Superklassen deklariert wurden. für indizierte Instanzvariablen gilt, dass wenn die Superklasse solche hat, sie auch die Subklasse haben muss. Methodedefinitionen hingegen, die dieselbe _Methodensignatur_ verwenden, überschreiben einfach die geberten Methoden. Entsprechende Regeln sind in anderen Programmiersprachen zum Teil erheblich komplexer.

Da die Subklassenbeziehung auch in Smalltalk nicht reflexiv ist, muss es **die Klasse Object** mindestens eine Klasse geben, die keine Subklasse ist (und entsprechend keine Superklasse hat). Es ist die Klasse Object, die oberste aller Superklassen. In ihr sind die Definitionen angelegt, die den Instanzen aller Klassen zugutekommen sollen (also z. B. die Methode printString). Diese Methoden werden per Vererbung auf alle anderen Klassen übertragen, wodurch sie deren Instanzen zur Verfugung stehen. Eine ganze Reihe nutzlicher Methoden, die in Object definiert sind, werden wir in Kapitel 14 kennenlernen.

### Mechanisms der Vererbung von Superklassen auf Subklassen

Es stellt sich die Frage, wie der Mechanisms der Vererbung genau umgesetzt wird. Eine Moglichkeit ware z. B., die Definition einer Superklasse per Kopieren und Einfugen auf ihre Subklassen zu übertragen. Das ware zwar moglich und wurde auch die Semantik der Vererbung korrekt wiedergeben, wurde aber das (technische) Problem mit sich bringen, dass bei einer Anderung einer Superklasse auch alle ihre Subklassen mit geandert werden musseten.

Eine weitere Moglichkeit ware, für jede Instanz einer Subklasse automatisch je eine Instanz aller ihrer Superklassen mit z erzeugen und diese Instanzen zu einer zu vereinen. Diese Umsetzung der Vererbung steht jedoch mit dem Konzept der Identifat von Objekten in Konflikt: Ein Objekt einer Subklasse hatte auf einmal mehrere identiaten, und zwar eine für sich selbst und eine pro Superklasse, von der sie erbt. Auch das ware problematisch.

Stattdessen wird die Vererbung in Smalltalk und vielen anderen objekt-orientierten Programmiersprachen als ein Aufteilen der Klassendefinitionen realisiert: Vereinbarungen, die in einer Klasse getroffen wurden, gelten automatisch auch für alle Subklassen, es sei denn, diese spezifizieren etwas anderes. Dabei werden die Vereinbarungen nicht übertragen (wie per Kopieren und Einfugen), sondern einfach nur mitbenutzt.

### Loschen von Methoden

Wie bereits in Abschnitt 10.3 erwahnt, wird die Programmireerin, die eine abstrakte, weil unvollstandige, Klasse instanziert, irgendwann damit bestraft, dass das Versenden einer Nachricht an die entsprechende Instanz zu einer Fehlemeldung fuhrt, die ihr (per subclassResponsibility oder implementedBySubclass, die, genau wie doesNotUnderstand.; in der Klasse Object definiert ist) anzeigt, dass die Methode (erst) in einer Subklasse implementiert werden sollte. Dummenweise bekommt die Programmirerin diesen Hinweis erst zur Laufzeit des Programms zu Gesicht, also dann, wenn es schon zu spat ist (es sei denn, man testet gerade). Man erkennt hieran sehr schon den interaktiven Geist des Smalltalk-Systems, insbesondere die Philosophie, nach der Programmieren nichtsweiter ist als das iterative Zurechtbiegen und Erweitern eines bereits bestehenden, funktion-nierenden Systems. Man muss eine Weile damit gespieht haben, um diesem Charme zu erliegen.

**Selbsttestaufgabe 11.1 (fur Java-Fans)**

überschreiben Sie die Methode doesNotUnderstand : so, dass man beim Versenden einer Nachricht an nil eine Meldung. Null pointer exception" erhalt. Achtung: Speichern Sie vorher unbedingt lhr Image und stellen Sie es nach der Bearbeitung der Aufgabe wieder her!

Wenn man sich erst einmal damit abgefunden hat, dass man als Programmireerin Methoden schreibt, die ausschliesslich dem Zweck dienen, sich

**überschreiben selbst oder eine Kollegin auf Programmierfehler hinzuweisen, dann erscheint einem eine weitere Smalltalk-Konvention geradezu als elegant, namlich die, geerbte Methoden durch überschreiben auszuloschen. Tatsachlich ist genau hierfur eine weitere Methode in der Klasse Object mit Namen,,shouldNotImplement" vorgesehen, die zu einer entsprechenden Fehlermeldung fuhrt. Eine Klasse, die also eine geerbte Methode loschen mochte, überschreibt diese einfach mit**

**448 self shouldNotImplement**

im Rumpf. Bevor Sie jetzt als disziplinierte Programmiererin den Stab über Smalltalk brechen, erlauben Sie noch den Hinweis, dass der Wunsch, geerbte Methoden zu loschen, direkte Folge der vorrangigen Orientierung an Verebung ist, die bereits oben kritisert wurde: Ware die Superklasse auf Grundlage des Prinzips der Generalisierung ausgewahlt worden, kame man gar nicht in die Verlegenheit, Methoden loschen zu wollen, denn alles, was für die Generalisierung sinnvoll ist, ist grundsatzlich auch für ihre Spezialisierungen sinnvoll, oder die Generalisierung ist keine Generalisierung. Ausserdem haben Sie auch in Sprachen mit starker Typprufung, in denen das Loschen von Methoden nicht moglich ist, als Programmiererin immer die Freiheit, eine Methode so zu überschreiben, dass sie garantiert nichts tut, was mit der Idee der Klasse, von der sie erbelt ist, in Einklang zu bringen ware. Auch hier waren Laufzeitfehler die unvermeidbare Folge. Mehr dazu im Kurseinheit 3; hier sei nur soviel bemerkt wie, dass wenn man sich bei der Organisation seiner Klassenhierarchie auf das Prinzip der Generalisierung stutzt, dass man dann auch nicht in die Verlegenheit kommt, Methoden loschen zu wollen.

### Subklassenhierarchie und Verebung unter Metaklassen

Verebung ist nicht auf die Klassen der Ebene 1 beschrankt -- es können in Smalltalk vielmehr auch Metaklassen, die ja ebenfalls Klassen sind (s. Kapitel 8), voneinander erben. Da Metaklassen aber bei der Erzeugung von Klassen automatisch angelegt werden (und auch keine eigenen Namen haben), hat die Programmiererin auch keinen direkten Einfluss auf die Verebungshierarchie der Metaklassen. Vielmehr wird diese automatisch parallel zur Vererbungshierarchie der Klassen, die Instanzen der Metaklassen sind, angelegt. Dies hat zurFolge, dass in SMALLtalk neben den Instanzvariablen und -methoden auch die Klassenvariablen und -methoden von einer Klasse auf ihre Subklassen verebt werden.

Da in SMALLtalk jede Klasse direkte oder indirekte Subklasse von Object ist und die Subklassenhierarchie der Metaklassen parallel zu der ihrer Klassen angelegt ist, erbt jede Metaklasse in SMALLtalk automatisch von Object class, der Metaklasse von Object. Was lage also naher, als die Klassenmethoden, die allen Klassen zur Verfugung stehen sollen -- darunter auch die beiden Standard-konstruktoren new und new: -- in Object (genauer: als Instanzmethoden von Object class) zu definieren?

Nun gibt es ja schon, wie bereits in Fussnote 29 oben erwahnt, in SMALLtalk zwei Arten von Objekten, namlich solche, die instanzierbar sind (also Klassen) und solche, die es nicht sind. Darüber hinaus gibt es auch noch eine Unterscheidung zwischen Klassen, die Metaklassen sind, und solchen, die es nicht sind -- bei allen Gemeinsamkeiten von Klassen und Metaklassen muss man z. B. von Klassen neue Subklassen bilden können, von Metaklassen jedoch nicht. Diese Unterscheidungen muss schliesslich irgendwo getroffen werden. Und so kommt es, dass Object class nicht die Wurzel der Verebrungshierarchie der Metaklassen ist (kann sie sowieso nicht, denn auch sie muss eine Subklasse von Object sein!), sondern selbst von einer für diesen Zweck vorgesehenen Klasse erbt. Aus demselben Grund, aus dem die Klasse Object,,Object" und die Klasse Metaclass,,Metaclass" hei8t, hei8t diese Klasse,,Class": Es gilt namlich für jede Instanz dieser Klasse, dass sie eine Klasse ist. Man beachte ubrigens, dass Class, auch wenn sie die Superklasse aller Metaklassen ist, selbst keine Metaklasse ist, denn sont musste Class ja als Superklasse von Object class und wegen der parallelen Verebrungshierarchie von Metaklassen und Klassen die (Meta-)Klasse einer Klasse sein, die Superklasse von Object ist. Ist sie aber nicht. Ausserdem ist, wie man sich leicht überzeugen kann, die Klasse von Class die Klasse Class class und erst Class class eine Metaklasse. Zugegebenermassen etwas kompliziert.

Finden Sie für das SMALLtalk-System lhrer Wahl heraus, wie die Zusammenhange der Klassen Object, Class und Metaclass sowie derer jeweiligen Metaklassen Object class, Class class und Metaclass class sind. Benutzen Sie dazu die Methoden allSuperclasses, allSubclasses und isKindOf: (Um zu testen, ob ein Objekt in einer Autzahlung, wie sie von allSuperclasses und allSubclasses zuruckgeliefert wird, enthalten ist, können sie die Methode includes: verwenden.)

Die Klasse Class steht in der Verebrungshierarchie SMALLtalk s neben der Klasse Metaclass. Gemeinsam erben sie von der Klasse Behavior (in SMALLtalk-80 und direkten Derivaten indirekt, über die Klasse ClassDescription), in der endlich, neben vielen anderen Methoden, new und new: definiert sind. Man beachte, dass diese Methoden als Instanzmethoden deklariert sind; da sie aber in der Verebrungshierarchie SMALLtalk s von den Metaklassen der Klassen geerbt werden (z. B. Object class),stehen sie in den Klassen als Klassenmethoden zur Verfugung. new und new: werden also in der Praxis immer an Klassen geschickt.

### Dominanz der Vererbung

SMALITALK stammt aus einer Zeit, in der man mit der objektorientierten Programmierung noch relativ wenig praktische Erfahrung gesammelt hatte. Damals war man der Ansicht, einer der Hauptvorteile der objektorientierten Programmierung sei die Wiederverwendung von Code durch Vererbung. Nun hat die Vererbung, wie in Abschnitt 10.1 dargelegt, durchaus etwas mit der auf Generalisierung bzw. Spezialisierung beruhenden Abstraktionshierarchie zu tun: Der allgemeinere Begriff (die Superklasse) übertragt (verebt) alle seine Eigenschaften auf die spezielleren Begriffe (Subklassen), der speziellere erbt sie von den allgemeineren. Dies liegt in der Natur der Sache. Problematisch wird es jedoch, sobald man den kausalen Zusammenhang umkehren und von einer moglichen Vererbung auf eine Generalisierung/Spezialisierung schliessen will: Nur weil eine Klasse (zufalling) Eigenschaften einer anderen gebrauchen konnte, heisst das noch lange nicht, dass die erbende Klasse auch eine Spezialisierung der verebenden ist. Ein klassisches Beispiel hierzu hatten wir mit der Ableitung der Klasse **Rechteck** von der Klasse **Quadrat** bereits kennengelernt; den unangehmen Folgen solch verebungsorientierter Vorgehensweisen werden wir in der nachsten Kurseinheit noch begegnen.

## 12 Dynamisches Binden

Wie bereits in den Abschnitten 4.3.2 und 4.5.2 in Kurseinheit 1 angerissen, verbigt sich hinter dem Nachrichtenversand ein dynamisch gebundener Methodenaufruf. Dabei ist die Auswahl der Methode nicht nur vom Nachrichtenselektor, sondern auch vom Emfangerobjekt abhangig. In Abschnitt 11.2 hatten wir bereits angedeutet, wie in Superklassen definierte Methoden für ihre Subklassen zugereifbar sind; hier schauen wir uns nun etwas genauer an, wie die dynamische Bindung von Methodenaufrufen vorstatten geht.

Wenn eine Methode auf einem Empfangerobjekt aufgerufen wird, wird zunächst geprufft, ob die Methode im zur Klasse des Empfangers gehorden Methodenworterbuch enthalten ist. Dies kann man auch selbst tun: Es gibt dafur in der Klasse **Behavior** eine Instanzmethode

[FIGURE:S1.F1][ENDFIGUR

[MISSING_PAGE_FAIL:132]

Abschnitt 10.3 und 11.3).41 In den statisch typgepruften Sprachen, die wir in den nachsten Kurseinheiten kennenlern werden, ist das charakteristischerweise nicht so. Dem kann man entgegenhalten, dass die heutigen (auch) statisch typgepruften Programmiersprachen wie Java, C# oder C++ samtliche nicht ohne dynamische _Typumwandlungen_ auskommen, die ebenfalls zu Laufzeitfehlern fuhren können. Tatsachlich ist es sowohl in Smalltalk als auch in Java und C# (in C++ nur mit Einschrankungen; s. Abschnitt 51.5) nicht nur moglich, sondern sogar geboten, Laufzeitfehler da, wo moglich, zu vermeiden, indem man vor einem Methodenaufruf explizit pruft, ob ein Objekt die gewunschte Methode auch hat -- in Smalltalk mittels canlnderstand:, in Java et al. mittels eines entsprechenden Typtests vor einem _Down cast_. Die großßere Flexibilitat, die die objektorientierte Programmierung durch das dynamische Binden bietet, hat eben den Preis, dass bestimmte Laufzeitprufungen durchgefuhrt werden mussen. Statische Typprufung kann das Risiko von Typfehlern verringern, aber nicht ausschliessen -- gleichzeitig schrankt es die Flexibilitat beim Programmieren ein, ein Umstand, der so manchen, der schon einmal grossere Programme in Smalltalk geschrieben hat, an der Verwendung typgeprufter Sprachen stort.

Footnote 41: Nicht umsonst ist das heute unter dem Namen JUNIT am besten bekante Unit-test-Framework zuerst für Smalltalk entwickelt worden -- in Smalltalk ist Testen die einzige Möglichkeit, Fehler in einem Programm vor seiner Auslieferung zu finden.

### Nachrichten an self

In Smalltalk muss das Empfangerobjekt eines Nachrichtenversands immer explizit gemacht werden, selbst wenn sich die dazu passende Methode in derselben Klasse befindet. So kann also insbesondere **self** nicht (wie beispielsweise this in Java) weggelassen werden, wenn ein Objekt eine Nachricht an sich selbst schicken mochte. Wie bereits in Abschnitt 4.3.1 erwahnt, bezeichnet die Pseudovariable **self** immer den Empfanger der Nachricht, also dasjenige Objekt, auf dem die Methode, in deren Definition die Variable **self** vorkommt, gerade ausgefuhrt wird, und dessen Instanzvariablen zugreifbar sind. (Die einzige Ausnahme hiervon bilden Blocke, in denen **self** sich auf den Empfanger des _Home context_ bezieht; s. Abschnitt 4.4.1 in Kurseinheit 1).

Dabei ist allerdings zu beachten, dass die Klasse des durch **self** bezeichneten Objekts nicht unbedingt dieselbe sein muss, in der die gerade ausgefuhrte Methode (in der auch das **self** steht) definiert ist, denn das kann ja, aufgrund von Verebrung, durchaus eine Superklasse sein. Das hat eine fundamentale Auswirkung: Die zu einer an **self** geschickten Nachricht passende Methode ist nicht automatisch die, die in derselben Klasse definiert ist, sondern kann durchaus in einer ihrer Subklassen gefunden werden, namlich dann, wenn die aufrufende Methode selbst erst im Rahmen der Suche in der Kette der Superklassen gefunden wurde. Konkret bedeutet diese (bereits in Abschnitt 10.3 im Kontext abstrakter Klassen beschriebene) sog. _offene Rekursion_, dass das Ergebnis des Ausdrucks

[MISSING_PAGE_FAIL:134]

[MISSING_PAGE_FAIL:135]

davon abhangt, welcher Art die Operanden sind. Nehmen wir beispielsweise an, es gabe zwei primitive Methoden für die Addition, und zwar eine effiziente für die Integer-Addition (**IAdd**) und eine weniger effiziente für die Float-Addition (**FAdd**), und man mochte Additionen für beliebige Kombinationen von Summanden moglichst effizient durchfuhren können. Dann kommt man vielleicht auf die folgende Tabelle von Zuordnungen:

Wahrend die Unterscheidung nach Empfangerobjekten vom dynamischen Binden und damit dem Laufzeitsystem vorgenommen wird, bleibt die Frage, wie man die Unterscheidung nach den Parameterobjekten vornimmt: Zumindest die Implementation der Addition in der Klasse **Integer** muss ja danach unterscheiden, ob der Parameter auch ein Integer oder vielleicht ein Float ist. Anstatt nun diese _Fallunterscheidung_ (mittels entsprechender Methoden isInteger bzw. isFloat) explizit zu machen, kann man sich eines einfachen Tricks bedienen: Man ruff im Rumpf einer Methode dieselbe Methode einfach noch einmal auf und vertaucht dabei Empfanger (self) und Parameter. Damit es dabei nicht zu unendlichen Rekursionen kommt, kodiert man die Klasse des Empfangers im Nachrichtenselektor der neu aufgerufenen Methode42, also z. B. plusFloat: anstelle von nur **plus** :. Das Ergebnis sieht dann wie folgt aus:

Footnote 42: In Sprachen wie Java, in denen das _Double dispatch_ auch gebrauchlich ist, ist das nicht notwendig, da es in ihnen zur Differenzierung von gleichnamigen Methoden das sog. _überladen_ gibt.

[FIGUREDiese Technik, namlich eine Methode gleicher Bedeutung unter Vertauschung von Sender und Empfanger aufzurufen, nennt man **Double dispatch**, und zwar, weil die dynamische Bindung (auch _Method_ oder _Message dispatching_ genannt) zweimal, und zwar unmittelbar hintereinander, erfolgt. Etwas ahnliches haben Sie bei der Implementierung von + in **Integer** in Abschnitt 4.3.7 (Kurseinheit 1, Zeile 154) schon gesehen. Die Technik des Double dispatch wurde ubrigens von Dan ingalls am Beispiel von Smalltalk erstmals beschrieben; sie findet auch in anderen Sprachen mit _Single dispatch_ (wie Java und C#) verbreitet Anwendung. Double dispatch wird in Sprachen, bei denen bei der (dynamischen) Methodenauswahl von Haus aus die Parametertypen mit beruckschtigt werden (die sog. _Multidispatch-Sprachen_), naturgemas nicht benotigt.

## 13 Programmieren mit Collections

In Kapitel 2 von Kurseinheit 1 waren wir bereits auf :\(n\)-Beziehungen eingegangen, die logisch gleichberechtigt neben Zu-1-Beziehungen stehen, die aber in der Umsetzung besonderer Mechanism bedurfen. Als Basis der Umsetzung hatten Sie bereits Zwischenobjekte kennengelent, die über ihre indizierten Instanzvariablen solche Beziehungen -- wenn auch nur indirekt -- herstellen können. Tatschlich konnte man, wenn man sich der Haufigkeit des Vorkommens von :\(n\)-Beziehungen in der Programmierung bewusst ist, vermuten, dass indizierte Instanzvariablen speziell für diesen Zweck eingefuhrt wurden. Auf den ersten Blick bedauerlich ist nur, dass dafur eben diese Zwischenobjekte notwendig sind.

Es ergibt sich aus diesem Umstand aber auch ein entscheidender Vorteil.

Da auch diese Zwischenobjekte Instanzen von Klassen sein mussen, ist es

**Verhalten** moglich, verschiedene Arten von :\(n\)-Beziehungen zu definieren und diese jeweils mit Verhalten zu versehen, das speziell auf die Art der Beziehung bezogen ist. So ist es beispielsweise moglich, :\(n\)-Beziehungen zu definieren, deren Elemente (die in Beziehung stehenden Objekte) jeweils nur einmal darin vorkommen durfen (mengenwertige Beziehungen) oder nach einem bestimmten Kriterium sortiert sind. Auch können Operationen wie das Hinzufugen oder Entfernen von Objekten zu einer Beziehung, die bei Zu-1-Beziehungen über die Zuweisung zu einer Instanzvariable erfolgen (das Entfemen durch Zuweisung von n11), beliebig ausgestaltet werden, um beispielsweise die Mengenwertigkeit oder die Sortierung zu erhalten.

Besonders attraktiv ist jedoch die in Smalltalk bestehende Moglichkeit,

**Spezielle** eigene Kontrollstrukturen für :\(n\)-Beziehungen zu spezifizieren. Die bereits

**Kontrollstrukturen** vorhandenen durften Sie ja schon in Abschnitt 4.6.4 kennenlernen; hier

**fur :\(n\)-Beziehungen** kommt hinzu, dass die Standarditeratoren je nach Art der Beziehung unterschiedliche Eigenschaften haben. Außerdem ist es naturlich moglich, mit eigenen Arten von Beziehungen

auch spezielle, nur für diese Beziehungen benotigte Kontrollstrukturen zu spezifizieren. Doch zunächst zur Pflege von solchen Beziehungen.

### Pflegen von :\(n\)-Beziehungen

Um :\(n\)-Beziehungen zu pflegen, also um Objekte zu einer Beziehung hinzuzufugen und wieder zu entfemen, sieht Smalltalk standardmagbig die Methoden **add** : und **remove** : vor, die beide jeweils das Argumentobjekt zuruckeliefern. Beide sind in der abstrakten Klasse **Collection** definiert, die Wurzel einer Hierarchie von Klassen, den _Collection-Klassen_, ist, die allesamt der Verwirklichung von :\(n\)-Beziehungen dienen. Unsere Zwischenobjekte, die diese Beziehungen reprasentieren, sind also alle indirekte Instanzen von **Collection**.

Die Methoden **add** : und **remove** : bleiben zunächst (in **Collection**) **Methoden add** : und **remove** : abstrakt:

```
476add:anobject
477
478selfimplementedBySubclass
479
479self
480remove:anobject
481ifAbsent:[selferrorAbsentObject]
482remove:anobjectifAbsent:anExceptionBlock
483selfimplementedBySubclass
```

Da sie von der tatsachlichen Realisierung einer Collection abhangen, können sie erst in den entsprechenden Subklassen (durch _überschreiben_) realisiert werden.

Beim Entfernen eines Objektes aus einer Collection43 mittels **remove** : gibt es zwei Sonderfalle zu berucksichtigen: Das Objekt ist nicht vorhanden oder das Objekt ist mehrfach vorhanden. Im ersten Fall wird ein Fehler gemeldet, wahrend im zweiten nur ein Vorkommen des Objekts aus der Collection entfernt wird (das erste, wie auch immer die Reihenfolge festgelegt ist). Da es immer vorkommen kann, dass ein zu entfernendes Objekt gar nicht vorhanden ist, und ein entsprechender vorhoriger Test auf Vorhandensein (s. u.) wieder so eine stereotype Handling ist, bietet **SMALLtalk** eine Variante von **remove** :, die einem genau das erspart: **remove** : anObject **ifAbsent** : anExceptionBlock**. Soltte das zu entfemende Objekt fehlen, wird stattdessen **anExceptionBlock** ausgefuhrt und dessen Ergebnis zuruckgeliefert. Will man, dass beim Versuch, ein nicht vorhandenes Objekt zu entfernen, nichts passiert, so gibt man einfach den leeren Block [] für **anExceptionBlock** an. Sollen mehrere Objekte auf einmal einer Beziehung hinzugfugt bzw. daraus entfernt werden, so stehen hierfur die Methoden addAll: aCollection bzw. removeAll: aCollection zur Verfugung, die jeweils eine Collection als Parameter enwarten.

[MISSING_PAGE_FAIL:139]

Dabei ist addAll: nur einmal, namlich in Collection, definiert. Man beachte, dass dabei ein Objekt nicht seine Klasse wechselt, sondem lediglich der Inhalt einer Collection in eine neue obertragen wird. Diese übertragung ist immer dann sinnvoll, wenn die Klasse der neuen Collection Eigenschaften hat, die man gem nutzen mochte. Ein Beispiel hierfur finden Sie in Zeile 525 unten. Die Nachricht **yourself** (von Object geerbt) liefert überigens ihren Empfanger zuruck; sie wird am Ende von kaskadierten Nachrichtenausdrucken in Return-Anweisungen verwendet, um den Empfanger zuruckzuliefern.

Zum Pflegen seiner Beziehungen ist es manchmal vorteilhaft, zu wissen, mit wie vielen Objekten man in Beziehung steht und mit welchen. Die Klasse Collection sieht dafur die Methoden size, isEmpty und notEmpty, includes: sowie occurencesOf: vor, die jeweils die nabelegte Bedeutung haben.

### 13.2 Zu-n-Beziehungen mit besonderen Eigenschaften

Die Klasse Collection ist wie gesagt abstrakt. SMALITALK sieht nun eine ganze Hierarchyen von spezielleren, instanzierbaren (konkreten) Collection-Klassen vor, die für die unterschiedlichsten Zwecke eingesetzt werden können. Darunter sind so offensichtliche wie **Set** (fur ungeordnete Collections, in denen jedes Element hochstens einmal vorkommen darf, also Mengen) und **Bag** (fur solche, in denen die letzte Einschrankung aufgehoben ist). **Set** und **Bag** haben (neben der mangelnden Ordnung ihrer Elemente) gemein, dass die Elemente in beiden nicht über einen Index zugerfbar sind. Im Gegensatz dazu stehen geordnete Collections (Klasse **SequenceableCollection** oder **IndexedCollection**, je nach System), in denen das \(i\)-te Element eindeutig bestimmt ist und die entsprechend die Methoden at: und at:put: implementieren (genaugenommen überschreiben, denn diese Methoden sind ja für alle Objekte, die über indizierte Instanzvariablen verfugen, schon definiert, und werden lediglich für ungeordnete Collections wieder geloscht). Aber auch ungeordnete Collections (in denen keine Reihenfolge festgelegt ist) können indiziert sein: In Objekten der Klasse **Dictionary** wird jedes Element unter einem Schlussel, der selbst wieder ein Objekt sein kann, gespeichert. Die dazugehofigen Methoden heissen wiederum at: und at:put:, erlauben aber Objekte anderer Klassen als **Integer** als Indizes.

#### Dictionaries

Dictionaries reprasentieren sog. qualifizierte Beziehungen, das sind solche, bei denen jedes Element der Beziehung durch einen Qualifizierer eindeutig bestimmt wird. Der Qualifizierer heißt auch _Schlussel_ (engl. key; vergleichbar mit dem Primarschlussel relationaler Datenbanken), das qualifizierte Element der Beziehung nennt man auch Wert (engl. value). Ein Element einer qualifizierten Beziehung besteht also gewissermassen aus einer Asoziation eines Schlussels mit einem Wert. Der Clou an der Implementierung von Dictionaries ist, dass man Werte unter ihren Schlusseln extrem schnell (im Idefall ohne jede Suche) auffinden kann. Das wird heute fast immer über sog. Hashing erreicht.

[MISSING_PAGE_FAIL:141]

die Delegation auf Instanzebene stattfindet und zudem dynamisch (also nachdem eine Instanz erzeugt wurde) eingerichtet werden kann und da sie zudem von Fragen der Generalisierung/Spezialisierung vollig befreit ist, erfreut sie sich in der objektorientierten Programmerung grosser Beliebtheit.

Je langer Sie in SMalltalk programmieren, desto haufiger werden Sie

feststellen, dass Sie durch Verwendung eines Dictionaries lhren Code

duetlich vereinfachen können. Tatsachlich erlauben es Dictionaries (bzw.

der von ihnen realisierte _Assoziaitvspeicher_), Assoziationsketten, die Grundlage vieler

menschlicher Denkprozesse sind, direkt in einem Programn nachzubilden. Fragen Sie sich also, wann immer Sie es mit einer Menge von Objekten zu tun haben, wie Sie auf die Elemente der Menge zugereifen wollen; wenn dies über einen Schlossel erfolgt, dann ist

Dictionary die Klasse Ihrer Wahl.

Es darf ubrigens der Schlussel eines in einem Dictionary gespeicherten

Objekts ruhig ein Attribut (der Inhalt einer Instanzvariable) des Objekts sein; dies kommt

sogar recht haufig vor. Beispielsweise wird man Personen in einem Dictionary unter ihrem

Nachnamen oder einer Ausweisnummer speichern. Allerdings sollte dieses Attribut dann unveränderlich sein, da das Objekt nach einer Anderung des Attributs immer noch unter

dem alten Attributwert als Schlussel gespeichert ist und nur unter diesem wiedergefunden wird.

#### 13.2.2 Sortierte Collections

Eine weitere nutzliche Collection-Klasse wird durch SortedCollection implementiert. Es handelt sich dabei um eine Subklasse von OrderedCollection, bei der die Reihenfolge der Elemente nicht von aussen, also durch die Angabe eines Indexes oder die Reihenfolge der Einfugung, festgelegt wird, sondern von innen, genauer durch eine Qualitat der eingefugten Objekte. Zwischenobjekte der Klasse SortedCollection setzt man ein, wenn man die in Beziehung stehenden Objekte in einer bestimmten Reihenfolge stehen wissen mochte, wie z. B. die Kinder einer Person in der Namensfolge, und zwar unabhangig davon, in welcher Reihenfolge sie der Collection hinzugefugt wurden. Voraussetzung dafur, dass die Elemente einer SortedCollection sortiert werden können, ist, dass sie sich vergleichen lassen, dass also die (binare) Methode <= (fur kleiner gleich) darauf definiert ist. So liefert beispielsweise
mit #(123) das gewunschte Ergebnis.45

Wenn die Elemente, die in eine sortierte Collection eingefugt werden solen.

Sortierblocke len, keine Grossen sind, also insbesondere den Vergleich <<= nicht implementieren, dann ist es immer noch moglich, für eine neue Instanz einer SortedCollection einen sog. Sortierblock zu spezifizieren, der zwei _formale Parameter_ hat und dessen Auswertung zuruckliefert, ob der erste tatsachliche Parameter kleiner oder gleich dem zweiten ist. Tatsachlich wird, falls man bei der Erzeugung keinen Sortierblock angibt, ein Standardsortierblock angenommen:

SortedCollection

OrderedCollection

SortedCollection

OrderedCollection

SortedBlock: aBlock

"Answer aSortedCollection which will

sort in the order defined by aBlock."

"(super new: 10) sortBlock: aBlock

new: anInteger

"Answer a SortedCollection capable of

holding anInteger number of elements

which will sort in ascending order."

"(super new: anInteger) sortBlock: [:a:b|a<=b]

sortBlock

noltierte Instanzaribalen

nein

sistammethoden

S35sortBlock: aBlock

"Answer the receiver. Set the sort block for

the receiver to aBlock and resort the receiver."

sistamblock := aBlock.

sistammethoden

S36

"Answer the receiver. Set the sort block for

the receiver to aBlock and resort the receiver."

sistamblock := aBlock.

sistam

self reSort

S37

"Man beachte jedoch, dass eine nachtragliche Anderung der Attributwerte, die zum Vergleich der Objekte für die Sortierung herangezogen wurden, keine automatische Anderung der Reihenfolge bewirkt, selbst wenn dies eigentlich notwendig wurde.

#### Arrays

Nicht zuletzt werden auch ganz banale Arrays haufig verwendet, insbesondere wegen der (bereits in Abschnitt 1.2 vorgestellten) Moglichkeit der einfachen _literalen Definition_. So kann man ohne viel Aufwand über die Elemente einer beliebigen, ad hoc spezifizierten Aufzahlung iterieren:

```
541#(1'abc'true)collect:element - 1
```

beispielsweise weist dem Laufparameter des Blocks, element, nacheinander die Elemente des literalen Arrays zu. Der Wesentliche Nachteil von Arrays ist, dass ihre Grosse beschrankt ist. benotigt man eine geordnete Collection, die beliebig wachsen kann, der von Arrays, also am Anfang, am Ende oder an einer beliebigen Position dazwischen Elemente hinzugefugt werden können, dann kann man auf Instanzen der Klasse OrderedCollection zuruckgreifen. Diese eignen sich aufgrund des angebotenen Methodensatzes, ihres _Protookolls_, speziell für die Implementierung von Stapeln (Stacks) und Puffern (Queues).

### 13.3 Collections für andere Zwecke

Nicht alle Collections dienen der Umsetzung von :\(n\)-Beziehungen. Ein gutes Beispiel gibt die Klasse Interval. Bei Instanzen der Klasse Interval handelt es sich um endliche arithme-

\begin{tabular}{c c}  & Intervalle als \\  & Collections \\  & Abstand zueinander haben. Die Elemente einer solchen Collection mussen deswegen nicht \\  & gespeichert, sonderm können berechnet werden. Die Spezifikation eines Intervalls umfasst seinen Anfangs- und seinen Endwert sowie die Schrittweite, die auch negativ sein darf. \\
542(Interval from: 5 to: 1 by: -2) & \\  & erzeugt ein Intervall, das die Zahlen 5, 3 und 1 enthalt. Intervalle dienen vor allem dem Zweck, sog. For-Schleifen zu emulieren (s. Abschnitt 4.6.3 in Kurseinheit 1): \\
543(Interval from: 5 to: 1 by: -2) do: [:-1 - 1] & \\  & etwa bewirkt, dass dem Laufparameter i nacheinander die Werte **5**, **3** und 1 zugewiesen werden. Die zugeparamettige Form \\
544(Interval from: 1 to: 10) do: [:-1 - 1] & \\  &nimmt hingegen eine Standardschrittweite von 1 an. für noch mehr Komfort ist in der Klasse Number eine Methode to:by:vorgesehen, die ein entsprechendes Intervall zuruckliefert:

```
545to:eNumberby:iNumber
546AIntervalfrom:selfto:eNumberby:iNumber erlaubt, statt Zeile 547(5to:1by:-2)do:i1-1
```

zu schreiben. Um der geschatzten Programmiererin auch noch die Klammern zu ersparenen, wurde gleich noch die Methode to:by:do:hinzugefuigt, die daraus
5485to:1by:-2do:[::1|_=1] zu machen erlaubt. (Man beachte, dass hier der Iterator in der Klasse Number und nicht in einer Collection wie Interval definiert wurde.) Wie man sieht, ist es in Smalltalk moglich, ohne grossen Aufwand neue Ausdrucksformen hinzuzufugen, ohne dazu (wie in den meisten anderen Sprachen notwendig) die Syntax andern zu mussen.

```
Selbsttestaufgabe13.1 Siefinden folgendes Codefragment vor:
5491to:asizedo:[::1|(aat:1)doSomething] Kritisieren Sie es! Zu guter Letzt sind auch die Klassen String und Symbol Collections, und zwar genauer geordnete Collections fester Grosse (wie Arrays), deren Inhalt jedoch auf Zeichen (Instanzen der Klasse Character) beschrankt ist. Strings sehen neben der Moglichkeit des Vergleichs (mittels der Operatoren <, <=, >, >=) auch noch ein Pattern matching (Methode match:aString) sowie spezielle Operatoren zur Behandlung von Gross-/Kleinschreibung und eine Konversion in Literale vor. (Die Klasse Symbol ist ubrigens eine Subklasse der Klasse String; sie erbt damit alle Methoden von String.) Auf die Moglichkeiten der literalen Repräsentation von Strings und Symbolen wurde bereits in Kurseinheit 1, Abschnitt 1.2, eingegangen.
``` Selbsttestaufgabe13.2 ```

überlegen Sie sich, wie Sie das Case- (oder Switch-)Statement in Smalltalk simulieren wurden, und gehen Sie auf die Einschrankungen ein, die Sie dazu machen mussen.

Verhalten für alle Objekte

In der Klasse Object ist das Protokoll definiert, das allen Objekten gemein ist, d. h., für das alle Klassen Methodendefinitionen haben, und zwar entweder eigene oder geerbte. Object gibt zu diesem Zweck Standardimplementerungen vor, die von den meisten Objekten direkt übernommen werden können (und nur von den wenigsten überschrieben werden mussen). Dazu zahlen z. B. die Bereits mehrfach erwahnten isNil und notNil (die nur von Undefinedobject überschrieben werden) sowie zahlreiche weitere Typtests (isInteger, isFloat usw.). Daneben gibt es auch noch eine ganze Reihe anderer Methoden, die zu kennen es sich lohnt.

### Kopieren von Objekten

In Abschnitt 7.3 hatten wir ja die Instanzierung als den hauptsachlichen Weg kennengelernt, wie neue Instanzen von Klassen, für deren Objekte es keine literale Repräsentation gibt, erzeugt werden. Wir hatten allerdings dort schon auf die Moglichkeit des Klonens/Konpierens hingewiesen. Darauf wollen wir nun wieder zuruckkommen.

Die einfachste Form des Kopierens eines Objekts erzeugt ein Objekt glei- 

```
550shallowCopy
551"Answer a copy of the receiver which shares the receiver instance variables."
```

Diese Methode liefert eine neue Instanz der Klasse des Empfangers, die in denselben Beziehungen zu denselben anderen Objekten steht wie das Original. Insbesondere werden die Objekte, die die Instanzvariablen des Originals benennen, nicht selbst kopiert. Deswegen nennt man die Kopie **flach**. Sie erfolgt einfach durch Zuweisung aller Instanzvariablen des Originals an die Instanzvariablen des neuen Objekts, das damit zur Kopie wird. Die Implementierung in SMALITALK EXPRESS ist die folgende:

```
553|answeraClass size|
554aClass:=selfclass.
555aClassisVariable
556ifTrue:[
557size:=selfbasicSize.
558answer:=aClassbasicNew:size]
559ifFalse:[
560size:=0.
561answer:=aClassbasicNew].
562aClassisPointers
563ifTrue:[
5641to:size+aClassinstSizedo:[:index|
565answerinstVarAt:index
566put:(selfinstVarAt:index)]]
567ifFalse:[
5681to:sizedo:[:index|
569answerbasicAt:index
570put:(selfbasicAt:index)]].
571"answer
```

isVariable unterscheidet dabei zwischen Klassen mit indiizierten Instanzvariablen und solchen ohne; isPointers unterscheidet zwischen Klassen mit zusammengesetzten Objekten und _atomaren_.

Nun ist eine flache Kopie aber haufig nicht genug. Es gibt daher noch 

```
572deepCopy
573"Answer a copy of the receiver with shallow copies of each instance variable."
```

Wie der Name nahelegt, unterscheidet sich die Methode deepCopy von shallowCopy darin, dass auch die in Beziehung stehenden (durch die Instanzvariablen benannten) Objekte kopiert werden. Statt einzelner Objekte wird also ein Objektgeflecht kopiert -- die Kopie ist **tief**. Es muss dazu an die beiden tatsachlichen Parameter von **put** : (Zeilen 566 und 570) lediglich eine Nachricht zum Kopieren der Parameter angehangt werden. Dabei ist jedochVorsicht geboten: Wenn es sich dabei ebenfalls um ein tiefes Kopieren handelt, dann kann der Kopiervorgang leicht in eine Endlosrekursion geraten.

**Selbsttestaufgabe 14.1**

überlegen Sie, wie Sie ein rekursives tiefes Kopieren technisch in den Griff bekommen können.

Nun ist die Festlegung, ob die Kopien ihrer Instanzen tiefe oder flache

**klassenspezifische**

sein sollen, gelegentlich ein Charakteristikum der Klasse selbst. Jede

**Kopiertiefe**

Klasse erbt deswegen von **Object** eine Methode **copy**, die standardm\(\ddot{\text{a}}\)lig (also in **Object**)

einfach **shallowCopy** aufruft (warum es nicht **deepCopy** aufruft, sollte klar sein) und die erbende Klasse entsprechend ihren eigenen Konditionen **überschreiben kann. Es ist so moglich, die Kopiertiefe von Objektstrukturen selbst zu bestimmen, indem man **copy** für manche Klassen **deepCopy** aufrufen lasst und das tiefe Kopieren durch Instanzen terminiert, deren Klassen **shallowCopy** aufrufen lassen.

Manchmal darf bei Kopier- oder Konvertioperation kein Objekt des

**Kopiervorgange mit**

gleichen Typs zuruckgegeben werden. In diesen Fallen sollte statt self

**self species**

class (Zeile 554) self species aufgerufen werden:

**species**

* "Answer a class which is similar to (or the same

**as) the receiver class which can be used for

**containing derived copies of the receiver."**

Die Methode species war uns schon einmal begegnet, und zwar in Kurseinheit 1, Abschnitt 4.6.4, Zeile 244. Sie gibt standardm\(\ddot{\text{a}}\)big die Klasse des Empfangerobjekts zuruck und kann überschrieben werden, wenn eine andere Klasse angegeben werden soll. Dies ist

z. B. bei der Methode collect:, ausgefuhrt auf einer Instanz von **Interval**, sinnvoll, da

**collect:**

* "hier kein Intervall zuruckgegeben kann. So kann beispielsweise die von

**(Interval from: 1 to: 5) collect: [ n n printString ]**

zuruckgegebene Collection von Strings nicht als Intervall dargestellt werden. Entsprechend

ist in der Klasse Interval die Methode species als

**species**

* "Array**

implementiert.

### Reinkarnation von Objekten

Eine der vielleicht interessantesten Methoden SMALITAKS ist die Methode become :

**become: anObject**

[MISSING_PAGE_FAIL:149]

[MISSING_PAGE_EMPTY:150]

"default do nothing"
*release
* "Discard all dependents of
* the receiver, if any."
* Dependents removeKey: self ifAbsent: []

### Selbstdarstellung

Wir hatten bereits ausgenutzt, dass alle Objekte Smalltalks eine (mehr oder weniger aus-sagekraftige) String-Repräsentation besitzen: Die Methode

```
638printString
639"Answer a String that is an ASCII representation
640ofthe receiver."
```

gibt eine Darstellung des Objekts als String zuruck. Dies ist für Ausgaben auf dem Transcript interessant, aber auch für die Inspektion von Objekten und für das Debugging, bei denen sich die Objekte unter Verwendung dieser Methode der Betrachterin prasentieren.

Die Methode inspect
641inspect
642"Open an inspector window on the receiver." ```
startet auf dem Empfanger einen Inspektor und gibt den Empfanger zuruck. Dies ist nutzlich, wenn man ein Zwischenperbnis eines Ausdrucks inspizieren mochte, ohne den Ausdruck dazu in zwei aufteilen zu wollen -- man fugt einfach inspect an der Stelle des Ausdrucks, an der das zu inspizierende Objekt gewonnen wurde, ein.

Die Methode
```
643storeOn:aStream
644"Append the ASCII representation of the
645receivertoaStream from which the
646receivercanbe reinstantiated." ```

erlaubt, ein Objekt so auf einen Ausgabestrom (s. u.) zu schreiben, dass es daraus rekonstruiert werden kann. Dabei wird keine binare, sondern eine textuelle Repräsentation verwendet. So schreibt beispielsweise Squeak bei Auswertung von Time noon storeOn:aStream die Zeichenfolge '12:00 pm'asTime auf den durch aStream bezeichneten Ausgabestrom und (Interval from: 1 to: 5) die Zeichenfolge '(1 to: 5)'.

[MISSING_PAGE_FAIL:152]

* "Write each of the objects in aCollection to the receiver stream. Answer aCollection."
* "nextMatchFor: anObject
* "Access the next object in the receiver. Answer
* "true if it equals anObject, else answer false."
* "skip: anInteger
* "Increment the position of the
* "receiver by anInteger."
* "skipTo: anobject
* "Advance the receiver position beyond the next
* "occurrence of anObject, or if none, to the end of
* "stream. Answer true if anObject occurred, else
* "answer false."
* "atEnd
* "Answer true if the receiver is
* "positioned at the end (beyond
* "the last object), else answer
* "false."

Fur frei positionierbare Streams kommt noch das Protokoll zur Anderung des Zeigers hinzu:

* "Answer the current receiver stream position."
* "position: anInteger
* "Set the receiver stream position to anInteger.
* "Report an error if anInteger is outside the
* "bounds of the receiver collection."
* "
* "Position the receiver stream to the beginning."
* "setToEnd
* "Set the position of the receiver stream to
* "the end."
* "peek
* "Answer the next object in the receiver stream
* "without advancing the stream position. If the
* "stream is positioned at the end, answer nil."

Fur **peek** ist die freie Positionierbarkeit notwendig, weil man dazu erst das nachste Element

anspringen und dann wieder einen Schritt zuruckgehen muss.

Da ein Stream (wie eine Collection) eine Menge von Objekten reprasentiert, mochte man darüber (genau wie über eine Collection) iterieren können. Kein Problem:

* "Evaluate aBlock once for each element in the
* "receiver, from the current position to the end."
* "self atEnd* [39] **whileFalse: [aBlock value: self next]**

Ausserdem wird naturlich zwischen (nur) lesbaren und schreibbaren Streams unterschieden.

Erst eine weitere Kategorie von Streams operiert nicht auf Collections,

**Streams auf Dateien**

sondem auf externen Daten. Dazu gehoren insbesondere die File streams. In SMALLtalk-80 wurde mit den Klassen FileDirectory, File und FilePage (die selbst keine Streams sind) ein eigenes Dateisystem geschaffen; die meisten heute gebrauchlichen Implementierungen nehmen jedoch eine Abbildung auf das Betriebssystem vor, für das sie geschrieben wurden. Man erkennt hier noch sehr schon, welche Funktion Smalltalk ursprunglich zugdacht war: die der einzigen Software auf einem Computer.

Besonders in SQUEAK gibt es noch zahllose weitere Streams, so u. a. für Multimedia-Aufgaben; insgesamt unterscheiden sich die verschiedenen Smalltalk-Dialekte bei der Handhabung von Streams zum Teil erheblich, veswegen wir hier auch nicht weiter darauf eingehen.

## 16 Parallelitat: aktive und passive Objekte

Die objektorientierte Weltsicht, die auch in diesem Kurs propagiert wird (namlich die von den Objekten, die einander Nachrichtten schicken und die auf den Empfang von Nachrichten reagieren, indem sie ihren Zustand antern und weitere Nachrichten verschicken), legt nahe, dass Objekte aktiv sind, will sagen, dass sie über einen eigenen Rechenprozess verfugen. Doch schon in Abschnitt 4.3.2 wurde klar, dass es damit in der Realitat nicht weit her ist: Es werden in der Praxis keine Nachrichten verschickt, sondern lediglich Methoden aufgerufen.

Abgesehen vom dynamischen Binden dieser Methoden unterscheidet sich damit das Ausfuhrungmodell der objektorientierten Programmierung nicht von dem der prozeduralen Programmierung (a la Pascal); insbesondere sind alle Objekte **passiv** (was soviel bedeutet, wie dass sie nur aktiv sind, solange sie gerade eine Methode ausfuhren).

Unter **aktiven Objekten** wurde man sich vorstellen, dass sie über einen Prozess verfugen, der nur die eigenen Methoden ausfuhrt. Erhalt ein aktives Objekt eine Nachricht, dann nimmt es diese an und arbeitet sie ab, sobald es die Zeit dazu hat. Die Kommunikation aktiver Objekte wurde namlich asynchron ablaufen, wenn mit der Nachricht (dem Methodenufuf) nicht auch ein Prozess verbunden ist (was ja dem klassischen Prozedurafurf entsprache). Aktive Objekte waren aber sehr aufwendig und deswegen setzt die objektorientierte Programmierung in der Praxis auf passive.

Gleichwohl ist auch in der objektorientierten Programmierung Parallelver-

**parallele Prozesse**

arbeitung moglich. Nur kommt sie (zumindest in Smalltalk, aber auch z. B. in JAVA) nicht in Form von aktiven Objekten daher, sondern in Form von parallelen Prozessen. Jeder dieser Prozesse fuhrt zu einer Zeit eine Methode aus; er besucht zwar mit dem Methodenaufruf die Empfangerobjekte, diese bleiben jedoch selbst passiv (haben also kein Eigenleben).

[MISSING_PAGE_FAIL:155]

[MISSING_PAGE_FAIL:156]

* [716] AlleInstanzen isNil ifTrue: [AlleInstanzen := Set new].
* [717] neueInstanz := self basicNew.
* [718] AlleInstanzen add: neueInstanz.

* neueInstanz ```
**Selbsttestaufgabe 8.3 (Seite 95)**
```
720accessingSubClass:className
721instanceVariableNamesWithAccessor:instWithAccessor
722instanceVariableNamesWithoutAccessor:instWithoutAccessor
723classVariableNames:classVarString
724poolDictionaries:stringOfPoolNames
725newClass|
726newClass := self
727subclass:className
728instanceVariableNames:instWithAccessor,',instWithoutAccessor
729classVariableNames:classVarString
730poolDictionaries:stringOfPoolNames.
731instWithAccessor asArrayOfSubstrings do: [ :aName |
732newClass compile: (aName,' ',aName).
733newClass compile: (aName,':argument ',aName,':=argument.' argument') ].
734newClass ```
Visual Works
```
735accessingSubClass:className
736instanceVariableNamesWithAccessor:instWithAccessor
737instanceVariableNamesWithoutAccessor:instWithoutAccessor
738classVariableNames:classVarString
739poolDictionaries:stringOfPoolNames
740newClass |
741newClass := self
742subclass:className
743instanceVariableNames:instWithAccessor

[MISSING_PAGE_FAIL:158]

[MISSING_PAGE_FAIL:159]

[MISSING_PAGE_FAIL:160]

[:assoc | (assoc key value = self)

iftrue: [^a assoc value value]].

aBlock value

Die Wert-Anweisungspaare mussen zuvor in ein Dictionary eingetragen werden.

**Selbsttestaufgabe 14.1 (Seite 133)**

Es musste bei jedem Ansto\(\ss\) eines tiefen Kopiervorgangs zunächst eine leere Menge erzeugt werden, in die nach und nach alle kopierten Objekte eingetragen werden. Vor jedem Kopieren musste dann zunächst geprutt werden, ob das Objekt nicht schon eingetragen, also bereits kopiert worden ist. Falls ja, musste statt einer neuen Kopie die bereits erzeugte verwendet werden (da sonst identische Objekte nicht zu identischen Kopien fuhren). Man verwendet für die Buchhaltung am besten ein Dictionary.

**Kurseinheit 3: Typen in der objektorientierten Programmierung**

_The purpose of a type system is to prevent the occurrence of execution errors during the running of a program. The accuracy of this informal statement depends on the rather subtle issue of what constitutes an execution error. Even when that is settled, the type soundness of a programming language (the absence of certain execution errors in all program runs) is a non-trivial property. A fair amount of careful analysis is required to avoid false and embarrassing claims of type soundness; as a consequence, the classification, description, and study of type systems has emerged as a formal discipline._

Luca Cardelli

Im Gegensatz zu Smalltalk sind die meisten objektorientierten Programmiersprachen typisert, was soviel hei8t wie dass Programmelementen bei ihrer Deklaration (s. Kapitel 19) Typen zugeordnet werden. Dabei schrankt ein Typ die Menge der Objekte, für die ein Programmelement stehen kann, und die Menge der Dinge, die damit gemacht werden können, ein. Meistens sind die Regeln zur Verwendung von Typen fester Bestandteil der Sprache -- wenn Sie eine solche Sprache neu lernen, dann wurden Sie gar nicht auf die Idee kommen, Typsystem und ubrige Sprachdefinition voneinander getrennt zu betrachten. Dennoch sind Typen für das Funktionieren eines Programms prinzipiell verzichtbar46 und es lohnt sich durchaus, das Typsystem einer Sprache von ihrem Rest zu losen, beispielsweise weil man es austauschen oder verbessern will. Dies um so mehr, als heute gangige Typsysteme entweder ziemlich schwach oder ziemlich kompliziert sind.

Footnote 46: Wenn man auf Moglichkeiten wie das Überladen von Methoden verzichten kann; Laufzeittypinformation, wie man sie z. B. für das _dynamische Binden_ oder für die _Garbage_ collection benötigt, kann durch Laufzeitklasseninformation (was nicht dasselbe ist!) ersezt werden; s. Abschnitt 28.3.

So fuhrt diese Kurseinheit Typsysteme am Beispiel von STRONGtalk, einer Smalltalk-Erweiterung um ein _optionales Typsysteme_, ein Sie geht dabei langsam und inkrementell vor. Wer das zu ode erscheint, die sei gewarnt: Es wird noch kompliziert genug und nicht jede Leserin wird alles, was sie in diesem Kurs über Typsysteme liest, auf Anhieb verstehen. Auch waredie Alternative, diese Kurseinheit am Beispiel einer bekannteren Sprache mit verpflichtendem Typsystem hochzuziehen, stets mit dem Nachteil belastet, dieses konkrete Typsystem als quasi vom Himmel gefallen darstellen zu mussen -- wenn Sie dann spater eine andere Sprache kennenlernen, hatten Sie vermutlich Schwierigkeiten, das Gelernte abzustreifen und sich mit den neuen Verhaltnissen zurechtzufinden. Ziel dieser Kurseinheit ist aber, dass Sie Typsysteme als das verstehen, was sie sind: eine Moglichkeit zur Spezifikation redundanter Information, die die Qualitat von Programmen erhohen soll.

## 18 Hintergrund

Sie kennen vielleicht aus anderen Programmiersprachen, dass Variablen und anderen Programmelementen bei ihrer Deklaration (Kapitel 19) ein Typ zugeordnet wird. Dieser Typ schrankt die moglichen Werte der _deklanieren Elemente_ ein. So lassen sich beispielsweise in einer Variable vom Typ Boolean nur Wahrheitswerte, in einer vom Typ String nur Zeichenketten speichern.

**Typ** ist ein primitiver Begriff, vergleichbar etwa mit dem Begriff der

**Type**: **Menge in der Mengentheorie. Ein Typ hat eine _Intension_ und eine _Extension_, wobei erstere der Definition des Typs entspricht, letztere seinem Wertebereich, also der Menge der Elemente (Objekte), die zu dem Typ gehoren (man sagt auch, die den Typ haben" oder,,die von dem Typ sind"). Haufig hat ein Typ auch einen Namen, den Typbezeichner. Typen sind die Grundlage von Typsystemen.

Ihnen falt wahrscheinlich sofort die Ahnlichkeit zum Konstrukt der

**Type** und Klasse, wie es in der letzten Kurseinheit eingefuhrt wurde, auf. Tatsachlich gibt es hier auch einen Zusammenhang. Um Sie aber nicht bleich in für diese Kurseinheit

eher schadliche Denkmuster verfallen zu lassen, soll dieser Zusammenhang zunächst zuruckgestellt werden. Eine Aufklarung erfolgt dann in Kapitel 28.

Ein **Typsystem** umfasst Typausdrucke, Objekt- oder Wertausdrucke, Regeln, die Wertausdrucken Typen zuordnen, und Regeln, die von Wertausdrucken einzuhalten sind (zusammen die **Typregeln**). Wertausdrucke (bzw. schlicht Ausdrucke, wenn es nicht um die Abgrenzung von Typausdrucken geht) kennen Sie schon: In Smalltalk sind es die in Kurseinheit 1, Kapitel 4.1 aufgefuhrten. Mit den anderen Konzepten werden Sie in den nachfolgenden Kapiteln vertraut gemacht, allerdings in weniger formaler Form, als Sie das nach dieser Definition vielleicht befurchten.

Warum aber typisiert man Variablen und andere Programmelemente?

**Grunde für die**

**Typisierung**

**Dafur gibt es mindestens vier gute Grunde:**

1. Typisierung regelt das Speicher-Layout.
2. Typisierung erlaubt die effizientere Ausfuhrung eines Programms.

3. Typisierung erhoht die Lesbarkeit eines Programms.
4. Typisierung ermoglicht das automatische Finden von logischen Fehlern in einem Programm.

Zu 1.: Der Compiler kann anhand des Typs einer Variable bestimmen, wie

**Speicher-Layout**

viel Speicherplatz er für die Aufnahme eines Wertes reservieren muss. Dies ist jedoch natur-

gemass nur für Variablen mit Wertsemantik relevant und daher für die objektorientierte Programmerung, insbesondere für Sprachen wie SMALLtalk (in denen Referenzsemantik vorherrscht), von untergeordneter Bedeutung.

Zu 2.: Wenn man weiss, dass die Werte einer Variable immer vom selben

Typ sind, also alle demselben Wertebereich entstammen, dann lassen sich

**Ausfuhrung**

bestimmte Optimierungen durchfuhren. Wenn man z. B. aufgrund der Deklaration einer Variabl **x** für gegeben annehmen kann, dass **x** nur ganze Zahlen enthalt, dann kann der Compiler für die übersetzung von **x** := **x** + 1 die Ganzzahalddition, ja sogar die Inkrement-Anweisung des Prozessors verwenden. Kennt der Compiler den Typ von **x** hingegen nicht, dann muss das Programm vor der Ausfuhrung der Addition erst prufen, von welchem Typ der Wert von **x** ist -- handelt es sich um eine Flie8kormazahl, so muss es zu der entsprechenden Operation verzweigen, handelt es sich womoglich um gar keine Zahl, dann muss es einen Laufzeitfehler signalsieren oder sich etwas ande einfallen lassen. Dem kann man entgegenhalten, dass im Falle der objektorientierten Programmerung selbst bei einer Typisierung aller Variablen gelegentlich noch Laufzeittests durchgefuhrt (oder andernfalls schwere Programmfehler in Kauf genommen) werden mussen, und dass sich die zur Optimierung bentigte Information auch anders als über explizite Typisierung von Variablen (namlich z. B. über die sog. _Typinferenz_, also die Ausnutzung impliziter Typinformation) gewinnen lasst.

Zu 3.: In der Vergangenheit hatten Variablen eher kurze, wenig selbster-

**enohte Lesbarkeit**

klarende Namen (vgl. dazu auch Kapitel 62 in Kurseinheit 7). Es ist dann sinnvoll, wenigstens an der Stelle der ersten Erwahnung der Variablen (in der Regel deren _Deklaration_) einen Hinweis darauf zu haben, wofur (fur welche Menge von Objekten) die Variable steht. Dies kann über einen Kommentar erfolgen, aber auch durch die Assoziation mit einem Typen, die aussagt, welcher Art die Werte der Variable sein mussen. Doch nicht nur Variablen-, auch Methodennamen können für sich genommen wenig aussagekraftig sein und durch die Verknupfung mit Typen aussagekraftiger gemacht werden: Eine Deklaration der Methode **next** etwa, die ListElement als Typ des Ein- und Ausgabeparameters deklariert, legt nahe, dass sie das in einer Liste auf den Eingabeparameter folgende Element zuruckliefert. Ohne die Angabe der Parametertypen musste man als Nutzerin der Funktion, die ihre Implementation nicht kennt, schon über ihren Zweck spekulieren. Dem mag man freilich entgegenhalten, dass man stattdessen ja auch selbsterklarende Namen für Variablen und Methoden vergeben konnte (mehr dazu in Kurseinheit 7, Kapitel 62).

[MISSING_PAGE_FAIL:165]

[MISSING_PAGE_FAIL:166]

Programmanalyse feststellbar), aber es lassen sich auch Falle konstruieren, in denen eine automatische Programmanalyse streiken muss.47

Was man jedoch immer tun kann, um Typkorrektheit zu gewahrleisten, ist, dass man zur Laufzeit vor einer Variablenzuweisung pruft, ob der zu- zuweisende Wert den von der Variable geforderten Typ hat. Diese sog. **dynamische Typprufung** (engl. dynamic type checking) hat jedoch den entscheidenden Nachteil, dass sie zu spat kommt, namlich zu einem Zeitpunkt, in dem man bereits nicht mehr viel anderes machen kann als einen Fehler zu signalsieren (der dann gunstigenfalls durch eine dafur vorgesehene Fehlerbehandlungsmethode aufgefangen wird, der aber in der Pravis haufig nur zu einem Programmabbruch fuhrt). Man kann jedoch argumentieren, dass auch letzteres immer noch besser ist, als mit falschen Werten weiterzuarbeiten und damit entweder einen Programmabbruch an einer anderen Stelle, die nicht mehr so leicht mit der fehlerhaften Wertzuweisung in Zusammenhang zu bringen ist48, in Kauf zu nehmen oder gar einen logischen Fehler, der überhaupt nicht erkannt wird.

Man beachte ubrigens, dass nach diesem Kriterium Smalltalk -- entge- gen haufig zu lesenden Behauptungen -- keine dynamische Typprufung SMalltalk, durchfuhrt, da Typfehler erst im letztmoglichen Moment offenbar werden, namlich wenn auf einer Variable eine Methode aufgerufen werden soll, die für das Objekt, auf das die Variable verweist, gar nicht definiert ist.49 Um das zu verhindern, findet man in Smalltalk-Code gelegentlich Figuren wie

Footnote 47: Aus theoretischer Sicht ist das Problem sogar unentscheidbar, auch wenn solche Aussagen in der Regel auf pathologischen Programmkonstruktionen, die man in der Pravis kaum vorfinden wird, basieren.

Footnote 48: Man denke etwa an die sog. _Null pointer exceptions_ in Java, die erst dann auftreten, wenn mit einem Variablenwert null tatsachlich etwas gemacht werden soll, was unter Umstanden erst am Ende einer langen Zuweisungskette der Fall ist.

Footnote 49: Smalltalk und andere Programmiersprachen werden gelegentlich als dynamisch typisiert (dynamically typed) bezeichnet. Das aber ist Unsinn, denn eine Typisierung findet in Smalltalk gar nicht, auch nicht zur Laufzeit, statt. Außerdem ist mit dynamischer Typisierung in der Regel dynamische Typprufung gemeint. Was ein dynamischer Typ sein soll, ist auch gar nicht klar.

Footnote 49: Smalltalk und andere Programmiersprachen werden gelegentlich als dynamisch typisiert (dynamically typed) bezeichnet. Das aber ist Unsinn, denn eine Typisierung findet in Smalltalk gar nicht, auch nicht zur Laufzeit, statt. Außerdem ist mit dynamischer Typisierung in der Regel dynamische Typprufung gemeint. Was ein dynamischer Typ sein soll, ist auch gar nicht klar.

Sehr viel nutzlicher als die dynamische Typprufung ist die statische **statische Typprufung** Typprufung, bei der, trotz aller theoretischen Hindernisse, die Typkorrektheit zur übersetzungszeit gewahrheistet werden soll. Die Typprufung ist damit Aufgabe des Compilers und nicht, wie im Fall der dynamischen Typprufung, Aufgabe des Lauzeitsystems oder gar der Programmiererin. Wie wir schon gesehen haben, bedeutet dies nicht weniger, als einen Beweis zu fuhren, dass bei keiner Austufhrung eines Programms eine Typinvariante verletzt wird. In der Praxis bedeutet dies aber, dass eine rein statische Typprufung immer auch Programme zuruckweist, die nutzlich, sinnvoll und typkorrekt sind (s. objies Beispiel der Zeilen 833 - 835, das zumindest typkorrekt ist: **i** erhalt niemals einen Wert vom Typ String). Zwar kann man versuchen, moglichst wenige typkorrekte Programme durch die statische Typprufung zuruckzuweisen, aber wie man sich leicht vorstellen kann, wird mit steigender Genauigkeit das dazu notwendige Typsystem immer aufwendiger und schwieriger zu benutzen, bis es irgendwann so kompliziert ist wie das Programm, dessen Fehler es entdecken soll (so dass man bei auftretenden Typfehlern erst einmal prufen muss, ob die Ursache tatsachlich in einem fehlerhaften Programm oder vielleicht nur in _fehlerhaften Typannotationen_ liegt).

So ist die Suche nach einem guten Typsystem immer die Suche nach einem guten Kompromiss. Die meisten heute in der Praxis verwendeten Typsysteme basieren auf einem solchen: einer statischen Komponente, die moglichst viele Fehler findet, ohne dabei die Programmiererin allzu sehr einzuschranken, und einer dynamischen Komponente, die den Rest erledigt. Eine erwahnenswerte Ausnahme davon macht C++: hier wird, zugunsten von Performanz (Speicherplatz und Geschwindigkeit), auf eine dynamische Komponente der Typprufung vollstandig verzichtet. Da die statische Typprufung von C++ aber nicht alles abdeckt, sind C++-Programme auch nicht automatisch typkorrekt. Mehr dazu in Abschnitt 51.5.

## 19 Deklaration, Definition und Verwendung von Programmelementen

Programme bestehen aus Schlusselwortern und -zeichen sowie aus Programmelementen, deren Namen, die sogenannten Bezeichner, frei vergeben werden können. Viele Programmisprachen verlangen, dass man diese Programmelemente vor der ersten Verwendung wereinbart oder deklariert. Durch eine solche **Deklaration** gibt man dem Compiler den Bezeichner bekannt; er kann ihn in der Folge wiedererkennen und mit der Deklaration in Verbindung bringen.

Bei der **Definition** wird dem Bezeichner das zugeordnet, wofur er steht.

Im Falle einer Variable ist das eine bestimmte Stelle im Speicher, die gensignatur

nugend Platz bietet, um den Wert der Variable aufzunehmen. Im Falle einer Methode sind es die Anweisungen, die durch die Methode zusammengefasst werden. Nicht selten (aber immer abhangig von der Programmisprache) erfolgen Deklaration und Definition in einem

[MISSING_PAGE_FAIL:169]

## 20 Typdefinitionen und deren Verwendung

Damit durch ein Typsystem Fehler ausgeschlossen werden können, die auf der Voraussetzung von Eigenschaften von Objekten beruhen, die diese gar nicht haben (also beispielsweise der Verwendung von Nicht-Zahlen in arithmetischen Ausdrucken), muss bekannt sein, welche Eigenschaften einem Typ und damit seinen Elementen zugeordnet sind. Im Fall von SMALLIALK sind die Eigenschaften, die mit einem Objekt verbunden werden können, schnell gefasst: Es handelt sich einfach um die Menge der Methoden, die es versteht, also um sein _Protokoll_ (s. Abschnitt 4.3.8 in Kurseinheit 1). Ein solches Protokoll definiert einen Typ: Er umfasst die Menge der Objekte, die über das Protokoll verfugen.

Wenn man nun eine Variable mit einem solchen Protokoll als Typ typisiert und das Programm typkorrekt ist, dann ist garantiert, dass jede Methode, die im Protokoll enthalten ist und die auf der Variable aufgerufen wird, auch für den Inhalt der Variable, das referenzierte Objekt, definiert ist. Typfehler, also Fehler der Sorte,,does not understand" (s. Abschnitt 4.3.2 in Kurseinheit 1), treten dann nicht mehr auf.

\begin{tabular}{c c}  & **Typen als Teile von** \\  & **Typdefinitionen** \\  & **Typdefinitionen** \\  & **T**ekt liefert) und deswegen selbst, genau wie Variablen, typisiert werden sollte. Protokolle definieren also nicht nur Typen, sie verwenden auch selbst welche, namlich indem sie die Typen der Ein- und Ausgabeobjekte spezifizieren. Ein einfaches Beispiel für eine Typdefinition, die selbst Typen verwendet, ist die folgende: \\
844 name ^ & <String> \\
845 name: einName <String> ^ & <Self> \\
846 alter ^ & <Integer> \\
847 alter: einAlter <Integer> ^ & <Self> \\ \end{tabular}

Wie schon bei einer temporaren Variable, stehen die _Typannotationen_ von formalen Parametern in STRONGTALK in spitzen Klammern dahinter. Diese Schreibweise sollten Sie nicht allzu sehr verinnerlichen, da andere Programmiersprachen die spitzen Klammern zur Kennzeichnung von Typvariablen (in Kapitel 29 behandelt) verwenden. Der Ruckgabetyp einer Methode wird durch ein vorangestelltes Dach (*) gekennzeichnet und folgt auf den letzten Parameter. Da es in SMALLIALK keine Methoden gibt, die nichts zuruckgeben (eine Methode ohne explizite Ruckgabeanweisung gibt in SMALLIALK ja immer das Emfangerobjekt zuruck), muss auch immer ein Ruckgabetyp angegeben werden. Ist dies der Typ selbst, kann der Name **Self** verwendet werden. Es handelt sich dabei gewissermansen um eine **Pseudo-Typvariable** (entsprechend der Pseudovariable **self**, deren Typ sie darstellt).

Falls Sie sich wundern, dass obige Zeilen kein Schlusselwort zur Einleitung **Typdefinitionen** \\  & **Typdefinitionen** \\  & **Typdefinitionen** \\  & **interaktives, browser-gestutztes System, in dem Typen in Formulare eingetragen und nicht in Textdateien spezifiziert werden. Gleichwohl faltt auf, dass innerhalb der Typdefinition inden spitzen Klammern (also da, wo Typen stehen sollen) keine Typdefinition auftauchen, sondern Namen. Und tatsachlich wird in STRONGtalk jeder Typ benannt (in seiner Typdefinition mit einem Namen versehen). Im folgenden werden Typen, ahnlich wie Klassen, in tabellarischer Form notiert. Der Typ Person etwa mit obigem Protokoll liest sich dann wie folgt:

\begin{tabular}{l} \hline Typ \\ \hline Protocol \\ \hline
848 name \({}^{\Lambda}\) <String> \\
849 name : einName <String> \({}^{\Lambda}\) <Self> \\
850 alter \({}^{\Lambda}\) <Integer> \\
851 alter : einAlter <Integer> \({}^{\Lambda}\) <Self> \\ \hline
**Selbstestestaufgabe 20.1** \\ \hline Definieren Sie den Typ Boolean gemass obigem Schema! \\ \hline \end{tabular}

In STRONGtalk ist die Protokollbildung der einzige sog. **Typkonstruktor**, **Typkonstruktoren** d. h., das einzige Sprachkonstrukt, mit dem man neue Typen definieren kann. Andere Programmiersprachen sehen ein reichhaltigeres Angebot vor: In Pascal beispielsweise gibt es die Typkonstruktoren **record**, **array of, set of**, file of**, Zeiger auf (\({}^{\Lambda}\)) sowie Aufzahlungen (enumerations) und Teilbereiche (ranges). In C++ gibt es u. a. class und struct (entsprechend **record** in Pascal), Java, C# und Eiffel bieten auch jeweils verschiedene Typkonstruktoren an. für eine puristische Sprache wie Smalltalk bzw. STRONGtalk reicht jedoch einer vollkommen aus.

Wie man leicht einsieht, gibt es in STRONGtalk keine primitiven Typen, also keine Typen, deren Definitionen nicht selbst auf einen oder mehrere Typen zuruckgefuhrt werden musste. Daran ruhrt auch die Optionalitat der Annotierung nichts: Selbst wenn man eine _Typannotation_ weglast (was immer erlaubt ist), hat die entsprechende Variable bzw. der Ruckgabewert der Methode einen Typ, nur wird er an dieser Stelle nicht angegeben. Das wirft naturlich die Frage auf, wie man Typen unter zwangslawfiger Selbstbezuglichkeit überhaupt eine Bedeutung beimessen kann.

### Induktiver Aufbau von Typen und Semantik

Um diese Frage zu beantworten, ist es zunächst interessant, festzustellen, dass es Typen gibt, die sich ausschliesllich auf sich selbst beziehen, deren Bedeutung also zumindest nicht von der anderer Typen abhangt. Das klassische Beispiel hierfur ist Boolean: Alle seine Operationen fordern den Typ Boolean als Operanden und haben Boolean als Typ zum Ergebnis. Aber woher erhalt Boolean seine Bedeutung?Eine eher theoretisch relevante Moglichkeit, solchen nur auf sich selbst beruhenden Typen eine Bedeutung zu geben, ist, sie auf bekannte externe Formalismen abzubilden. Im Beispiel von **Boolean** ist dies naturlich die _boolesche Algebra_. Jede, die die boolesche Algebra kennt und akzeptiert, wird auch den Typ **Boolean** sofort verstehen und akzeptieren (so er den den Erwartungen entsprechend definiert ist). Entsprechend lasst sich ein Typ **Fraction** mit den Operationen **+**, -**, \(\star\) und / definieren, Wikipedia der die rationalen Zahlen mit den entsprechenden Operationen reprasentiert. Nimmt man dann noch **Boolean** als mit Bedeutung (Semantik) versehen an, kann man noch Vergleichsoperationen wie =, >, \(\star\) etc. hinzufugen, ohne in Interpretationsprobleme zu laufen. Andere Typen, für die es eine solche direkte Abbildung nicht gibt, die aber in ihrer Definition rekursiv auf solche Typen zuruckgefuhrt werden können, kann man,,induktiv über deren Aufbau" eine Bedeutung beimessen. Man nennt eine solche Art des Versehens mit Bedeutung eine _denotationale Semantik_.

Eine andere, für die praktische Programmierung relevantere Moglichkeit ist, einen Typ und seine Operationen auf Anweisungen einer (gedachten

**Sepantik**

oder realen, Hauptsache wohlspezifiziierten) Maschine abzubilden. Die Abbildung für Basistypen wie **Rational** oder **Boolean** ist in der Programmiersprache bzw. deren Compiler gewissermassen hart verdrahtet. für von der Programmiererin definierte Typen kann sie dies hingegen nicht sein; deren Bedeutung kann aber vom Compiler, wiederum,,induktiv über deren Aufbau", aus der Bedeutung von Typen, die eine vorgegebene Semantik haben, abgeleitet werden. Man nennt dies dann auch eine _operationale Semantik_.

Man beachte, dass es für beide Arten der Semantik notwendig ist, dass sich alle Typen auf solche zuruckfuhren lassen, deren Bedeutung vorausgesetzt werden kann. Es gibt also kein vollstandig in sich selbst definiertes, von Extenem umabhangiges System. Selbst Smalltalk bzw. Strongtalk ist kein solches: Auch wenn die Implementierung von **Boolean** nicht,,hart verdrahtet", sondern auf dynamisches Binden abgewalzt wird, so sind dafur aber mindestens die beiden Wahrheitswerte **true** und **false** dem System bekannt, und **Integer** und **Float** (nicht jedoch **Fraction**!) sind,,fest verdrahtet", inklusive der Vergleichsrelationen (die ja die Wahrheitswerte zum Ergebnis haben).

Wenn Sie Kurs 01661 (,,Datenstrukturen") bereits belegt haben oder **Zusammenhang mit** ahnliches Vorwissen besitzen, dann erinnert Sie obliges Schema von **abstrakten** Typdefinitionen vielleicht an die Schreibweise abstrakter Datentypen.

Auch dort wird ein Typ syntaktisch als eine Menge von Operationen (Funktionen) beschrieben, deren Operanden (Argumente) alle selbst typisiert sind. Es gibt jedoch mindestens zwei wichtige Unterschiede zwischen den Signaturen eines abstrakten Datentyps und dem Protokoll eines Strongtalk-Typs:

1. Abstrakte Datentypen sind nicht objektorientiert in dem Sinne, dass die Objekte keinen Zustand haben und bei Operationen (Funktionen) die Objekte, auf denen die Operationen ausgefuhrt werden, nicht ihren Zustand wechseln. Stattdessen geben Operationen neue Objekte zuruck. Die Objekte der abstrakten Datentypen sind also gewissermassen alle unveränderlich (vgl. Kurseinheit 1, Abschnitt 4.3.5).

2. Entsprechend haben die den Methoden eines Protokolls entsprechenden Funktionen in den Spezifikationen abstrakter Datentypen immer ein Argument mehr, und zwar vom Typ des Datentyps selbst. Dieses Argument enspricht in der objektorientierten Programmierung dem Nachrichtenempfanger, dem impliziten Parameter self.

Der Bezug zu abstrakten Datentypen ist auch eine beliebte Moglichkeit, Typen einer Programmiersprache mit einer Semantik zu versehen.

### Verwendung definierter Typen

Definierte Typen können in Programmen verwendet werden, in STRONGTalk bei der Deklaration von (anderen) Typen, von Variablen, von Blocken und von Methoden. Man spricht dann von einer **Typisierung** der deklarierten Programmelemente. Die Verwendung in Typdefinitionen haben Sie ja oben bereits kennengelernt, die Verwendung in Methoden verlauft analog. Variablen (Instanzvariablen, tempororear Variablen etc.) werden in STRONGTalk genau wie formale Parameter (die ja auch Variablen sind) typannotiert, namlich durch Hintanstellung eines in spitzen Klammern eingeschlossenen Typnamens. Bei Blocken taucht der Ruckgabetyp im selben Segment wie die formalen Parameter auf, also vor dem Separator |. Die vollstandig typannotierte Klasse Stack aus Abschnitt 8.2 sieht in STRONGTalk beispielsweise so aus:

\begin{tabular}{l l} \hline \hline Klasse & Stack \\ \hline benannte Instanzvariablen & stackcontent \textless Array\textgreater{} \\  & stackpointer \textless Integer\textgreater{} \\  & indizierte Instanzvariablen & nein \\ \hline \hline
**1852** & push: anElement \textless{} Object\textgreater{} A \textless{} Self\textgreater{} \\
**1853** & "left neues Element auf Stapel" \\
**1854** & stackpointer := stackpointer + 1. \\
**1855** & stackcontent at: stackpointer put: anElement \\
**1856** & pop A \textless{} Self\textgreater{} \\
**1857** & "entferent oberstes Element vom Stapel" \\
**1858** & stackpointer := stackpointer - 1 \\
**1859** & top A \textless{} Object\textgreater{} \\
**1860** & "liafert oberstes Element des Stapels" \\
**1861** & stackcontent at: stackpointer \\ \hline \end{tabular}

Ein Beispiel für einen typisierten Block finden Sie in Abschnitt 29.3, Codzeile 950.

[MISSING_PAGE_FAIL:174]

hingegen nicht. lst eine Zluweisung zulassig, dann spricht man auch von einer **Zuweisungskompatibilitat** der beteiligten Typen. Die für das Programmieren relevante Implikation ist allerdings die umgekehrte: Wenn zwei Typen zuweisungskompatibel sind, dann gilt, dass eine entsprechende Zuweisung zulassig ist, also zu keiner Verletzung einer Typinvariante fuhrt. Wie Sie noch sehen werden, verlangt Zuweisungskompatibilitat keinesweg identische Typen; daraus ergibt sich aber eine sprachliche Uneindeutiqkeit, die zunächst behoben werden muss.

Dem Satz,**a** ist zuweisungskompatibel mit **b**" kann man nicht eindeutig

\begin{tabular}{c c}  & **Sprachgebrach;** \\ entnehmen, ob nun **a b** zugewiesen werden kann oder **b a**. Dass beides \\ geht, ist nur dann der Fall, wenn die beteiligten Typen aquivalent in einem noch zu bestimmenden Sinne sind, was aber, wie schon gesagt, nicht unbedingt der Fall sein muss. Im folgenden soll daher die Richtung der erlaubten Zuweisung so gelesen werden, dass beim Satz,**a** ist zuweisungskompatibel mit **b**" die Zuweisung **b** := **a** zulassig ist. Die umgekehrte Richtung, **a** := **b**, kann ebenfalls zulassig sein; dies wird durch den Satz jedoch nicht ausgesagt. Zuweisungskompatibilitat ist ubrigens (in der Regel) eine transitive Eigenschaft: Wenn **a** zuweisungskompatibel mit **b** ist und **b** zuweisungskompatibel mit **c**, dann ist auch **a** zuweisungskompatibel mit **c**.

\begin{tabular}{c c}  & **Zuweisungskompatibilitat bei** \\ \end{tabular}

\begin{tabular}{c c}  & **Methodenaufrufen** \\ \end{tabular}

\begin{tabular}{c c}  & **Zuweisungskompatibilitat bei** \\ \end{tabular}

\begin{tabular}{c c}  & **Methodenaufrufen** \\ \end{tabular}

\begin{tabular}{c c}  & **Zuweisungskompatibilitat bei** \\ \end{tabular}

\begin{tabular}{c c}  & **Methodenaufrufen** \\ \end{tabular}

\begin{tabular}{c c}  & **Zuweisungskompatibilitat bei** \\ \end{tabular}

\begin{tabular}{c c}  & **Methodenaufrufen** \\ \end{tabular}

\begin{tabular}{c c}  & **Zuweisungskompatibilitat bei** \\ \end{tabular}

\begin{tabular}{c c}  & **Methodenaufrufen** \\ \end{tabular}

\begin{tabular}{c c}  & **Zuweisungskompatibilitat bei** \\ \end{tabular}

\begin{tabular}{c c}  & **Methodenaufrufen** \\ \end{tabular}

\begin{tabular}{c c}  & **Zuweisungskompatibilitat bei** \\ \end{tabular}

\begin{tabular}{c c}  & **Methodenaufrufen** \\ \end{tabular}

\begin{tabular}{c c}  & **Zuweisungskompatibilitat bei** \\ \end{tabular}

\begin{tabular}{c c}  & **Methodenaufrufen** \\ \end{tabular}

\begin{tabular}{c c}  & **Zuweisungskompatibilitat bei** \\ \end{tabular}

\begin{tabular}{c c}  & **Methodenaufrufen** \\ \end{tabular}

\begin{tabular}{c c}  & **Methodenaufrufen** \\ \end{tabular}
Mengen der Methodensignaturen gleich sind. Man spricht in diesen Fallen von einer **Typaquivalenz**.

Von der Typaquivalenz gibt es zwei Arten: die **nominale** (sich auf den Namen beziehende) Typaquivalenz, auch **Namensaquivalenz** genannt, und die **strukturelle** Typaquivalenz, auch als **Strukturaquivalenz** bezichnet. Wahrend die nominale Typaquivalenz verlangt, dass zwei Deklarationen (beispielsweise von Variablen) dieselben Typen anfuhren, damit Zuweisungskompatibilitat vorliegt, kommt es bei der strukturellen Typaquivalenz lediglich darauf an, dass die Typen paarweise gleich definiert sind (also die gleichen Eigenschaften von ihren Werten verlangen), die Typen sich also in ihrer Struktur, aber nicht unbedingt in ihren Namen gleichen.

Typaquivalenz ist eine symmetrische Eigenschaft: Wenn ein Typ A (nominal oder strukturell) aquivalent zu einem Typ B ist, dann ist B genauso aquivalent zu A. Die Reflexivitat der Typaquivalenz, also dass jeder Typ aquivalent zu sich selbst ist, ergibt sich von selbst. Ausserdem ist Typaquivalenz transitiv: Wenn A (nominal oder strukturell) aquivalent zu B ist und B in der gleichen Art aquivalent zu C, dann ist auch A aquivalent zu C (und, aufgrund der Symmetrie, C aquivalent zu A).

### Strukturaquivalenz

Um strukturelle Typaquivalenz festzustellen, werden die Definitionen der beteiligten Typen _rekursiv expandiert_, was soviel hei8t wie dass in einer Typdefinition vorkommende Namen anderer Typen durch ihre Struktur ersetzt werden. Nimmt man beispielsweise die Typdefinitionen

```
TypPerson
```
870sitzA<Wohnung>
871sitz:einWohnnsitz<Wohnung>A<Self>

```
TypWohnung
872strasseA<String>
873strasse:einStrasse<String>A<Self>
874ortA<String>
875ort:einOrt<String>A<Self>
```

```
TypFirma
976sitzA<Buro>
987sitz:einFirmensitz<Buro>A<Self>
```

``` TypBuro* 878straSe ^^<String>
* 879straSe: einStrasSe <String> ^<Self>
* 880ort ^<String>
* 881ort: einOrt <String> ^<Self>

dann sind die Typen Person und Firma sowie Wohnung und Buro jeweils strukturaquivalent, aber nicht namensaquivalent. Bei der Strukturaquivalenz haben Namen also lediglich die Funktion der abkurzenden Schreibweise, bei der Namensaquivalenz hingegen auch eine von der Struktur unabhangige Bedeutung. Namensaquivalenz impliziert Strukturaquivalenz, aber nicht umgekehrt; Namensaquivalenz ist somit das starkere Konzept.

Strukturaquivalenz als Bedingung der Zuweisungskompatibilitat reicht
* 89stuarkturaquivalenz als 100igsche und Laufzeitfehler, die auf der Annahme
* 90stuarkturaquivalenz
* 91en nicht vorliegenden Eigenschaft (Methode) bei einem Wert einer Variable basieren, zu verhindern. Sie garantiert, dass die Methode eines Programms auf den jeweiligen Empfangerobjekten mit den geforderten Parameterobjekten auch durchgefuhrt werden können. So kann z. B. bei erfolgreicher Typprufung (und daher vorliegender Typkorrektheit) ohne Kenntnis der konkreten Inhalte der Variablen sichergestellt werden, dass bei Vorliegen der Deklaration p <Person> der Ausdruck
* 892p.sitzstraSe: 'HeimatstraSe'

keine Typfehler produziert, und gleichzeitig der Ausdruck
* 893p.sitz: 'zuhause'

schon zur übersetzungszeit als fehlerhaft zuruckgewiesen wird, da er zu einer Variablenfehlbelegung (die in Smalltalk noch problemlos moglich gewesen ware) fuhrt. Man beachte, das letztere sogar zu einer Speicherschutzverletzung fuhren konnte, wenn die Variable p -- wie in vielen Sprachen mit Typsysteme -- Wertsemantik hatte, namlich dann, wenn der übergebene String grosser ist als der zur Aufnahme der Wohnung vorgesehene Speicherplatz.

Strukturaquivalenz ist eine rein syntaktische Bedingung. Insbesondere
* 11Type branding
* 12können bei geforderter Strukturaquivalenz Typen zufallig zuweisungskompatibel sein, die inhaltlich überhaupt nichts miteinander zu tun haben. Dadurch können Objekte, die eigentlich getrennten Typen (disjunkten Wertebereichen) angehoren, über Kreuz und über die Typgrenzen hinweg zugewiesen werden. _Semantische Fehler_ sind also immer noch moglich. Man trifft daher in Sprachen mit Strukturaquivalenz gelegentlich die Pravis an, jedem Typ eine für ihn charakteristische Methode exklusiv zuzuordnen, so dass er mit keinem anderen mehr strukturaquivalent ist. Diese Technik nennt man **Type branding**.

### Namensaquivalenz

Nun können Typen neben ihrer formalen Funktion, Fehler zu vermeiden, noch eine inhaltliche, namlich eine _Filterfunktion_ austfullen. Diese setzt allerdings voraus, dass dem Typ auch eine Bedeutung, die über seine blosse Struktur (seine Syntax) hinausgeht, beigemessen werden kann. Dies geschieht heute vor allem durch die Benennung des Typs, die dann, gepaart mit Namensaquivalenz als Bedingung der Zuweisungskompatibilitat, verlangt, dass einer Variable nur Werte gleicher Bedeutung zugeweisen werden können. Eine Zuweisung einer Wohnung an ein Buro oder umgekehrt ist dann, trotz im obigen Beispiel strukturell gleich definierter Typen und deswegen ausbleibenden Typfehlern, aufgrund fehlender Namensgleichheit ausgeschlossen, was auch sinnvoll ist, da es sich dabei mit einer gewissen Wahrscheinlichkeit um einen logischen Programmierfehler handelt, der auf mechanische Art sonst kaum zu entdecken ware. Die Filterfunktion der geforderten Namensaquivalenz druckt also eher eine Absicht der Programmiererin aus denn eine technische Notwendigkeit. Die Bedeutung gerade dieser Funktion sollite man jedoch nicht unterschatzen -- nur wenige Moglichkeiten, Fehler in einem Programm aufzudecken bzw. zu vermeiden, sind so einfach zu haben.

Ein der Typprufung per Namensaquivalenz ahnliches Prinzip kommt ubri-

gens in der Physik zur Anwendung: Bei ihren Berechnungen fuhren Physikerinnen stets eine Art Typprufung durch, indem sie nicht nur mit den Betragen der physikalischen Grossen, sondern auch mit deren Einheiten rechnen. Wenn Physikerinnen also beispielsweise eine Geschwindigkeit berechnen und bei der Behandlung der Einheiten etwas anderes als m/s herauskommt, dann steckt im Rechenvorgang ein Fehler -- das Ergebnis hat nicht den richtigen Typ (die richtige Einheit) und ist deswegen mit hoher Wahrscheinlichkeit falsch.

Namensaquivalenz hat aber auch einen entscheidenden Nachteil: Sie

setzt voraus, dass getrennt voneinander entwickelte Programme zumindest an ihren Schnittstellen (also da, wo Objekte ausgetauscht werden) dieselben Typen verwenden. Dies kann für die Interoperabilitat von getrennt voneinander entwickelten Programmen (wie z. B. Web services) ein echtes Hindernis sein.

Strukturele Typaquivalenz bietet mehr Flexibilitat als nominale: Sie erlaubt Aquivalenz von Typen, bei deren Definition man vom jeweils anderen nichts wusste. Die erhohte Flexibilitat hat jedoch ihren Preis: Zufallige strukturelle über-einstimmungen können zu einer Aquivalenz fuhren, die nicht der intendierten Semantik entspricht. _Type branding fuhrt_ in solchen Fallen eine Namensaquivalenz durch die Hintertur ein, mit dem Vorteil, dass diese optional ist.

## 23 Typerveiterung

Wie bereits in Kapitel 21 angedeutet, verlangt die Zuweisungskompatibilitat nicht unbedingt Typaquivalenz. Tatsachlich reicht es ja, bei einer rein strukturellen (syntaktischen) Betrachtung, voll aus, dass der Typ der rechten Seite einer Zuweisung das Protokoll (die Menge der Methoden) des Typs der linken Seite enthalt, um in der Folge Typfehler zu vermeiden. Anders ausgedruckt: Der Typ auf der rechten Seite einer Zuweisung darf eine Erweiterung dessen auf der linken Seite um zusatzliche Methoden sein.

Die sog. **Typerveiterung** (engl. type extension; extension hier im Sinne von Erweiterung und nicht im Sinne der Ausdehnung als Gegenstuck zur Intension; vgl. Abschnitt 7.1 in Kurseinheit 2), wie sie z. B. in den Programmiersprachen Modula-3 und Oberon (beides Nachfolger von Pascal) Verwendung findet, sieht genau dies vor. Eine Typerveiterung des obigen Typs Buro um ein Landerkennzeichen sieht dann beispielsweise wie folgt aus:

\begin{tabular}{c|c} \hline Typ & InternationalesBuro \\ erweiterter Typ & Buro \\ \hline Protokoll & \\ \hline
884 & landerkennzeichen \({}^{\star}\) \textless String\textgreater{} \\
885 & landerkennzeichen: einlanderkennzeichen \textless String\textgreater{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasci{} \textasciasci{} \textasci{} \textasciasci{} \textasciasci{} \textasciasciasci}{{} \textasci}{ \textasciasci}{ } \textasci{} \textasciasci{} \textasciasciasciasci}{{} \textasci}{ \textasci}{ \textasci}{ \textasciasci}{} \textasciasciasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasciasci}{} \textasciasciasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci} \textasciasciasciasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{ \textasci}{\textasci}{ \textasci}{ \textasci}{\textasciasci}{ \textasci}{ \textasci}{ \textasci} \textasciasciasci{} \textasciasciasciasci}{ \textasci}{ \textasci}{ \textasci}{\textasci}{ \textasci} \textasciasciasci{} \textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci} \textasciasciasci{} \textasciasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci} \textasciasciasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci} \textasci}{\textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci} \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci} \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci} \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{ \textasci}{\textasci}{ \textasci} \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{ \textasci}{\textasci}{ \textasci}{ \textasci}{\textasci}{ \textasci}{ \textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{ \textasci}{\textasci}{ \textasci}{\textasci} \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{ \textasci}{\textasci}{ \textasci} \textasci}{\textasci}{ \textasci}{ \textasci}{\textasci}{ \textasci}{\textasci} \textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{ \textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{ \textasci} \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{ \textasci}{\textasci}{ \textasci}{\textasci} \textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci} \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci} \textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{\textasci} \textasci}{\textasci}{ \textasci}\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}\textasci}{\textasci}{ \textasci}{\textasci}{ \textasci}{\textasci}{\textasci}{schlichtweg für das Objekt nicht definiert sind. Die Zuweisungskompatibilitat unter Typeweiterung regelt der Begriff der Typkonformitat.

## 24 Typkonformitat

Einen Typ, dessen Definition alle deklarierten Elemente der Definition eines anderen Typen enthalt, nennt man mit dem anderen **typkonform**. So ist **InternationalesBuro** im obigen Beispiel mit **Buro** typkonform. Typkonformitat ist in vielen Sprachen eine notwendige und hinreichende Voraussetzung für die _Zuweisungskompatibilitat_: Es darf dann ein Objekt vom Typ **InternationalesBuro** einer Variable vom Typ **Buro** zugewiesen werden.

Typkonformitat ist aberreflexiv, d. h., jeder Typ ist konform zu sich selbst.

Sie ist weiterhin transitiv: Wenn A typkonform zu B ist und B typkonform

**Zu C, dann ist auch A typkonform zu C. Wie man sich leicht denken kann,**

ist die Typkonformitat jedoch im Gegensatz zur Typaquivalenz nicht symmetrisch: Aus der Tatsache, dass ein Typ B typkonform zu einem Typ A ist, folgt nicht, dass auch A typkonform

zu B ist. Vielmehr ist dies mit einer kleinen Ausnahme sogar zwingend nicht der Fall: Typkonformitat ist meistens antisymmetrisch, was sovi heisst wie dass wenn B zu A und A zu B typkonform ist, dass dann A und B identisch sein mussen.

Von der Typkonformitat gibt es, genau wie von der Typaquivalenz, zwei Varianten, namlich eine **strukturele Typkonformitat** und eine namensgebundene (**nominale) Typkonformitat**. Zur strukturellen Typkonformitat reicht es aus, wenn der konforme Typ wie oben alle Elemente des Typs, zu dem er konform sein soll, enthalt: Der Typ mit der Definition

\begin{tabular}{l} \hline Typ \\ \hline \end{tabular}

* 886stra8e ^ <String>
* 887stra8e: einStrasse <String> ^ *Self>
* 888ort ^ <String>
* 889ort: einOrt <String> ^ *Self>
* 890landerkennzeichen ^ <String>
* 891landerkennzeichen: einLanderkennzeichen <String> ^ *Self>

ist also zum Typ **Buro** strukturell konform. für die nominale Konformitat muss zusatzlich und explizit die Enweiterung eines (oder Ableitung von einem) anderen Typ angegeben werden: die Definition von **InternationalesBuro** aus Kapitel 23 ist also mit **Buro** nicht nur strukturell, sondem auch nominal konform. Da bei der Erweiterung alle Elemente des Typs, der erweitert wird, beim erweiternden erhalten bleiben, folgt die Konformitat aus der Erweiterung.

[MISSING_PAGE_FAIL:181]

tiblilitat. Interessantwerweise wurde Strongtalk, das ursprunglich ein auf struktureller Kondrmitat beruhendes Typsystem (inkl. Type branding) hatte, inzwischen auf nominale Typkonformitat umgestellt. Als Begrundung wurde angefuhrt, dass ein strukturelles Typsystem, insbesondere eines, bei dem Typen nicht explizit benannt werden, es der Programmiererin nicht erlaubt, ihre Absicht (intendierte Semantik, die obengenannte Filterfunktion) auszducken, was Programme schwerer zu lesen und zu debuggen macht, und dass die Fehlermeldungen, die eine strukturelle Typprufung produziert, sich oft nicht auf die eigentliche Fehlerquelle beziehen und sehr schwer zu verstehen sind [Stronstalk 2.0].

Fragen der Zuweisungskompatiblilitat unter Typweiterung spielen ubringens auch bei Funktionsaufrufen, bei denen ja _implizite Zuweisungen_ aufreten (s. Abschnitt 4.3.2), eine wichtige Rolle. So muss bei dem Ausdruck

895 a := self m: e der Typ von e eine Erweiterung des in m für den Parameter geforderten Typ sein und der Ruckgabettyp von m eine Erweiterung des Typs von **a**.

## 25 Typeinschrankung

Typerveiterung ist nicht die einzige Moglichkeit, auf der Basis eines bereits bestehenden einen neuen, verwandten Typen zu erzeugen; Typeinschrankung ist eine andere.

Eine erste, offensichtliche Form der Typeinschrankung liegt dann vor, wenn ein Typ auf Basis eines anderen unter Entferren von Eigenschaften (Methoden) definiert wird (das Beispiel vom Pinguin als einem Vogel, der nicht fliegen kann, kennen Sie ja bereits aus Kurseinheit 1, Abschnitt 9.2; das Beispiel vom Quadrat als einem Rechteck, das nur eine Kantenlange braucht, ist ein anderes). Diese Form der Typeinschrankung stellt zumindest auf Ebene der Typdefinition (der Intensionen) die Umkehrung der Typerveiterung dar. Es liegt auf der Hand, dass diese Form der Typeinschrankung nicht zur Zuweisungskompatiblilitat fuhrt; dies folgt schon aus der fehlenden Symmetrie der Typkonformitat. Sie soll hier deswegen keine weitere Berucksichtigung finden, auch wenn es Sprachen gibt, die sie erlauben (z. B. Eiffel).

Eine unter dem Gesichtspunkt der Zuweisungskompatiblilitat interessantere Form der Typeinschrankung besteht darin, die verwendeten Typen einer Typdefinition durch andere, speziellere zu ersetzen (ohne hier schon zu sagen, was _spezieller" im Zusammenhang mit Typen bedeutet). Diese Form der Typeinschrankung ergibt sich auf naturliche Weise, wenn man sich den Zusammenhang von Extensionen von definierten Typen und solchen, die in Typdefinitionen vorkommen, ansieht.

Das Ganze soll an einem Beispiel verdeutlicht werden. Man denke sich einen Typ Dokument wie folgt definiert:
Fur die Dauer eines Ausdrucks wird durch die Methode druckenAuf : ein konkretes Dokument einem konkreten Drucker zugeordnet. Mengentheoretisch betrachtet ist diese Zuordnung eine Relation zwischen zwei Mengen:

Nun gibt es verschiedene Arten von Dokumenten und Druckern: Man kann z. B. bei Dokumenten zwischen Texten und Diagrammen unterscheiden und bei Druckern zwischen Zeilendruckern und Plottern. Die Extensionen entsprechender Typen sind dann jeweils Teilmengen der Extensionen von Dokument und Drucker.

Weiterhin ergibt es sich aus der Natur der Sache, dass man Diagramme nur auf Plottern drucken sollte und Texte nur auf Zeilendruckern. Dies geht konform zur obigen Betrachtung eines Methodenaufrufs als Relation: Wenn man die Menge einer Stelle einer Relation wie der obigen auf eine Teilmenge einschrankt, dann schrankt sich dadurch in der Regel auch die Menge der anderen Stelle auf eine Teilmenge ein:

Die andere Menge kann auch gleichbleiben; grosser wird sie jedoch nie.

Es ergibt sich daraus die folgende Definition eines Typs **Zeichnung** als Typeinschrankung von Dokument:
Man beachte, dass die Methode druckenAuf: nicht hinzugefugt wurde -- sie ersetzt vielmehr die von Dokument übernommene. So unterscheidet sich die Methode von der ursprunglichen auch nur in der _Typennotation_ des formalen Parameters. Man spricht in diesem Zusammenhang von einer **Redefinition** der Methode (an den ebenfalls dafur verwendeten Begriff des _überschreibens_ sind je nach Programmiersprache andere Bedingungen geknupft). Die Methoden name und name : werden ubrigens, genau wie bei der Typerveiterung, bei der Typeinschrankung übernommen, solange nichts andere susgesagt wird.

Man mag sich fragen, warum bei der Typerveiterung in Kapitel 23 keine zwei Formen analog zur Typeinschrankung eingefuhrt wurden. Die Typerveiterung wurde damit zur vollstandigen Umkehrung der Typeinschrankung wie hier beschrieben. Wie sie noch sehen werden, ist das Ziel nicht die Schaffung zweier Komplementare, sondern die Vereinigung beider zu _einer_ Beziehung zwischen Typen -- dazu mussen sie aber in dieselbe und nicht in gegensatzliche Richtungen gehen. Außerdem ist eine Erweiterung des Wertebereichs bei Einschrankung des Definitionsbereichs nicht durch den Begriff der Relation wie oben erklarbar; eine wichtige Analogie zur Realitat, die durch Typen zwecks semantischer Prufung nachgebildet werden soll, ginge dmit verloren.

Nun ergibt sich aber bei der Typeinschrankung auch ohne Loschen das Problem, dass sie die Zuweisungskompatibilitat, die ja für die Typerveiterung noch per Typkonformitat geregelt werden konnte, aushebelt: Wenn man bei den obigen Typdefinitionen und den Deklarationen

9001d -->= z <Zeichnung> l <Zeilendrucker>

zunächst

901d := z

zuweist und dann weiter

902d druckenAuf: 1

aufruft, dann ware, Typkonformitat von Zeichnung und Dokument bzw. Zeilendrucker und Drucker vorausgesetzt, die Typprufung zwar erfolgreich (denn druckenAuf: verlangt für Dokument Drucker als Argumenttyp), aber zur Laufzeit soll nun eine Zeichnung auf einem Zeilendrucker gedruckt werden, was gemass der obigen Definition von Zeichnung nicht vorgesehen ist. Eine der beiden Zuweisungen, die explizite in 

[MISSING_PAGE_FAIL:185]

Subtyping und Inklusionspolymorphic

Die Einfuhrung von Typaquivalenz und Typkonformitat bezog sich bislang lediglich auf das Verhaltnis der Typdefinitionen, also der Intensionen der Typen. Die Frage des Zusammenhangs der Wertebereiche der Typen, also der Extensionen, ist dabei unberucksichtigt geblieben. Wenn aber die obige Definition von Typkorrektheit weiter Bestand haben soll, dann mussen die Werte zuweisungskompatibler Typen zum Wertebereich des Typen, an den zugewiesen werden soll, gehoren.

Zur Erinnerung: _Typannotationen_ stellen _Invarianten_ dar, die die moglichen Werte einer Variable beschranken. Diese Invarianten durfen durch Zuweisungen nicht verletzt werden. Wenn man aber nun Zuweisungen von einem anderen Typen zulasst, dann wird die Typkorrektheit nur dann nicht verletzt, wenn der Wertebereich des anderen Typen (seine Extension) in dem dessen, dem zugewiesen wird, enthalten (inkludiert) ist. Mit anderen Worten: Damit eine Zuweisung **a** := **b**, bei der sich die Typen von **a** und **b** unterscheiden, zulassig ist, muss die Extension des Typs von **b** eine Teilmenge der Extension des Typs von **a** sein.

Im Fall der Typerveiterung ist dies nicht automatisch der Fall. So handelt **mangelinde Teilmen-**es beispielsweise bei der Extension des Typs**

als Erweiterung von

nicht unbedingt um eine Teilmenge der Extension von ZweiDPunkt, denn es ist z. B. nicht klar, was das Ergebnis der Addition eines dreidimensionalen zu einem zweidimensionalen Punkt sein konnte -- geometrisch ist die Addition zweier Punkte unterschiedlicher Dimensionen jedenfalls nicht definiert.

Versuchen Sie, das Beispiel mit ZweiDPunkt und DreiDPunkt so zu retten, dass sowohl Typerweiterung als auch Inklusion von Extensionen darin vorkommt. Evtl. finden Sie in Kapitel 9 von Kurseinheit 2 nutzliche Hinweise.

Das Phanomen der mangelnden Extensionsinklusion bei Typerweiterung lasst sich darauf zuruckfuhren, dass dem erweiterten Typ (im Beispiel **Dokument**) eigene, d. h. nicht einer seiner Erweiterungen entstammende **Herstellung der Teilmengenbeziehung** **Dokument**) eigene, d. h. nicht einer seiner Erweiterungen entstammende **Dokument**) eigene, d. h. nicht einer seiner Erweiterungen entstammende **Herstellung der Teilmengenbeziehung** **Werte (Objekte) zugestanden werden. Ware die Extension eines erweiterten Typs als die Vereinigung der Extensionen seiner Subtypen (hier Text und Zeichnung) definiert, gabe es dieses Problem nicht. Dies ist ein sehr guter Grund dafur, dass Supertypen -- genau wie Generalisierungen (Kurseinheit 2, Kapitel 9) -- keine eigenen Objekte haben sollten (vgl. a. Abschnitt 26.1 und Kurseinheit 7, Kapitel 69).

Auch nicht selbstverstandlich ist die Teilmengenbeziehung bei der Typein-schrankung: Durch das Weglassen von Eigenschaften (Methoden) wird die Extension, also die Menge der Werte (Objekte), die darunterfallen, eher großer denn kleiner -- je weniger spezifisch die Menge der geforderten Eigenschaften ist, desto mehr Objekte fallen darunter. Die sich daraus ergebende Teilmengenbeziehung ware also eher die umgekehrte (die Extension des einschrankenden Typen enthalt die des eingeschrankten). Etwas anders sieht es aus, wenn durch Typeinschrankung (_Redefinition_) die Ein- oder Ruckgabettypen von Methoden beschrankt werden: Die Menge der Zeichnungen ist eine Teilmenge der Menge der Dokumente, auch weil sich Zeichnungen eben nur auf Plottern ausgeben lassen. Die Zuweisungskompatibilitat von Zeichnung mit Dokument ware also, was die Inklusion der Extensionen angeht, kein Problem.

Man konnte nun die Typerweiterung unter oben gemachter Einschrankung und die zweite Form der Typeinschrankung als in dieselbe Richtung **Einschrankung** **Zielende Maßnahmen** ansehen: Beide schranken Extensionen ein. Das lasst sich wie folgt erklaren: Wenn man einer Menge von Objekten, die durch eine Anzahl Attribute alle gleichermassen charakterisiert werden, weitere Attribute beimisst, dann schrankt man diese Menge ein, wenn die hinzugefugten Attribute nicht alle Objekte der Menge charakterisiern. Wenn man beispielsweise wie oben geschehen die Attributmenge des Typs Dokument um die Methode zeilen * *Collection> erweitert, dann fallen die Zeichnungen aus der durch Dokument beschriebenen Menge von Objekten heraus, weil sie keine Zeilen haben. Alternativ konnte man auch sagen, dass Dokumente grundsatzlich über Zeilen verfugen können, diese aber bei Zeichnungen immer in der Anzahl 0 vorliegen (also die entsprechende Collection immer leer ist; eine Typeinschrankung!), nurerscheint das weniger naturlich.51 Man beachte die Parallelitat zum Begriff der _Spezialisierung_ (Abschnitt 9.2 in Kurseinheit 2): Der durch Typerweiterung oder -einschrankung aus Dokument hervorgegangene Typ Zeichnung ist spezieller als seine Vorlage.

Footnote 51: Stattdessen würde man eher vermuten, dass es sich um einen Programmierfehler handelt, wenn jemand bei einer Zeichnung auf ihre Zeilen zugereifen will. Außerdem musste bei erster Annahme der allgemeinste Typ, von dem alle anderen abeleitet sind (**Object** in **Strongitalk**), immer alle Attribute deklarieren, die einem jemals in den Sinn kamen, und das ware nun wirklich unpraktisch.

Nun ergibt sich aber gemass obigem Beispiel (Zeilen 900-902) ein Sachverhalt, der trotz aller Harmonie von Typerweiterung und -einschrankung nicht weniger als den Verlust der Zuweisungskompatibilitat bedeutet. Dieser resultiert jedoch bei genauerer Betrachtung nicht daraus, dass Zeichnungen keine Dokumente waren, sondern aus der mit der Typkorrektheit verbundenen, impliziten Allquantifiziertheit von Typinvarianten: Eine Methodendeklaration

913druckenAuf; einDrucker <Drucker> ^ ^ <Self> im Protokoll eines Typs Dokument wird namlich interprereitert als,,druckenAuf : ist definiert für alle Empfangerobjekte vom Typ Dokument und Parameterobjekte vom Typ Drucker", was aber in dieser Allgemeinheit sachlich falsch ist.

Typsysteme mit Typinvarianten der hier vorgestellten Art sind nicht in der

**Dependent types**

Lage, andere als implizit allquantifizierte Aussagen über Wertebereiche zu treffen. Dies ist gewissermassen der Preis der Einfachheit. Abhiffe schaffen neuere Typsysteme wie die Idee von den _Dependent types_, wie sie beispielsweise in Scala zum Einsatz kommen: Hier man sich die Parametertypen von Methoden als Funktionen des Typs, zu dem die Methode bei hort, vorstellen. Der Parametertyp von druckenAuf : aus obigem Beispiel ware dann, in Abhangigkeit davon, ob die Methode auf einem Objekt vom Typ Dokument oder Zeichnung aufgerufen wird, Drucker oder Plotter. Wie man sich leicht vorstellen kann, ist die statische Prufung solcher Bedingungen (Invarianten) aber nicht so einfach.

Die Vereinigung von Typerweiterung und Typeinschrankung mit Zuweisungskompatibilitat und der daraus folgenden Typkorrektheit bietet der Begriff des Subtypes.

### Der Begriff des Subtypes

Ein **Subtyp** ist als ein Typ definiert, dessen Werte oder Objekte überall da auftauchen durfen, wo ein Wert des Typs, von dem er ein Subtyp ist, verlangt wird. Subtyp steht dabei nicht für eine besondere Art von Typ, sondern vielmehr für eine Rolle in einer Beziehung zwischen zwei Typen, namlich der **Subtyppenbeziehung**. Die Gegenrolle heisst **Supertyp**.

Man beachte, dass diese Definition von Subtypen Zuweisungskompatibilitat impliziert: Wenn die Objekte eines Subtypen überall da auftauchen

**bilitat von Subtypen**

durfen, wo Objekte seines Supertypen enwartet werden, dann durfen sie auch Werte vonVariablen sein, die mit dem Supertypen annotiert (auf Werte des Supertypen beschrankt) sind. Ein Subtyp ist also mit seinem Supertyp per Definition zuweisungskompatibel. Es steckt in dieser Definition aber eine gewisse Zirkularitat (Subtyp als Vorausetzung und Ergebnis der Zuweisungskompatibilitat), die eineinfachheit der Zusammenhange vortauscht, die es in Wirklichkeit nicht gibt; die eigentliche Frage, was namlich erfullt sein muss, damit ein Objekt eines Typen tatsachlich da erscheinen darf, wo ein Objekt eines anderen Typen verartet wird, bleibt unberucksichtigt. Eine Befassung mit dieser Frage erfolgt hier aber nur insoweit, wie dies heutige Typsysteme auch tatsachlich tun; eine genauere Betrachtung erfolgt dann erst in Kurseinheit 6, Kapitel 54.

Ein Subtyp kann selbst wieder Subtypen haben usw.; man spricht dann **Subtyphierachie** auch von einer **Subtyppen**- oder einfach nur von einer **Typhierarchie**. In einer solchen Hierarchie kann man **direkte** von **indirekten Subtypen** unterscheiden: Zwischen einem Typ und seinem direkten Subtyp liegt kein weiterer Typ in der Typhierarchie, bei einem indirekten Subtyp hingegen schon. Die Subtypenbeziehung ist transitiv und reflexiv; insbesondere ist also jeder Typ ein Subtyp von sich selbst (das folgt schon aus obiger Definition des Begriffs Subtyp). Die Frage der Symmetrieeigenschaft muss noch bis zum nachsten Abschnitt zuruckgestellt werden.

Je nach verwendetem Typsystem kann ein Typ auch mehrere direkte Supertypen haben. Die sich daraus ergebende Struktur ist dann aber keine **Thehrere direkte Supertypen**.

Hierarchie mehr (im strengen Sinne; man spricht aber dennonch haufig von einer solchen, manchmal auch von einer **Mehrfachhierachie**), sondern nur noch ein gerichteter azyklischer Graph (engl. directed acyclic graph, kurz DAG). Alle obengenannten Eigenschaften der Subtypenbeziehung bestehen jedoch weiter fort.

Wenn Subtypen, ahnlich wie bei der Typerweiterung oder -einschran- kung, auf Basis von bereits bestehenden definiert werden, spricht man **Subtyping** auch vom (nominalen) **Subtyping** (s. u.). Eine solche Subtypendefinition erfolgt dann immer unter Angabe des oder der direkten Supertypen, und relativ dazu. Dabei verlangt die obige Definition von einem Subtypen einen bestimmten Zusammenhang zwischen den Definitionen (Intensionen) von Sub- und Supertyp: Die Erganzungen oder Anderungen, die eine Subtypendefinition relativ zu der ihres oder ihrer Supertypen vorinmmt, mussen gewahrleisten, dass die Werte (Objekte) des Subtyps überall da auftauchen durfen, wo ein Wert des Supertyps verlangt wird. Dies lasst sich durch folgende einfache Regel ausdrucken:

Wenn ein Typ Y ein Subtyp eines Typs X!st, dann mussen alle Bedinguen, die für Objekte des Typs X erfullt sind; auch für Objekte des Typs Y erfullt sein.

Es darf also insbesondere keine Bedingung, die ein Supertyp an seine Objekte stellt, durch einen Subtyp aufgehoben oder relativiert werden. Logisch gesprochen heißt das, dass die Bedingungen (die Intension) des Subtyps die des Supertyps impliziert. Daraus folgt, dass die Typerweiterung als Basis einer Subtypendefinition infrage kommt (da die Intension des Supertypen unverändert übernormmen und lediglich erganzt wird), die Typeinschrankung hingegen zunächst einmal nicht. Dennoch ware die Typeinschrankung vom Subtyping auszuschliessen eine unnotige Einschrankung, wie Sie qleich noch sehen werden.

Wenn man die eingangs dieses Kapitels gemachten Bemerkungen zur Typkorrektheit auf das Subtyping und die damit implizierte Zuweisungskompatibilitat übertragt, dann ergibt sich für die Extensionen von Supertypen und Subtypen, dass die Subtypenbeziehung als eine Teilmengenbeziehung gedeutet werden muss: Die Extension eines Subtypps ist in den Extensionen all seiner (direkten und indirekten) Supertypen enthalten. Umgekehrt umfasst die Extension eines Supertyps die Extensionen all seiner Subtypen. Es ergibt sich, dass nur wenn die Extensionen aller direkten Subtypen eines Typs paarweise disjunkt sind, man es mit einer echten Typhierarchie zu tun hat, in der jeder Typ nur genau einen direkten Supertyp hat. Ist die Extension eines Supertyps genau gleich der Vereinigung der Extensionen seiner Subtypen, hat der Supertyp keine eigenen Werte, also keine Werte, die nicht zugleich Wert eines seiner Subtypen sind. Diese Bedingung empiricht der Idee von der _Generalisierung_ aus Abschnitt 9.1 und im ubrigen gute objektorientierer Pravis (s. Kapitel 69).

### Strukturelles und nominales Subtyping

Beim Subtyping unterscheidet man wie bei der Typaquivalenz und -konformitat zwischen nominalem und strukturellen Subtyping. Nominales Subtyping liegt vor, wenn ein Subtyp aus einem nametlich erwahnten Supertyp abgeleitet sein muss, um als sein Subtyp zu gelten. Strukturelles Subtyping liegt vor, wenn ein Typ lediglich die obige Definition von Subtyp erfullen muss, um als solcher zu gelten. Nominales Subtyping impliziert strukturelles; analog zur Typkonformitat macht das nominale Subtyping die Subtypenbeziehung antismmetrisch, das strukturelle hingegen nicht.

### Kovarianz und Kontravarianz bei Methodenaufrufen

Dass Typwereiterung als Basis des Subtyping keine technischen Probleme bereitet, sollte hinreichend klargeworden sein: Typfehler sind damit ausgeschossen und es bleibt lediglich das semantische Problem, dass Werte eines Subtyps inhaltlich keine Werte des Supertyps sind (wie im Beispiel von zwei- und dreidimensionalen Punkten). Es bleibt noch die Frage, ob und falls ja in welchem Umfang Typeinschrankung im Rahmen des Subtyping erlaubt ist. Diese Frage soll an einem Beispiel beantwortet werden.

Angenommen, es ist ein Typ A wie folgt definiert:

Typ

A914 m: y <Y> A <Y>-

Zuweisungen der Art

915 x := a m: z

wobei **a** eine Variable vom Typ A sei (fur ein Objekt vom Typ A steht), sind nach den Regeln des Subtping dann zulassig, wenn die Variable **x** mit einem Supertyp und **z** mit einem Subtyp von Y (jeweils einschlieflich des Typs Y selbst) deklariert ist.

Nun sei weiterhin der Typ B wie folgt als Subtyp von **A** abgeleitet:

\begin{tabular}{p{142.3pt} p{142.3pt}} \hline Typ & B \\ Supertyp & A \\ \hline Protocol & \\ \hline \end{tabular}

Die Methode m: wird also in B _redefiniert_. Die Frage ist nun, in welchem Verhaltnis die dabei verwendeten Typen X und Z zu Y stehen mussen, damit die Zuweisung aus Zeile 915 weiterhin zulassig ist, selbst wenn die Variable **a** auf ein Objekt vom Typ B verweist. Mit anderen Worten: Welche Bedingungen sind an die Parametertypen bei der Redefinition zu stellen, damit eine Zuweisung eines Objekts vom Typ B an eine Variable vom Typ A in der Folge zu keiner Verletzung einer (anderen) Typinvariante fuht? Solche Folgefehler waren ja bereits in Kapitel 25 thematisiert worden.

Die Antwort lasst sich systematisch herleiten, indem man sich die zu Zeile 915 gehorenden impliziten Zuweisungen genau anschaut. Zuerst wird ja **der** dem formalen Parameter von m:, y, zugewiesen. Wenn **y** nun in B einen anderen Typ als Y bekommen soll, dann darf es sich dabei nur um einen handeln, der mehr Werte zulassst -- wurde er weniger Werte zulassen, konnte es sein, dass er die Zuweisung von **z** ausschliefl, wodurch Zeile 915 zu einem Typfehler (einem typinkorrekten Programm) fuhren wurde. Der Typ des formalen Parameters **y** von m: in B, Z, muss also ein Supertyp dessen in A, Y, sein. Zuletzt, d. h., nach erfolgter Auswertung des Methodenaufrufs, wird dann das Ergebnis **x** zugewiesen. Wenn nun der Ruckgabewert von **m:** in B, X, einen anderen Typ als in A, Y, bekommen soll, dann kann dies aufgrund der geforderten Zuweisungskompatibilitat nur um einen Typen handeln, der weniger Werte zulasst, da ja sonst die Zuweisung an **x** zu einem Typfehler fuhren konnte. Es kommt also als Ruckgabetyp für **m:** in B nur ein Subtyp von dem in A, Y, infrage. Es ergibt sich also, dass sich bei einer Redefinition einer Methode die Eingabeparametertypen einer Funktion nur _nach oben" (also zu einem Supertypen hin), die Ausgabeparameter hingegen nur _nach unten" (hin zu einem Subtyp) verändern durfen, wenn die Typkorrektheit eines Programms nicht verletzt werden soll.

[MISSING_PAGE_FAIL:192]

rucksichtigt wird, als Funktionen oder Abbildungen herhalten. Der hier zweistellige Definitionsbereich (Empfangertyp plus Parametertyp) der Funktion steht dabei stellverterend für beliebige Stellenzahl, also für Methoden mit beliebig vielen Parametern. Der Wertebereich ist hingegen immer einstellig, da eine Methode stets nur einen Wert zuruckgibt.

Wenn man nun die Anzahl der Empfangerobjekte einschrankt (was ja beim übergang zu einem Subtypen geschieht), dann schrumpft damit nicht nur der Wertebereich der Funktion (wie in Kapitel 25 schon illustriert), sondem auch die Menge der moglichen Eingabewerte (der zweite und alle weiteren Definitionsbereiche), die mit der Bereits eingeschrankten Menge der Empfanger gemeinsam auftreten können. Es verhalten sich also nicht nur die Ergebnis-, sondern auch die Parametertypen kovariant.

Dieses Ergebnis ist gewissermassen frustrierend, da es die soeben hergeleitete Kontravarianzregel für Parametertyppen infrage stellt: Was programmertechnisch moglich und sinnvollerscheint, hat in der Realitat (der Interpretation oder Semantik) keine Bedeutung. Auf der anderen Seite erklart es aber, warum kontravariante Parameterredefinitionen in der Programmierpraxis nicht benotigt werden.52 Kovarianz für Parametertyppen zuzulassen, so sinnvoll es auch zu sein scheint, erlaubt jedoch typinkorrekte Programme; Sie werden im Kontext der Programmiersprache Effelf (Kurseinheit 5, Abschnitt 52.5) noch ausführlicher auf das Problem und eine mogliche Losung hingewiesen.

Footnote 52: Wer ein Beispiel weiss oder hat, möge es mir bitte schicken!

### Inklusionspolymorphie

Ein von Christopher Strachey, einem der Urvater der Programmierung als wissenschaftliche Disziplin, eingefuhrter Begriff ist der **Polymorphie**. Polymorphie bedeutet allgemeinVielgestaltigkeit und wird vor allem in der Biologie verwendet. In der Programmierung steht er für verschiedene Dinge, die jedoch alle mit Typen zu tun haben.

Unter **Inklusionspolymorphie**, auch **Subtyppolymorphie** genannt, versteht man im wesentlichen dasselbe wie unter Subtyping: Wo Objekte eines Typs enwartet werden, können Objekte anderer Typen erscheinen, weil der erste Typ die anderen subsumiert (inkludiert). Der Begriff ist vor allem in Abgrenzung zum _parametrischen Polymorphism_ (engl. parametric polymorphism, s. Kapitel 29) gebrauchlich; sonst redet man eher von Subtyping.

Das Interessante an der Inklusionspolymorphie ist, dass sich der Wertebereich von Typen dadurch auf unvorhergesehene Umfange aufweiten lasst. Dies ist insbesondere für die Weiterentwicklung und Wiederverwendung von Programmen interessant, bei der einfach neue Typen hinzugefugt, die anstelle Bereits existierender eingesetzt werden können, ohne dass dazu am Programm sonst etwas geandert werden musste. Die Regeln einer strengen Typprufung werden durch Inklusionspolymorphie aufgelockert, ohne an Typischerheit zu verlieren.

Insgesamt krankt die Definition des Subtyping und der Inklusionspolymorphisme in der objektorientierten Programmierung jedoch daran, dass nicht

**einfachen Definition** klar definiert ist, was alles zu verlangen ist, damit ein Objekt eines Typs tatsachlich auch da auftauchen kann, wo ein Objekt eines anderen Typen erwartet wird. Zwar gibt die Regel von Ko- und Kontravarianze eine klare Bedingung vor, aber wie Sie schon gesehen haben, ist diese Bedingung aus praktischen Gründen nicht unumstritten. Dazu kommt, dass die Regel einerseits gar nicht ausreicht, um Ersetzbarkeit zu garantieren, und andererseits zu streng ist (s. Kurseinheit 6, Kapitel 54). Da Ersetzbarkeit aber der Definition des Subtypen-begriffs zugrunde liegt, bleibt das ganze schwammig. In dieser Kurseinheit habe ich mich, den meisten gangigen objektorientierten Programmiersprachen folgend, darauf zuruckgezogen, zu garantieren, dass keine Typfehler, also Fehler der Art, dass eine bestimmte, geforderte Eigenschaft (Methode) bei einem Objekt nicht vorhanden ist, auftreten können; alles weitere wird dann in Kapitel 54 behandelt.

## 27 Typumwandlungen

Zuweisungskompatibilitat unter Subtyping erlaubt also die Zuweisung von Objekten eines Subtypes an Variablen eines Supertypes. für die statische Typprufung ergibt sich daraus kein Problem, weil schergestellt ist, dass die Subtypen alle Eigenschaften ihrer Supertypen erhalten, so dass keine Typfehler auftreten können. für die Programmiererin ergibt sich aber manchmal das Problem, dass sie ein Objekt, auf das eine Variable eines Supertypes verweist, wie ein Objekt seines tatsachlichen Typs verwenden mochte, in der Regel, weil sie eine Methode darauf auftrufen mochte, die der Supertyp nicht hat. Genau diesen Methodenaufruf wurde die Typprufung aber zuruckweisen.

Fur diesen Zweck gibt es die Moglichkeit der **Typumwandlung** (engl. type cast). Eine Typumwandlung ist ein Verfahren, bei dem der vorgefundene Typ eines Ausdrucks (einer Variable oder eines Methodenauftrufs) in einen vorgegebenen konvertiert wird. Mit dem Objekt, für das der Ausdruck steht, passiert dabei gar nichts -- es wird lediglich der Compiler (bzw. der Type checker) davon überzeugt, dass der Ausdruck den bei der Umwandlung angegebenen Typ hat. Solte sich zur Laufzeit herauststellen, dass das nicht der Fall ist, kann ein Laufzeittypsystem -- soweit vorhanden -- dies bei seiner _dynamischen Typprufung_ bemerken und ggf. einen entsprechenden Fehler melden (vgl. die Anmerkungen dazu in Kapitel 18).

Typumwandlungen können grundsatzlich in verschiedene Richtungen erfolgen: zu Supertypen, zu Subtypen oder zu solchen, die weder Supernoch Subtyp des Ausgangstyps sind. Man spricht entsprechend von **Up cast**, **Down cast** oder **Cross cast**. Up casts sind immer typischer, Down casts und Cross casts nicht. Down casts sind relativ haufig; sie kommen vor allem dort vor, wo kein parametrischer Polymorphismus (Kapitel 29) zur Verfugung steht oder wo ein Objekt seinem tatsachlichen Typ entsprechend behandelt werden soll. Cross casts sind eher selten; in der _interfacebasierten Programmierung_ (s. Abschnitt 28.2) stehen sie für einen _Rollenwechsel eines Objekts_.

Nun sind Typumwandlungen entweder überflousig oder unsicher. Man sollte daher versuchen, auf se zu verzichten. Wo unverzichtbar, sollten

**empfehlungen** Typumwandlungen mit einem Typtest abgesichert werden. Dabei wird zur Laufzeit geprut, ob das Objekt, für das der typewandelte Ausdruck steht, auch den gewunschten Typ hat. lst das nicht der Fall, sollten die Teile des Programms, die den bei der Typumwandlung genannnten Typ voraussetzen, nicht ausgefuhrt werden. Sie werden in spateren Kapiteln zu den einzelnen Programmiersprachen noch Beispiele für diese Praxis zu sehen bekommen.

## 28 Der Zusammenhang von Typen und Klassen

Wenn in dieser Kurseinheit bislang ausschliesslich von Typen die Rede war und Klassen dabei ignoriert wurden, so hat das gute Grunde: Wahrend eine Klasse die Implementierung ihrer Objekte festlegt, ist eine Typdefinition vollkommen frei von Implementierungssapekten. Zwar können auch _abstrakte Klassen_ (Kurseinheit 2, Abschnitt 10.3) ausschliesslich aus Methodendeklarationen bestehen, also ohne jeden Implementierungsanteil daherkommen, aber auch ihr Zweck ist in der Regel, zumindest eine partielle Implementierung vorzugeben, die anderen Klassen, ihren Subklassen, gemeinsam ist, so dass sie diese erben können: Schliesslich druckt die Klassenhierarche ja eine,,genetische" Verwandtschaft aus (s. Abschnitt 10.1 und Kapitel 11). Eine Typprufung soll aber ohne Ansehen der Implementierung stattfinden; sie baut daher aub abstrakte Spezifikationen, eben auf Typen.

Es sind also Typen abstrakte Spezifikationen, die zum einen den Wertebereich von Variablen einschranken und zum anderen das _Protokoll_ (den Funktionsumfang) von Objekten angebeen. Im Gegensatz dazu sind Klassen Konstrukte, die Objekte als Instanzen zu bilden erlauben und mit Implementierung versehen. Da Objekte aber auch den Wertebereich von Typen ausmachen, stellt sich naturlich die Frage, welcher Art der Zusammenhang zwischen Typen und Klassen ist.

Diese Frage soll anhand der schematischen Klassendefinitionen aus Kurseinheit 2, Abschnitt 7.2 beantwortet werden. In SMALITALK ist diese ja stets von der Form53

[MISSING_PAGE_POST]

Compiler diese Zuweisungskompatibilitat auf einfachere Weise als die Prufung der Strukturkonformitat, die ja eine _rekursive Expansion_ der Typdefinitionen erfordert, feststellen zu lassen, gibt es zwei Moglichkeiten (bei beiden handelt es sich gewissermassen um Varianten einer Namenskonformitat):

1. jede Klasse sagt explizit, mit welchen Typen sie konform ist, oder
2. jede Klasse spezifiziert implizit selbst einen Typ.

Im ersten Fall musste der Compiler noch prufen, ob eine Klasse tatsachlich auch über alle Eigenschaften der von ihr genannten Typen verfugt; im zweiten Fall ist das automatisch der Fall, da der Typ ja gewissermassen aus der Klasse erzeugt wird. Diese zweite Art wird von den allermeisten typisierten, objektorientierten Programmiersprachen bevorzugt, doch auch die erste kommt in popularen Sprachen vor: So kann beispielsweise in Java und C# jede Klasse angeben, mit Variablen welcher Interface-Typen ihre Instanzen zuweisungskompatibel sein sollen (s. Kurseinheit 4, Kapitel 40 und Kurseinheit 5, Abschnitt 50.4.2). Auch STRONGtalk stellt beide Moglichkeiten zur Verfugung.

### Subklassen und Subtypen

Man konnte nun versucht sein, den Zusammenhang von Klassen und Typen auch unter Verebrung bzw. Subtyping beizubehalten und damit zu enwarten, dass eine Instanz einer Subklasse einer Klasse dem Wertebereich des zur Superklasse gehorenden Typs angehort. Das ist jedoch dann nicht der Fall, wenn in der Subklasse Anderungen vorgenommen werden, die eine Typkonformitat vom zur Subklasse gehorendem zum zur Superklasse gehorenden Typ aufheben, also z. B. Methoden geloscht oder inkompatibel redefiniert werden. Die meisten objektorientierten Programmiersprachen verbieten das jedoch, so dass sich die Subklassenbeziehung tatsachlich auf eine parallele Subtypenbeziehung übertragen lasst.

### Typen als Schnittstellenspezifikationen von Klassen

Eine Klasse liefert eine Implementierung. Nach gangigen Prinzipien nicht nur der objektorientierten Programmierung sind Implementierungen aber hinter _Schnittstellen_ (oder _Interfaces_) zu verbergen: Nur die Elemente einer Klassendefinition, die für Benutzerinnen einer Klasse zu Verwendung gedacht sind, sollen durch die Schnittstelle nach aussen getragen werden -- der Rest soll verborgen bleiben (das sog. _Geheimnisprinzip_).

In Programmiersprachen wie JAVA, C++ etc. gibt es spezielle Schlusselworter, die einem Element einer Klassendefinition (beispielsweise einer Methode) vorangestellt seine Zugreifbarkeit festlegen. Diese sog. _Zugriffsmodifikatoren_ (engl. access modifier) legen gemeinsam mit der Klassendefinition, die ihre vollstandige Implementierung beinhaltet, auch die Schnittstelle der Klasse fest. Je nach Sprache ist diese Schnittstelle für alle Benutzerinnen der Klasse gleich oder unterscheidet sich nach Lokalitat oder anderen Eigenschaften von benutzender und benutzter Klasse. Imersten Fall konnte man von einer absoluten Schnittstelle sprechen; um sie zu spezifizieren, reicht es, zwischen sichtbar und unsichtbar zu unterscheiden. Im zweiten Fall ist die Schnittstelle relativ.

Eine absolut spezifizierte Schnittstelle einer Klasse kommt, wenn sie wirklich keinerlei Implementierungsgeheimnisse verrat, einem Typ gleich. Sie besteht namlich nur aus Dekarationen von Methoden. Die gemachte Einschrankung ist notwendig, weil manche Sprachen, so z. B. Java und C++, die Instanzvariabelen ihrer Objekte in die Schnittstelle der Klassen aufzunehmen erlauben. Mit den Instanzvariablen wird aber die Repräsentation der Objekte nach aussen sichtbar, was dem Gedanken des Geheimnisprinzips widerspricht.

Wenn man nun eine Variable mit einem solchen die Schnittstelle reprasentierenden Typ deklariert und eine Typprufung erfolgreich durchgefuhrt hat, dann ist sichergestellt, dass über diese Variable nur auf die Elemente einer Klasse zugegriffen wird, die auch Bestandteil des Interfaces der Klasse sind. Wenn jede Instanz dieser Klasse ausschliesllich über typisierte Variablen ansprechbar ist, ist damit die Wahrung des Geheimnisprinzips garantiert. Typen dienen damit einem weiteren Zweck, den man zunächst einmal nicht mit ihnen assoziieren wurde, namlich der Wahrung des Implementationsgeheimnisses/Einhaltung der Schnittstellen durch den Compiler.

Dieser überaus nutzliche Zusammenhang zwischen Klassen, ihren Schnittstellen und Typen wurde erst relativ spat, namlich mit der Programmiersprache Java und ihrem _Interface-als-Typ-Konzept_, so weiterentwickelt, dass eine Klasse verschiedene Schnittstellen anbieten kann, die alle zugleich Typen der Klasse (genauer: Supertypen des der Klasse entsprechenden Typs) sind. Die damit ermoglichte _interfacebasierte Programmierung_, die in Kurs 01853 ausführlich behandelt wird, betrachte ich personlich als den wichtigsten Beitrag Javas zur Disziplin der objektorientierten Programmierung (s. a. Kurseinheit 4, Kapitel 45).

### Grunde für die Trennung von Typen und Klassen

Nun mogen Sie sich vielleicht fragen, warum Typen und Klassen über soiele Seiten als getrennte Begriffe dargestellt wurden, nur um am Ende zum Schluss zu kommen, dass eine Klassendefinition in der Regel auch als Typdefinition herhalt. Nun, erstens ist das nicht in allen Sprachen der Fall und zweitens ist es selbst in den Sprachen, in denen es der Fall zu sein scheint, nicht immer so (s. Fussnote 54). So handelt es sich eher um die Symbiose zweier verschiedener Konzepte, die unterschiedlichen Zwecken dienen, deren strukturele Ahnlichkeit sich aber durch eine syntaktische Zusammenlegung ausnutzen lasst:

1. Klassen dienen der Angabe von Implementierungen und damit als Container von ausfuhrbarem Code;
2. Typen dienen der Formulierung von Invarianten, die für Variablenbelegungen gelten mussen und deren Verletzung auf einen (logischen oder semantischen) Programmierfehler hinweist.

[MISSING_PAGE_FAIL:199]

Typen nach Bedarf zur generieren.54 Wohl deswegen bezeichnet man parametrische Typen (Typdefinitionen) auch als **generische Typen** (Typdefinitionen) oder kurz als **Generics**. Wie eben schon erwahnt, wird der Wertebereich bei einer solchen Typgeneration jeweils mitgneeriert.

Es erfolgt also die Zuweisung eines Typs zu einer Typvariable bei der Verwendung eines parametrisch definierten Typs in einer Deklaration, beispielsweise der Deklaration einer Variable oder des Ruckgabewerts einer Methode. Oberflachlich betrachtet entspricht diese Verwendung in etwa dem Aufruf einer (ja auch an einer anderen Stelle definierten) Methode oder besser (und schon aufgrund der Verwendung des Begriffs Instanziierung) eines Konstruktors; deswegen nennt man die Typvariablen, die in parametrischen Typdefinitionen vorkommen, auch **formale Typparameter** und die konkreten Typen, die bei der Verwendung des Typen in Deklarationen in die formalen Parameter eingesetzt werden, auch **tatsachliche Typparameter**. Trotz dieser Analogie zu Methoden- bzw. Konstruktoraufrufen muss man sich immer vor Augen halten, dass die Verwendung eines parametrisch definierten Typs bereits zur übersetzungszeit zu einer Zuweisung an die Typvariablen fuhrt, man es also keineswegs mit etwas Dynamischem zu tun hat. Insbesondere mussen Typen keine Objekte sein, um Typvariablen zugewiesen werden zu können.

### 29.1 Einfacher parametrischer Polymorphismus

Ein einfaches Beispiel für eine generische Typdefinition in STRONGTALK ist das folgende:

Typ

Typarataben

T

Protocol

921 x ^ <T> ^ <Self>

T ist dabei eine Typvariable. Beim Vorkommen von T im Abschnitt,,Typvariablen" handelt es sich um ihre Deklaration (Vereinbarung); beim Vorkommen im Abschnitt,,Protokoll" um ihre Verwendung.

Das für den Tatbestand der Parametrisierung wichtige an dieser Typdefinition ist, dass **x**: anstelle des Parameter- und **x** anstelle des Ruckgabetyps T nennt, wobei T eben kein Typ, sondern eine Typvariable ist. für Typvariablen verwendet man traditionell einzelne Grossbuchstaben; dies hat den nutzlichen Nebeneffekt, dass man durch eine Typvariable keinen tatsachlichen Typen verderckt, wie es sonst verseentlich passieren konnte: Man konnte die Typvariable namlich auch beispielsweise,,Integer" nennen, aber sie ware deswegen immer

[MISSING_PAGE_FAIL:201]

gibt **a**, **b** und **c** jeweils verschiedene Typen, die jedoch alle Instanzen der parametrischen Definition von **A** sind. Dennoch sind **a**, **b** und **c** wechselseitig nicht zuweisungskompatibel; sie haben tatsachlich verschiedene Typen. **a** ist jedoch mit **d** wie in
* 932] d <A[Integer]> 1

deklariert zuweisungskompatibel und umgekehrt, da beide denselben Typen haben.

### Collections als Standardanwendungsfall für parametrischen Polymorphismus

Eine wichtige Gruppe von Klassen, die Sie in den letzten beiden Kurseinheiten kennenglement haben, sind die sog. Collection-Klassen. Auch diese bilden jeweils einen Typ, so dass Variablen, die auf eine Collection verweisen, mit diesem Typ deklariert werden können.

Nun dienen Collections ja u. a. dem Zweck, Zu-n-Beziehungen zwischen ei-

**Problemstellung** nem Objekt und mehreren anderen zu ermoglichen, indem sie dafur Zwischenobjekte zur Verfugung stellen (s. Kurseinheit 2, Kapitel 13). Und so bilden die mit den Collection-Klassen assoziierten Typen auch nur die Typen für die Zwischenobjekte. Was man jedoch eigentlich bei der Deklaration von \(n\)-wertigen Attributen angeben (deklarieren) mochte, ist der Typ der in Beziehung stehenden Objekte.

Wenn das Attribut beispielsweise kinder hei8t und man damit eine Person mit einer Menge anderer Objekte vom Typ Person, den Kindern, in

**Elementtypen einer**

**Collection**

Beziehung setzen mochte, dann nutzt es nichts, wenn man kinder vom

Typ Person deklariert -- es konnte dann hochstens eine Person enthalten und nicht mehrere. Was man vielmehr gern hatte, ware etwas, das dem Array-Typkonstruktor array

**[<Bereich>] of <Elementtyp>** (spitze Klammern hier wieder als Begrenzer von metasyntaktischen Variablen) von PASCAL gleicht: Im gegebenen Beispiel wurde man gern deklarieren, dass kinder den Typ Collection of Person haben soll. Genau das tut 935 at: einIndex <Integer> put: einElement <E> ^ <Self> Das Programmfragment

936

p <Person> |
937 p := Person new.
938 p kinder at: 1 put: Person new.
939 p kinder at: 2 put: Person new.
940 (p kinder at: 1) kinder at: 1 put: Person new

ist demnach typkorrekt (und weist p zwei Kinder und ein Enkelkind zu).

Ein anderes Beispiel für eine parametrische Definition einer Collection ist Dictionary: Hier sollte nicht nur der Element-, sondem auch der Schlusseltyp variabel gehalten werden. Eineentsprechende parametrische Typdefinition, diesmal mit zwei Typparameteren, kann wie folgt aussehen:

\begin{tabular}{l l} \hline Typ & Dictionary \\ \hline Typvariable & S E \\ \hline Supertyp & Collection[E] \\ \hline Protokol & \\ \hline
941 at: einSchlussel <S> ^ ^ & <E> \\
942 at: einSchlussel <S> & put: einElement <E> ^ & <Self> \\ \hline Dabei ist der parametrische Typ Dictionary ein Subtyp des ebenfalls parametrischen Typs Collection. Man beachte, dass der Typparameter E hier bereits in der Supertypdeklaration verwendet wird. Ein Dictionary, in dem Integer auf beliebige Objekte abgebildet werden, erhalt man dann durch die Instanziierung Dictionary[Integer, Object]. Es ist mit einer Variable vom Typ Collection[Object] zuweisungskompatibel. Auf die Einzleheiten des Subtypings bei parametrischen Typen wird in Kapitel 30 eingegangen. \\ \end{tabular}

### Parametrischer Polymorphismus und Inklusionspolymorphic

Nun war die Speicherung von Personen in Collections, wie sie oben benotigt wurde, auch schon ohne den parametrischen Polymorphismus moglich, namlich per Inklusionspolymorphic (Subtyping). So wurde es zunächst ausreichen, wenn Collection wie folgt definiert ware:

\begin{tabular}{l l} \hline Typ & Collection \\ \hline Protokol & \\ \hline
943 at: einIndex <Integer> ^ & ^ <Object> \\
944 at: einIndex <Integer> put: einObjekt <Object> ^ & ^ <Self> \\ \hline \end{tabular}

An die Stelle der Typvariable E tritt also der (konkrete) Typ Object. Da in StronGTalk alle Typen Subtypen von Object sind, kann man jedes belie- bige Objekt in einer solchen Collection speichern. In der Klasse Person, die Collection verwendet, wurde dann kinder schlicht als vom Typ Collection (ohne Typparameter) deklariert. Das objige Programmfragment (Zeilen 936-940) konnte dann auch beinahe so bleiben, bis auf eine kleine Ausnahme: Zeile 940 enthalt jetzt einen Typfehler, da das Ergebnis von p kinder at: 1 vom Typ Object ist und das Protokoll von Object keine Methode kinder unterstitzt. Es ware also erst noch eine Typumwandlung von Object nach Person, ein Down cast (s. Kapitel 27), vonnoten. Deren Zulassigkeit ist aber davon abhangig, was wirklich in der Collection drinsteckt, und das kann der Compiler nicht (oder nur sehr aufwendig) feststellen. Die Losung, die Inklusionspolymorphie bietet, beinhaltet also eine Sicherheitslucke in der statischen Typprufung, die der parametrische Polymorphisms behebt.

\begin{tabular}{c c}  & Unzulanglichkeit des \\ Zum einen ware es ohne Inklusionspolymorphie nicht moglich, in einer \\ Collection mit Elementtyp **XYZ** auch Objekte eines Subtypes von **XYZ** zu \\ speichern. Solche _heterogenen Collections_ kommen aber in der Praxis immer wieder vor, so dass man selbst bei Verwendung einer parametrischen Definition von \\ Collections nicht auf Inklusionspolymorphie verzichten wird. Zum anderen wird die erhohte \\ Typischerheit bei der Verwendung von parametrisch definierten Typen (wo man ja zumindest bei homogener, also ohne Ausnutzung der Inklusionspolymorphie, Belegung der mit einem Typparameter typisierten Variablen ohne Typumwandlungen auskommt) mit einer geringeren Typischerheit innerhalb der Typdefinition (bzw. Klassendefinition) selbst erkauft. Dies verlangt nach Erklarung. \\ Stellen Sie sich einen Collection-Typ MyCollection vor, dessen Werte solche Collections sein sollen, deren Elemente sortiert und summiert werden können. Dieser Typ sei ein Subtyp von Collection und verfuge weiterhin über entsprechende Methoden sortieren und summieren: \\ \hline Typ & MyCollection \\ Typvariable & E \\ Supertype & Collection[E] \\ Protokoll & \\
945 sortieren & \({}^{\star}\) +Self? \\
946 summieren & \({}^{\star}\) +Number? \\ \end{tabular}

Intuitiv verlangt die Sortierbarkeit der Objekte vom Typ MyCollection, dass auf den Elementen eine Vergleichsfunktion definiert ist. Dies ist aber nicht für alle Typen und somit auch nicht für alle moglichen Belegungen der Typvariable E der Fall. Auch verlangt die Methode summieren, dass sich aus den Elementen einer solchen Collection ein Wert aggregieren lasst, der vom Typ Number oder einem Subtyp davon ist. Man kann daraus schliessen,dass die Elemente ebenfalls vom Typ Number sein oder zumindest Methoden besitzen mussen, die einen solchen Wert zuruckliefern. Und so wurde auch eine Implementierung der Methode summieren in etwa wie folgt aussehen:

```
947summierenA<Number>
948Aelements
949inject:0into:[:summe<Number>:element<Number>|summe+element].
```

Das aber verlangt, dass der Elementtyp von MyCollection Number oder ein Subtyp davon sein muss, da sonst die Zuweisung an den formalen Blockparameter element nicht zulasig ware. Insbesondere wurde das Codefragment

```
951list<MyCollection[String]>|
952listemumiere
```

zu einem Typfehler fuhren, weil in Zeile 950 einer Variable vom Typ Number ein Objekt vom Typ String zugewiesen wird. Nun kann aber die Definition des parametrischen Typs MyCollection nicht wissen, wie sie hinterher verwendet wird, und wenn eine Addition durchgefuhrt werden soll, sit sie darauf angewiesen, dass sie nur mit Typen von addierbaren Objekten instanziert wird. Es wird also die erhohte Typischerheit außerhalb der Typdefinition, namlich bei ihrer Verwendung, durch eine verminderte Typischerheit innerhalb erkauft.

Was man gerne hatte, um diesen Mangel zu beheben, ware die Sicherheit, dass alle Typen, die für E eingesetzt werden können, bestimmte Eigenschaften haben, im gegebenen Beispiel, dass sie sortierbar und addierbar sind. Entsprechend sollte ein Typfehler nicht erst in Zeile 950 moniert werden, sondern bereits an der Stelle, an der die unzulassige Wertzuweisung an die Typvariable stattfindet, namlich bei der Verwendung (der _Instanzierung_) der parametrischen Typdefinition in der Deklaration von Zeile 951. Genau das erlaubt der beschrankte parametrische Polymorphismus, der im nachsten Abschnitt behandelt wird. zunächst jedoch noch zu einem anderen wichtigen Aspekt von parametrischem Polymorphismus und Subtyping.

Unter den Typdefinitionen

[MISSING_PAGE_EMPTY:206]

obertragt. Dies wird auch in Abschnittt 29.5 noch eine besondere Rolle spielen. Vor diesem Hintergrund beinahe paradox erscheint, dass sich Subtyping jedoch dazu einsetzen lasst, das oben beschriebene Problem mit der,,inneren Typsicherheit" von parametrisch definierten Typen zu losen.

### Beschrankter parametrischer Polymorphismus

Obiges Beispiel hat gezeigt, dass die einfache Form des parametrischen Polymorphismus für Typsicherheit in der objektorientierten Programmierung nur teilweise nutzlich ist: Da die Typvariablen selbst nicht typisiert sind, kann man innerhalb der Typdefinition (und der den Typ implementierenden Klassen) keine Aussagen über den Typ machen. Ausserhalb, bei der Verwendung (Instanziierung) der Typdefinition, geht das schon, da hier die Typvariable durch einen Typ ersetzt ist.

Was man also gern hatte, ist, dass die Typvariable innerhalb der mit ihr **wertbeschrankte** parametrisierten Typdefinition selbst wertbeschrankt ist, und zwar derart, **Typvariablen** dass man bei den als Werte zulasigen Typen ein bestimmtes, benotigtes Protokl voraussetzen kann. Die tatsachlichen Typparameter sind dann nicht mehr beliebig zu wahlen, sondern nur noch aus solchen Typen, die die Einschrankungen erfullen. Eine Moglichkeit, das zu erzielen, ware, Metatypen einzufuhren, deren Wertebereiche Typen mit durch die Metattypen vorgegebenen Eigenschaften sind. Diese Moglichkeit wird jedoch in der Praxis nicht genutzt.

Stattdessen verwendet man eine Art der Beschrankung des Wertebereichs von Typvariablen, die auf Subtyping beruht. Wenn man namlich **Supertypen als**. **Schranken** erzwingen kann, dass ein tatsachlicher Typparameter (also der Wert der Typvariable) Subtyp eines bestimmten Typs ist, der die benotigten Eigenschaften (Methoden) umfasst, dann ist damit alles erreicht, was man benotigt: Aufgrund der Regeln des Subtyping hat jeder solche Typ die Eigenschaften des Supertypes (s. Kapitel 26).

Ein solchermassen durch einen Supertyp beschrankte parametrische **Beispiel**. Typdefinition ist die folgende:

[.5em] Typ

MyCollection

Pyvariablen **E < Number**

Der Rest der Definition geht wie oben. Der Ausdruck E < Number im Abschnitt,,Typvariablen" ist Deklaration und Beschrankung zugleich; die Beschrankung ist aber wie gesagt keine Typisierung wie in normalen Variablendeklarationen. Sie druckt vielmehr aus, dass die Typen, die als Werte für E eingesetzt werden durfen, Subtypen von **Number** sein mussen. Die Deklaration aus Zeile 951 wird damit unzulassig und fuhrt zu einem entsprechenden Typfehler wahrend der statischen Typprufung; die Deklaration

[MISSING_PAGE_FAIL:208]

bereits bekannten Problemen fuhren.55 Auch hier bietet parametrischer Polymorphismus eine Alternative, wenn auch nicht ganz so, wie vielleicht enwartet.

Man ersetzt dazu zunächst den Typ des Parameters durch eine Typvariable T. Nun kann man schlecht

\begin{tabular}{c c} \hline Typ & T \\ Typvariable & T \\ Protocol & \\ \hline
967 = einT <T> & A <Boolean> \\ \hline \end{tabular}

schreiben, da der Typ dann keinen Namen hatte und somit auch nicht verwendbar (referenzierbar) ware. Was man aber sehr wohl machen kann, ist, einen allgemeinen parametrischen Typ zu definieren, der nur dem Zweck des Gleichheitstests dient und der den Parametertyp des Tests variabel halt, wie in

\begin{tabular}{c c} \hline Typ & Equatable \\ Typvariable & T \\ Protocol & \\ \hline
968 = einT <T> & A <Boolean> \\ \hline \end{tabular}

Man kann dann die gewinschte Rekursion indirekt, namlich per Definition eines nicht parametrischen Typs als Subtyp des parametrisierten Typs Equatable herstellen, wobei man den zu definierenden Typ gleichzeitig als tatsachlichen Typparameter einsetzt. So liefert z. B.

\begin{tabular}{c c} \hline Typ & Integer \\ Supertyp & Equatable[Integer] \\ \hline \end{tabular}

eine Methode mit der Signatur = einT <Integer> & A <Boolean> im Protokoll von Integer. Allerdings kann man so nicht erzwingen, dass bei der Definition des Typs Integer oben genau Integer als tatsachlicher Typparameter eingesetzt wird; es hatte auch jeder andere Typ, z. B. String, sein können -- der Gleichheitstest ware dann mit = einT <String> & A <Boolean> falsch dekariert.

Genau diese Beschrankung des tatsachlichen Typparameters kann man nun mit einer stilisischen Figur erreichen, die vermutlich manch einer von lhnen erhelbiche Kopfschmerzen bereiten wird (zumindest macht sie das mir immer wieder aufs neue): Man beschrankt den formalen Typparameter T von Equatable auf einen Subtyp von Equatable[T], wobei das Vorkommen von T in Equatable[T] eine Verwendung der gerade erst eingefuhrten Typvariable T darstellt.

verlangt also im obigen Beispiel der Typdefinition von **Integer** als Subtyp einer Instanzie- rung der parametrischen Definition von **Equatable**, dass der tatsachliche Typparameter **Integer** ein Subtyp von **Equatable[Integer]** sein muss. Genau das sagt aber die obige Typdefinition von **Integer** ausl Stunde dort **Equatable[String]** oder irgend etwas anderes als Typschranke, ware dies nicht mehr der Fall (s. Abschnitt 29.3) und die Definition von **Integer** verursachte einen statisch feststellbaren Typfehler.

Wenn Sie hier ein Verstandnisproblem haben, trosten Sie sich -- es dauert **ein paar Worte zum** eine Weile, bis man es verstanden hat, und noch langer, bis solche Figuren zum aktiven Repertoire gehoren. Gleichwohl sollten Sie sich damit befassen: Das Java-Collections-Framework in der Version von Java 5 ist voll solcher Typdefinitionen, nicht, weil sie schon sind, sondern weil man sie braucht, um das Framework typischer zu machen, ohne seine Flexibilitat zu opfern. Auch Sie werden, wenn Sie objektorientiert programmieren, über kurz oder lang solche Konstrukte von sich geben mussen.

## 30 Parametrischer Polymorphismus und das Kovari-anzproblem

In gewisser Weise hat man es beim rekursiv beschrankten parametrischen Polymorphismus wie oben vorgestellt mit einem Fall von kovarienter Redefinition zu tun: Der Parametertyp der Methode = andder sich mit dem Emfangertyp. Allerdings ergibt sich daraus, anders als bei der Verwendung von **Self**_als Typvariable_, kein Widerspruch zur Kontravarianzregel des Subtyping, denn Integer wird dadurch unmittelbar ja lediglich zu einem Subtyp von **Equatable[Integer]** und nicht etwa von **Equatable[Object]**. Tatsachlich sind **Equatable[Integer]** und **Equatable[Object]** ja zwei vollkommen verschiedene Typen (mit disjunkten Wertebereichen) und **Equatable[T]** ist gar kein Typ (so dass man auch keine Variable mit ihm deklarieren kann), so dass keinerlei Zuweisungskompatibilitat und damit auch kein Problem mit Typkorrektheit besteht.

Trotzdem stellt sich die Frage, ob sich das in Abschnitt 26.3 angesprovhene allgemeine Problem der wunchenswerten kovarianten Redefinition von Eingabeparametern in Methoden mittels parametrischen Polymorphismus nicht irgendwie losen lasst. Die Antwort ist unbefriedigend: nur zum Teil.

So kann man, um das Beispiel von Dokumenten und Druckern aus Abschnitt 26.3 wieder aufzugereifen, einen parametrischen Typ Dokument wie folgt definieren:* [970] Dokument Die Deklaration von Zeichnung mit Typparameter T als Subtyp von Dokument vorausge-setzt, lassen sich die folgenden Variablendeklarationen bilden:
* [971] **z <Zeichnung[Plotter]> p <Plotter> 1 <Zeilendruckers>**

Weiterhin die Deklarationen von Plotter und Zeilendrucker als Subtypen von Drucker vorausgesetzt ware ein Methodenaufruf
* [972] **z druckenAuf: p** typkorrekt,
* [973] **z druckenAuf: 1** hingegen nicht. Allerdings ist die Assoziation von Zeichnung mit Plotter, die Kovarianz, in keiner Typdefinition festgehalten, sondern lediglich in der Deklaration von **z**. Es hindert einen insbesondere nichts daran, dieselbe oder eine andere Variable als vom Typ Zeichnung[Zeilendrucker] zu deklarieren. Man beachte, dass es anders als im obigen Beispiel von Equatable, wo ja der Typparameter auf den definierten Typ selbst eingeschrankt wurde, hier keine Moglichkeit gibt, einen bestimmten Wert für einen Typparameter verzuschreiben.

Was man allerdings tun konnte, ist, Zeichnung als Subtyp von Dokument[Plotter] zu definieren. Dies hat jedoch den Nachteil, dass Zeichnung damit kein Subtyp mehr von Dokument und, wie auch zuvor schon Zeichnung [Plotter] kein Subtyp von Dokument[Drucker] ist (s. Abschnitt 29.3), wodurch die Zuweisungskompatibilitat mit entsprechend deklarierten Variablen verlorengeht. Kovariante Redefinition bei gleichzeitiger Inklusionspolymorphie lasst sich auch mittels parametrischer Typen nicht hinbekommen.

## 31 Grenzen der Typisierung

Wie Sie sehen, ist das Problem der kovarianten Redefinition ziemlich hartnackig. Man muss aber gar nicht so weit gehen, um an die praktischen Grenzen der Typisierung zu gelangen: Bereits der Ausdruck

* [974] **x reciprocal** beinhaltet einen Typfehler, wenn nicht sichergestellt ist, dass **x** nicht **0** enthalt. Nun konnte man einen Typ **NotZero** definieren und **x** als von diesem Typ deklarieren, womit der obige

[MISSING_PAGE_FAIL:212]

Man definiert einfach die Addition als Methode des Typs Punkt und redefiniert (überschreibt) die Methode in DreiDPunkt entsprechend. Allerdings muss man dann noch sagen, was passieren soll, wenn zu einer Instanz vom Typ DreiDPunkt (als Empfangerobjekt) eine Instanz vom Typ Punkt addiert werden soll; die Regeln der Zuweisungskompatibilitat verbieten das ja nicht! (Eine mogliche Losung ware _Multi dispatch._)

**Selbsttestaufgabe 29.1 (Seite 191)**

Wenn dem so ware, dann ware

980gb:=gazulassig. Der Ausdruck

981gb:=

der den deklarierten Typ B hat, wurde dann aber (wegen des Alias von gb auf das Objekt in ga) ein Objekt vom Typ A, also einem Supertyp, zuruckliefern. Also ist auch G[A] kein Subtyp von G[B]!

## 34 Das Programmiermodell Javas

Java ist in vielerlei Hinsicht (und vor allem im Vergleich zu SMALITALK) eine konventionelle Programmiersprache. Programme werden als Quelttext in sog. _Compilation units_ gespeichert, die gewohnlich Dateien sind und die -- jede für sich -- immer als Ganzes übersetzt werden.57 Das Ergebnis der übersetzung ist jedoch kein direkt ausfuhrbarer Maschinen-code, sondern ein sog. _Bytecode_, der von einer virtuellen Maschine, der Java Virtual Machine (JVM), interpretiert werden muss. Das sonst ublic Linken der einzelnen Klassen (genauer: des zu den Klassen gehorenden Bytecodes, die sog. Class files) wird dabei durch das Classloading der JVM ersetzt. Vorteile des ganzen sind eine grossere Flexibilitat bei der Entwicklung und Verteilung von Anwendungen sowie eine weitgehende Plattformunabhangigkeit: Java-Programme können, soweit sie nicht von bestimmten Eigenheiten der Betriebssysteme abhangen (man denke z. B. an die unterschiedliche Handhabung von Gross-/Kleinschreibung -- Java ist case sensitive, Windows nicht!), auf jedem Rechner und Betriebssysteme laufen, für die es eine JVM gibt.

Wahrend Java als Programmiersprache anfangs noch recht klein und überschaubar war (zumindest im Vergleich zu C++, einem ihrer Hauptkonkurrenten), so ist die Sprachdefinition heute ein Moloch. Mit dem wachsenden Nutzerninenkreis sind auch die Anforderungen an die Sprache gewachsen, und mit dem Java Community Process wurde aktiven Entwicklerinnen die Moglichkeit eingeramnt, Vorschlage zur Sprachenweiterung zu machen. Dabei ist jedoch -- aufgrund der mittlerweile riesigen Menge an Software, die in Java geschrieben ist -- stets auf Ruckwartskompatibilitat zu achten, so dass revolutionare Verbesserungen kaum moglich sind; stattdessen wird hinzugefugt. Das unterliegende Programmiermodell ist so immer dasselbe geblieben -- und wird es wohl auch immer bleiben.

Die grundlegenden Werkzeuge der Java-Programmierung sind neben der Edtor der Java-Compiler javac, die JVM, die Java-Klassenbibliothek (das sog. _Application Programming Interface_, API) und naturlich die Dokumentation (API-Dokumentation und Sprachdefinition). Gerade für die Java-Programmierung gibt es jedoch zahlreiche _integrierte Entwicklungsumgebungen_ (IDEs) und es ist niemandemz u raten, diese Werkzeuge links liegen zu lassen -- die einmal einen Teil ihrer wertvollen Lebenszeit mit dem richtigen Setzen des sog. Class path verbacht hat, wissen, wovon ich rede. Auf der anderen Seite sind diese IDEs sehr komplex und erschlagen gerade Anfangerinnen mit ihrem Funktionsumfang. Das ist auch der Grund, warum in diesem Kurs keine Java-Installation von lhnen verlangt wird -- wer es aber wissen und wer mit Java experimentieren mochte, die will ich keinesfalls davon abhalten.

Um ein Java-Programm, bestehend aus einer Menge von Class files, aus- zufuhren, muss man eine Klasse angeben, die eine Startmethodode besitzt.

Diese Startmethodode hei8t immer gleich; ihre Signatur hat die leicht zu merkende und immer wieder gern eingetippte Form

982public static void main(String[] args)

Dabei ist main der Name der Methode; was die anderen Elemente bedeuten, werden Sie im Laufe dieser Kurseinheit noch lernen. Auf Betriebsystemebene übergibt man dann einfach der JVM bei ihrem Aufruft den Namen der Klasse als Parameter, beispielsweise mit

983Java MeineTollsteKlasseBisher

Klassen werden in Java wie in Smalltalk per Konvention immer grossgrechrieben.

Ein letztes, wichtiges Merkmal des Programmiermodells von Java ist die **Deployment** Art des Deployment, also wie in Java programmierte Anwendungen in die Anwendung gehen. Wahrend fruher alle namhaften Web-Browser (per Plug-in) den Start von in Webseiten eingebettetten Java-Anwendungen erlaubten, bleibt heute praktisch nur noch die Verteilung per sog. Java Archive (einer.jar-Datei). Zu deren Ausfuhrung ist jedoch eine Installation der JVM vonnoten.

## 35 Objekte und Typen

Java-Programme sind objektorientierte Programme -- zur Laufzeit bestehen sie aus einer Menge interagierender Objekte. Dabei ist Java stark typisiert: Jedes Objekt gehort zum Wertebereich eines oder mehrerer Typen. Anders als in Smalltalk gibt es in Java neben Objekten auch Werte wie Zahlen, Zeichen und Wahrheitswerte, die keine Objekte sind.

In Java werden zunächst sechs Arten von Typen unterschieden: _primitive Typen, Klassentypen, Interfacetypen, Array-Typen, Aufzahlungstypen_

**Arten von Typen** und _Annotationstypen_. Von Klassen- und Interfacetypen gibt es seit Java 5 auch parametrisierte Varianten, die denen Strongtalks stark ahneln (die Java-Generics stammen teilweise von Autoren Strongtalks). Die primitiven Typen sind mit der Sprachdefinition festgeigt; es sind dies byte, short, int, long, float, double, boolean und char. Sie unterscheiden sich nicht sonderlich von denen gangiger, statisch typgeprufter prozeduraler Sprachen. Alle anderen Typen werden durch Typkonstruktion mittelsprechender Sprachkonstrukte in Java selbst definiert. Ein Teil dieser Typen ist jedoch mit der Sprachdefinition fest vorgegeben: So sieht Java für jeden primitiven Typ einen im wesentlichen gleichnamigen (mit Ausnahme von int und char bis auf Grosscheribung) Referenztyp vor, dessen Werte jeweils einen Wert eines entsprechenden primitiven Typs aufnehmen können. Diese Typen, namentlich Byte, Short, Integer, Long, Float, Double, Boolean und Character, nennt man deswegen _Wrapper-Typen_ (sie wickeln gewissermassen einen Wert eines primitiven Typs ein). Weitere Typen, die die Java-Sprachdefinition voraussetzt, sind Object, String, Throwable, Error, Exception, RuntimeException und Thread. Diese werden an entsprechenden Stellen unten weiter erlautert.

Genau wie in Smalltalk mussen auch in Java die Objekte irgendwo herkommen. Neben der Instanziierung von Klassen, wie Sie sie auch schon von Smalltalk her kennen, gibt es dafur auch in Java Literale.

### Literale

In Java gibt es Literale für Zahlen, Zeichen und Strings. für Arrays gibt es, da sie nicht aus Literalen zusammengesetzt sein mussen, etwas ahnliches, namlich die sog. _Array-Initialisie-rer_, sie werden in Kapitel 41 behandelt. Ob true und false bzw. null in Java Literaleoder Schlusselworter sind, hangt vom Standpunkt ab: Die meisten Syntaxeditoren behandeln sie wie Schlusselworter, gemass Sprachdefinition handelt es sich aber um Literale, die die beiden Booleschen Wahrheitswerte _wahr" und _falsch" bzw. den Wert des Nulltypen (**UndefinedObject** in **SMALLtalk**, in **Java** unbenannt) reprasentieren.

Zahlenliterale in Java können eine Vielzahl von Formen annehmen. für deri besondere Werte im Fliesskommabereich stehen allerdings keine Literale, sondern nur Konstanten zur Verfugung: Es sind dies **NaN** (fur das englische Not a Number) sowie **POSITIVE_INFINITY** und **NEGATIVE_INFINITY**. Zeichenliterale werden in Java durch einfache Anfuhrungstriche eingeschlossen, String-Literale durch doppelte. Beide können WikipediaA Escape-Sequenzen zur Darstellung von Sonderzeichen enthalten.

Anders als in **SMALLtalk** sind in Java Klassen keine Objekte. Dennoch **Klassenliterale** muss man in Programmen gelegentlich Klassen als Werte angeben. Das geht dann nicht (wie in **SMALLtalk**) per Angabe des Klassennamens (der dort ja zugleich als Pseudovariable definiert war), sondern mittels eines sog. **Klassenliterals**. Dies besteht aus dem Namen der Klasse, gefolgt von.class**, also beispielsweise

984Objectclass

Der Typ eines solchen Klassenliterals ist Class<T>, also im obigen Beispiel Class<Object>. Da in Java-Programmen Klassennamen auch direkt vorkommen durfen, so z. B. als Empfanger beim Aufruf von Klassenmethoden oder in Typtests wie **instanceof** (s. Abschnitt 35.4), sind Klassenliterale eher selten anzutreffen (die ganze Unterscheidung von Klassennamen und Klassenliteralen in Java ist m. E. alles andere als glucklich).

### Gleichheit und Identitat

In Java wird genau wie in **SMALLtalk** zwischen Gleichheit und Identitat von Objekten unterschieden. Die Gleichheit von Objekten wird mittels der Methode **equals**(.) (wobei (.) hier für einen nicht naher spezifizierten Parameter steht), die Identitat mittels == (bzw.!= für das Negat) geprut. **equals**(.) wird von der Klasse **Object** (in Java genau wie in SMALLtalk die Superklasse aller Klassen) geerbt und sollte in den Subklassen der jeweiligen Bedeutung von Gleichheitentsprechend überschrieben werden. Die Verwechselung von equals**(.) und == ist auch in Java ein ziemlich haufiger Programmierfehler (vgl. Abschnitt 1.4 in Kurseinheit 1). Das Gleichheitszeichen = steht in Java ubrigens (genau wie in C, C++ und C#) für die Wertzuweisung, was ich personlich für eine der grossen Tragodien der Informatik halte.

### Variablen und Zuweisungen

Java ist eine stark typisierte Sprache: Alle Ausdrucke haben einen Typ. Das gilt auch für Variablen, deren Typ bei ihrer Deklaration angegeben werden muss.

In Java gibt es Variablen mit _Referenz- und mit Wertsemantik_. Welche Semantik eine Variable hat, richtet sich nach ihrem Typ. Typen, die zu Variablen mit Wertsemantik fuhren, sind die oben genannten _primitiven_, namentlich **byte**,

**short**, **int**, **long**, **float**, **double**, **boolean** und **char**. Variablen, die mit einem anderen Typ deklariert werden, haben Referenzsemantik.

\begin{tabular}{c c}  & **Wertzuweisungen** \\ \end{tabular}

\begin{tabular}{c c}  & **und Inhalt von** \\ \end{tabular}

\begin{tabular}{c c}  & **Variablen** \\ \end{tabular}

Es gibt in Java genau wie in Smalltalk keine Moglichkeit, Pointerariablen explizit zu deklarieren; es gibt also insbesondere beim Methodenaufruf (und den damit verbundenen impliziten Zuweisungen) auch in Java kein _Call by reference_, sondern nur ein _Call by value_. Daran andert auch nichts, dass Variablen, die mit Referenztypen deklariert sind, Referenzsemantik haben -- bei den impliziten Zuweisungen eines Methodenaufrufs wird den formalen Parameterm immer eine Kopie des Zeigers übergeben. Siehe dazu auch die Bemerkungen in Abschnitt 4.3.2 (Kurseinheit 1) und Kapitel 37.

\begin{tabular}{c c}  & **Auto boxing und** \\ \end{tabular}

Seit Java 5 können Werte primitiven Typs an Variablen der entsprechenden Wrapper-Typen direkt zugewiesen werden und umgekehrt; dies **unboxing** nennt man **Auto boxing** bzw. **Auto unboxing**. Dabei können allerdings, genau wie bei der Handhabung bestimmter Werte als Objekte in Smalltalk (s. Abschnitt 1.4 in Kurseinheit 1), unenwartete Phanomene auftreten: Zwei Objekte, die den gleichen Wert reprasentieren, sind zwar immer gleich, mussen aber nicht identisch sein. Man muss also auch in Java genau überlegen, ob man die Equals-Methode oder den Test auf Identitat (==) verwendet; liegt man daneben, handelt man sich schwer zu findende Programmierfehler ein.

### Operationen und Methoden

\begin{tabular}{c c}  & **Trennung zwischen** \\ \end{tabular}

\begin{tabular}{c c}  & **Operationen und** \\ \end{tabular}

\begin{tabular}{c c}  & **Methoden** \\ \end{tabular}

\begin{tabular}{c c}  & **Methoden** \\ \end{tabular}

\begin{tabular}{c c}  & **Wertzuweisungen** \\ \end{tabular}

\begin{tabular}{c c}  & **und Inhalt von** \\ \end{tabular}

\begin{tabular}{c c}  & **Variablen** \\ \end{tabular}

\begin{tabular}{c c}  & **Wertzuweisungen** \\ \end{tabular}

\begin{tabular}{c c}  & **Unhalt von** \\ \end{tabular}

\begin{tabular}{c c}  & **Variablen** \\ \end{tabular}

\begin{tabular}{c c}  & **Wertzuweisungen** \\ \end{tabular}

\begin{tabular}{c c}  & **Unhalt von** \\ \end{tabular}

\begin{tabular}{c c}  & **Variablen** \\ \end{tabular}

\begin{tabular}{c c}  & **Wertzuweisungen** \\ \end{tabular}

\begin{tabular}{c c}  & **Unhalt von** \\ \end{tabular}

\begin{tabular}{c c}  & **Variablen** \\ \end{tabular}

wesentlich gepragt und was ihr bei manchen den Ruf einer hybriden Programmiersprache (halb objektorientiert, halb imperativ) eingebracht hat. Aus meiner Sicht ist die Unterscheidung zwischen Objekten und Werten, wie sie in JAVA vorgenommen wurde, aber sinnvoll: Werte haben weder Identitat noch Zustand, was also macht sie zu Objekten?

Die Methoden JAVAK kann man in Prozeduren und Funktionen aufteilen, wobei der einzige Unterschied ist, dass Prozeduren nichts zuruckgeben und deswegen void anstelle des Ruckgabetyps deklarieren. Es ist dies eine der vielen Erb-schaften von der Programmiersprache C.

Ein Operator, der speziell für Referenztypen zur Verfugung steht, ist der Typtest instanceof: Er erlaubt es zu prufen, ob ein Objekt Element (Instanz) eines Typs ist. Dabei wird nicht zwischen _direkten_ und _indirekten_ _Instanzen_ unterschieden: x instanceof Object wertet also immer zu true aus, egal, für welches Objekt x steht. Mehr zur Bedeutung des Typtests in Kapitel 44.

### Zuweisungskompatibilitat

In JAVA ist die Typkonformitat und damit die Zuweisungskompatibilitat unter Referenztypen an Subtyping gebunden: Damit Ausdrucke von einem Typ Variablen eines anderen zugewiesen werden können, mussen die Typen entweder gleich sein oder es muss eine Subtypbeziehung zwischen den beiden bestehen. In den meisten Fallen muss die Subtypbeziehung explizit deklariert werden; JAVA setzt also auf _nominale Typkonformitat_. Dies hat den in Abschnitt 22.2 von Kurseinheit 3 beschriebenen Vorteil der Filterfunktion, aber auch den Nachteil, dass Subtypen ihre Supertypen namentlich kennen mussen, was insbesondere bei verteilten Anwendungen, deren Teile nicht von vornherein fureinander entworfen waren (Web Services beispielsweise), von Nachteil ist. Weiterhin verlangt das Subtyping JAVAK, dass die Typen gewder Variablen (Felder und Parametertypen von Methoden) nicht abgeandert werden -- JAVA verlangt also _Novarianz_. Damit wird zumindest eine statisch-semantische Substituierbarkeit von Objekten der Subtypen gegen die ihrer Supertypen sichergestellt (vgl. Abschnitt 26.3 und Kapitel 54 in Kurseinheit 6). Allerdings kann der Ruckgabetyp von Methoden kovariant redefiniert werden; mehr dazu in Abschnitt 36.4.

Im Gegensatz zu ihren Vorlaufern Smalltalk und C++ ist JAVA eine Sprache mit einem strengen Typsystem. Das heisst insbesondere, dass in JAVA

**Typfehlern**

_alle_ Typfehler entweder schon wahrend der übersetzung vom Compiler oder aber wahrend der Ausfuhrung vom Laufzeitsystem, dann aber schon zum fruhestmoglichen Zeitpunkt, namlich bei einer Wertzuwiesung (bei der ja die Verletzung einer Typinvariante entsteht), abgefangen werden. In einem Fall kann man jedoch der Meinung sein, dass die Typinvarianten Javas zu lax gefasst sind, also Zuweisungen gestattet werden, von denen man nicht ausschlieBen kann, dass sie in der Folge zu einem Typfehler fuhren. Mehr dazu in Kapitel 41.

## 36 Klassen

Javaist (wie SMALITalk und alle in der nachsten Kurseinheit behandelten Sprachen) klassenund nicht prototypicalenbasiert; man programmiert also, indem man Klassendefinitionen angibt. Wie bereits in Kapitel 34 erwahnt gibt es in Java keine Anweisungen ausserhalb von Klassen (sieht man einmal von Import-Anweisungen ab).

Wie dort ebenfalls bereits erwahnt gibt es in Java einen relativ engen & Klassen und Dateien, Zusammenhang zwischen Klassen und Dateien: Jede Datei enthalt die Definition einer Klasse, die den Dateinamen (ohne Erweiterung) als Namen tragt. Eine Datei (oder _Compliation unit_) kann auch mehrere Klassen enthalten, die dann naturlich anders heissen -- unter ihnen darl jedoch keine als **public** deklariert werden. Schon weil die meisten integrierten Entwicklungsumgebungen für Java heute auf Dateibasis arbeiten und Dateien die Basis von vielen Versionsverwaltungssystemen sind, ist es jedoch wenig gebrauchlich, mehrere Klassen in einer Datei zu definieren (es sei denn, es handelt sich um _innere Klassen_; s. u.).

Nun hatten wir ja bereits in Kurseinheit 3, Kapitel 28, gesagt, dass Klassen & Klassen und Typen und Typen zunächst zwei verschiedene Konzepte sind, dass aber eine Typdefinition aus einer Klassendefinition abgeleitet werden kann. Genau so verhalt es sich in Java: Jede Klasse definiert ihren eigenen Typ. Genauer: Jede Klasse spezifiziert einen Typ, der genauso hei8t wie die Klasse und der als Eigenschaften die Felddefinitionen und die Methodedeklaratiohen der Klasse enthalt. Eine Deklaration

985 &Klassenname> <variablenname> ist also eine gultige Variablendeklaration in Java. Man beachte, dass, anders als in STRONGTAK, in Java der Typ bei Deklarationen ohne spitze Klammern vorangestellt wird. Es folgt dies der Tradition von C und C++. Die spitzen Klammern in Zeile 985 kennzeichnen hier lediglich wieder _metasyntaktische Variablen_.

### Klassendefinitionen

Eine einfache Klassendefinition sieht in Java wie folgt aus:

986class <Klassenname> {
987<Typ 1> <feld1>;
988 _ -
989<Ruckgabettyp 1> <methodel>(<Parametertyp 1> <parameter 1>, _) {_}
990 _ -
991}

Die geschweiften Klammern sind in Java (wie auch in C und allen syntaktisch davon abgeleiteten Sprachen) Begrenzer für Definitionen und Blocke; sie entsprechen den Schlusselwortern **begin** und **end** von Pascal. Die spitzen Klammern kennzeichnen auch hier wieder metasyntaktische Variablen (also Platzhalter für richtige Namen).

Die obige Klassendefinition teilt sich in die Angabe von _Instanzvariablen_,

die in Java **Felder** genannt werden, und _Instanzmethoden_, die in Java

Beide werden, der Tradition von C++ folgend, zusammenfassend auch als **Member** bezeichnet, wobei sich Member (das englische Wort für ein Element einer Menge) auf die Klassendefinition (oder _Intension_; vgl. Abschnitt 7.2 in Kursenheit 1) bezieht. Konstruktoren zahlen nicht zu den Membern; sie werden in Abschnitt 36.3 behandelt.

Neben Feldern und Methoden kann eine Klassendefinition in Java auch

**innere Klassen** geschachtelte sowie sog. **innere Klassendefinitionen** besitzen. Diese Klassendefinitionen gelten dann ebenfalls als Member der umschliesenden Klasse. Sie sind vor allem dann sinnvoll, wenn man ausdrucken will, dass die Existenz der inneren Klasse ohne die der ausseren sinnlos ware. So ist es beispielsweise ublich, wenn man verzeigerten Listen implementiert, die Klasse der Listenelemente, deren Instanzen neben dem eigentlichen Inhalt auch noch einen oder mehrere Zeiger aufnehmen mussen, innerhalb der Klasse der Liste zu definieren, denn diese Listenelemente wird man kaum ausserhalb einer Liste verwenden (und ihre Klasse auch gar nicht kennen) wollen. Innere Klassen werden zudem im Kontext von Instanzen ihrer ausseren Klasse(n) instanziiert; Instanzen innerer Klassen liegen somit,,innerhalb" von Instanzen ihrer ausseren Klasse(n), auf die sie mit einem **Outer this** genannten Konstrukt zugerefen können.

Member können auch mit dem Zusatz **static** deklariert werden. Dabei

**-methoden in Java** bedeutet static für so deklarierte Felder und Methoden, dass sie sich

nicht auf Objekte beziehen (die ja dynamische Gebilde sind), sondern auf die Klasse selbst, in der sie definiert sind. Es handelt sich also um _Klassenvariablen_ und _-methoden_. Da in Java

im Gegensatz zu Smalltalk Klassen selbst keine Objekte, sondern wahrend der Programmausfuhrung dauerhaft existierende, unveränderliche Gebilde sind, die nicht in Variablen gespeichert werden können, werden als static deklarierte Member auch nicht dynamisch gebunden.

Achtung: Man konnte im Fall von static deklarierten Feldern meinen,

**,****statisch" heiSt nicht** dass diese dadurch zu Konstanten wurden; das ist aber nicht der Fall.

**,****konstant"** Dazu dient in Java das Schlussekwort final, das für Variablen aussagt, dass ihnen genau einmal ein Wert zugewiesen werden darf. Im Gegensatz dazu brauchte man im schlusssekwortlosen Smalltalk für Konstanten noch _konstante Methoden_ (Abschnitt 4.3.6). Auf Methoden angewandt bedeutet final, dass diese nicht in Subklassen überschrieben werden durfen; mehr dazu im nachsten Abschnitt.

### Subklassenbeziehung

Es ist in Java wie in Smalltalk vorgesehen, dass alle Klassen ausser Object von bereits existierenden ableiten. Java verwendet dazu das Schlusselwort **extends**:

```
992class B extends A{
993
994Es wird dadurch das Bestehen einer _Subklassenbeziehung zwischen B und A deklariert_. Die Verwendung von **extends** legt bereits nahe, dass es sich dabei zugleich um eine _Typerweiterung_ handelt, aus der (gemass Kapitel 23) _Zuweisungskompatibilitat_ folgt; tatsachlich ist das auch so.

Durch Angabe einer Extends-Klausel gibt eine Klasse an, von welcher anderen Klasse sie die nicht static deklarierten Member erbt. Da die erbende Klasse, auch in Java _Subklasse_ genannt, die ggerbten Methoden nur invariant überschreiben darf (und ggerbte Felder in ihrer Sichtbarkeit nicht reduziert werden durfen; s. Abschnitt 39.1), ist ihr Typ automatisch Subtyp des Typs der Klasse, von der sie erbt.

Genau wie in SMalltalk gibt es in Java _abstrakte Klassen_. Anders als **abstrakte Klassen**. SMalltalk spendiert Java jedoch ein Schlosselwort **abstract**, mit dem man eine Klasse als abstrakt und damit als nicht instanzierbar deklarieren kann. Man Schreibt dazu einfach

995**abstract class A (-)**

Das bedeutet, dass von einer solchen Klasse keine Instanzen mehr gebildet werden durfen (vgl. Abschnitt 10.3). Dabei ist dieses Verbot, dessen Beachtung vom Compiler überproft wird, vollkommen unabhangig davon, ob von der Klasse Instanzen gebildet werden _konnten_ -- selbst wenn alles, was man für das Funktionieren der Instanzen benotigt, in der Klasse vorhanden ist (einschliellich Konstruktoren), darf sie nicht instanziert werden. Sehr viel haufiger ist aber der Fall, dass der Klasse die Implementierung von einer oder mehreren (bis hin zu allen) benotigten Methoden fehlt; diese Methoden werden dann in der Klasse lediglich deklariert, und zwar ebenfalls mit dem Schlussewort **abstract**:

996**abstract <Ruckgabettyp> <methode>(<Parametertyp> <parameters>, -)**: Man gibt dann hinter der Methodensignatur (also dem Namen und den Parametern) keine Implementierung (in geschweiften Klammem) an, sondern lediglich ein abschliessendes Semikolon. Im Gegensatz dazu muste ja in SMalltalk eine abstrakte Methode durch einen Aufruf von implementedBySubclass o. a. gekennzeichnet (s. Abschnitt 10.3 in Kurseinheit 2) werden.

Die Aufforderung, eine abstrakte Methode in einer Subklasse zu implementieren, gibt es in Java auch, allerdings nicht per Laufzeitfehler auf **abstrakten Klassen**. Programmausfuhrungsbene, sondern auf Compilerebene. Wenn man namlich von einer abstrakten Klasse (per **extends**) ableitet, dann muss die abgeleitete Klasse entweder selbst als abstrakt deklariert sein oder man muss alle abstrakten Methode der Klasse, von der sie ableitet, mit Implementierungen versehen. Tut man das nicht, erhalt man vom Compiler eine entsprechende Aufforderung.

Komplementar zur Abstract-Deklaration gibt es in Java auch die Moglichkeit, zu verhindern, dass von einer Klasse abgeleitet wird: Man Schreibt dazu anstelle von **abstract** einfach **final**. Dasselbe gilt für einzelne Methoden, deren überscheiben in einer Subklasse man durch eine Final-Deklaration verhindern kann. Eineeinfache, goldene Regel der objektorientierten Programmierung ist ubrigens, dass man alle Klassen entweder als abstrakt oder als final deklarieren soltte; dies setzt das Prinzip der abstrakten Generalisierungen durch und vermeidt die Probleme von nur von Vererbung getriebenen Klassenhierarchen (Kapitel 9 in Kurseinheit 2 und 69 in Kurseinheit 6).

### Konstruktoren

Objekte, für die es keine literale Repräsentation gibt, mussen in Java (wie in SMALLtalk) explizit, als Instanzen von Klassen, erzeugt werden. Dazu gibt es in Java eine spezielle Kategorie von Methoden, _Konstruktoren_ genannt, die, anders als in SMALLtalk, keine Klassenmethoden sind, sondern zwischen Klassen- und Instanzmethoden stehen. Dabei sind Konstruktoren wie Instanzmethoden, weil in ihrem Rumpf auf alle Felder und Methoden der neu erzeugten Instanz zugegriffen werden kann (und zwar genau so, als sei der Konstruktor eine Instanzmethode, die auf der neu erzeugten Instanz aufgerufen wurde). Konstruktoren können also all die Anweisungen enthalten, für die in SMALLtalk noch eine spezielle Methode initialize notwendig war (vgl. Abschnitt 8.2 in Kurseinheit 2). Konstruktoren sind aber auch wie Klassenmethoden, weil sie eben nicht auf einer Instanz aufgerufen werden, sondern auf der Klasse. Allerdings sieht Java dafur keine spezielle Klassenmethode new o. a. vor, sondern verwendet den Klassennamen selbst wie einen Methodennamen. Wenn man also, von SMALLtalk kommend, etwas der Form

```
997classA{
998staticAnew(<formaleParameterliste>){_}//Klassenmethode
999-
1000Aa=A.new(<tatsachlicheParameterliste>);
1001-
10021enwartenwurde, findet man in Java stattdessen
1003classA{
1004A(<formaleParameterliste>){_}//Konstruktor
1005-
1006Aa=newA(<tatsachlicheParameterliste>);
1007-
10081-
10081-
10081-
10081-
1003
1004Wie man sieht, erlauben Konstruktordefinitionen in Java anders als (andere) Methoden keine Angabe eines Ruckgabetypen -- da die erzeugte Instanz immer eine der Klasse ist, in der der Konstruktoren definiert ist, steht der Typ fest. Die Angabe des Ruckgabetyps in Zeile 998 ware also redundant.

Wenn man keinen Konstrukttor definiert, nimmt Java stets den (impliziten) Standardkonstruktor an, der parameterlos ist und der nichts weiter tut, als eine neue Instanz der Klasse zu liefern. AuSendem werden Konstruktoren nicht verebt; stattdessen wird der Standardkonstruktor einer Klasse beim Erzeugen einer Instanz von einer ihrer Subklassen automatisch mit aufgerufen. Um dieses Verhalten zu überschreiben, kann man aus einem Konstrukttor heraus einen beliebigen Konstruktor der Superklasse mittels **super** aufrufen; darin wiederum aufgerufene Methoden werden dann dynamisch gebunden, was dazu fuhren kann, dass von diesen Methoden auf noch nicht initialisierte Variablen zuruckgegriffen wird. Tatsachlich ist der ganze Komplex Konstruktoren und Initialisierung von Variablen in Java recht komplex, was, da Instanzierung und Initialisierung fundamentale und für jedes Programm unverzichtbare Vorgange sind, nicht gerade für Java als Anfangerinnensprache spricht.

Konstruktionen zur Objekterzeugung mit Klassenmethoden wie oben (Zeile 998) sind in Java ubrigens auch moglich; allerdings muss eine solche Klassenmethode dann in ihrem Rumpf einen Konstruktor wie in Zeile 1006 aufrufen. Man spricht dann von der Klassenmethode auch als einer _Factory-Methode_ (vgl. Abschnitt 8.3 in Kurseinheit 2); sie kann auch instanzen anderen Typs als des deklarietten zuruckgeben.

### überschreiben, überladen und dynamisches Binden

Nun hat die Subklasse die Moglichkeit, neue Member hinzuzufugen und **überschreiben** bereits bestehende zu redefinieren. In Java ist die Moglichkeit der Redefinition auf die Moglichkeit des überschreibens eingeschrankt, was soviel heisst wie dass eine Methode mit der gleichen Signatur (bestehend aus Methodenname und formalen Parametertypen) noch einmal definiert werden kann, und zwar mit geanderter Implementierung. Auch darf die Methode den Ruckgabetyp kovariant, also nach unten, abandern (vgl. dazu die Diskussion in Kurseinheit 3, Abschnitt 26.3). Dass die überschreibende Methode über die Einhaltung der Typinvarianten, die mit ihren (geerbten) Parametern verbunden sind, hinaus nur etwas tut, das mit der überschriebenen Methode kompatibel ist, dass sie also nicht mit dem erwarteten Verhalten bricht, kann durch die Sprachdefinition Java sicht erzwungen werden -- hier ist die Programmiererin in der Verantwortung (vgl. dazu auch die Abschnitte 52.6 in Kurseinheit 5 und 54.1 in Kurseinheit 6).

Nun kann man in Java auch Methoden mit gleichem Namen, aber verschiedenen Parametertypen in derselben oder einer Subklasse haben. Diese Methoden nennt man dann **überladen**. Es ist wichtig, zu verinnerlichen, dass in Java überladen und überschreiben zwei grundverschiedene Dinge sind, obwohl man in beiden Fallen nichts weiter tut als eine Methode mit bereits vorhandenem Namen noch einmal zu definieren: Beim überladen wird eine neue Methode eingefuhrt, beim überschreiben wird eine bereits bestehende redefiniert. Diese Unterscheidung spielt beim dynamischen Binden eine entscheidende Rolle.

Um das dynamische Binden Java genau zu verstehen (und damit das **dynamisches Binden** Verhalten eines Programms vorhersagen zu können), muss man sich den Bindelgorithmus vor Augen halten. Dieser geht wie folgt vor.

Bereits zur übersetzungszeit wird ein dynamischer Methodenaufruf lose an eine Methoden-deklaration gebunden, und zwar an genau die, die die folgenden Bedingungen erfullt:

1. Sie hat den gleichen Namen und die gleiche Anzahl Parameter59 wie die aufgerufene Methode.
2. Sie ist in der Klasse, die zu dem deklarierten Typ des Ausdrucks gehort, der das Empfangerobjekt liefert (nicht selten einfach eine Variable), deklariert oder wird von einer ihrer Superklassen geerbt.
3. Die deklarierten Parametertypen des Aufrufs (die deklarierten tatsachlichen Parametertypen) sind jeweils Subtypen der deklarierten Parametertypen der Methodendeklaration (der deklarierten formalen Parametertypen).
4. Es gibt keine andere Methode, die die gleichen Voraussetzungen erfullt, deren deklanierte formale Parametertypen aber gleich weit entfernt oder naher an den Typen des Aufrufs sind (Entfernung hier gemessen als die Anzahl der Subtypen, die dazwischen liegen).

Damit ist dann die oberste (Wurzel) einer Menge von Methoden gefunden, die moglicherweise in Subklassen überschrieben wird und an eine von denen der Methodenaufruf dann dynamisch gebunden wird. Man beachte, dass die überschreibenden Methoden dieselbe Signatur haben mussen wie die überschriebene; diese Methoden bilden eine Art Familie, von der eine zur Bindung herausgesucht wird.

Zur Laufzeit wird dann nur noch der tatsachliche Typ des Empfangerobjekts (die Klasse, von der es eine Instanz ist) bestimmt. Dieser muss, aufgrund der Regelin der Zuweisungskompatibilitat, ein Subtyp des deklarierten Typs des Ausdrucks sein, der das Empfangerobjekt liefert. Mit diesem tatsachlichen (auch dynamisch genannten) Typ wird dann aus der zuvor bestimmten Menge von in Frage kommenden überschriebenen Methoden die ausgesucht, die in der Klasse definiert wurde, die der Klasse des Empfangerobjekts in der Kette der Superklassen die nachste ist.

Wenn bei der Suche nach einer Methode zur übersetzungszeit nach obi- **Method ambiguous** gem Algorithmus (Schritt 4) eine oder mehrere andere Methodenfinitionen gleich weit von der aufgerufenen entfernt sind, dann meldet der Compiler einen sog. _Method ambiguous error_, der bedeuten soll, dass die aufgerufene Methode durch den Aufruf nicht ein-deutig bestimmt ist. Man beachte, dass der Fehler durch Methodenaufrufe, nicht durch Methodendeklarationen verursacht wird; wenn man den problematischen Aufruf entfernt, gibt es auch keinen Fehler mehr. Der einfachste Fall eines solchen Fehlers ergibt sich durch den Aufruf

1009 System.out.println(null)bei dem unklar ist, ob println(null) an die Implementierung von println(String), println(Object) oder von println(char[]) gebunden werden soll.

Man beachte, dass in Sprachen, in denen das dynamische Binden neben dem Typ des Empfangers auch die Typen der tatsachlichen Parameter berucksichtigt (das sog. _Multi-dispatch_), der Unterschied zwischen überladen und überschreiben dahinschmilt. In Java muss hingegen das dynamische Binden anhand der Parametertypen genau wie in Smalltalk über _Double dispatch_ (s. Abschnitt 12.3 in Kurseinheit 1) simuliert werden.

## 37 Ausdrucke

Ausdrucke sind in Java

* Literale,
* Variablen,
* die spezielle Variable this,
* Operatoranwendungen,
* Feldzugriffe der Form **a**.**x, wobei **a** für den Besitzer des Feldes (ein Objekt oder eine Klasse) und **x** für das Feld (die Instanz- bzw. Klassenvariable) steht (**a** kann auch durch **super** ersetzt werden),
* Methodenaufrufe der Form **a**.**m(_), wobei **a** für den Empfanger des Aufrufs steht oder für **super**, **m** für die Methode und _ für die tatsachlichen Parameter (die wiederum Ausdrucke sind),
* Array-Zugriffe der Form **a[i]**, wobei **a** für das Array und **i** für einen Index steht (eine ganze, positive Zahl; bei mehrdimensionalen Arrays können entsprechend weitere Indizes in eckigen Klammern angegeben werden),
* Klasseninstanziierungen der Form **new <Klassenname>** (<Parameter>)
* Array-Instanziierungen der Form **new <Basisstypname>** [<n>], wobei <Basisstypname> für den Typ der Elemente steht (also z. B. int bei einem Array von Integem) und <n> für einen Ausdruck, dessen Auswertung eine ganze, positive Zahl liefert (es können auch mehrere Dimensionen angegeben werden),
* Konditionalausdrucke der Form <Boolescher Ausdruck>? <Ausdruck 1> : <Ausdruck 2>, wobei in Abhangigkeit davon, ob <Boolescher Ausdruck> zu wahr oder zu falsch auswertet, entweder <Ausdruck 1> oder <Ausdruck 2> ausgewertet wird und das Ergebnis des Gesamtausdrucks liefert,
* Cast-Ausdrucke der Form (<Typname>) <Ausdruck>, wobei <Typname> für das Ziel des Casts steht und <Ausdruck> für den Ausdruck, dessen Ergebnis den mit <Typname> bezeichneten Typ annehmen soll, sowie* Lambda-Ausdrucke der Form (<Parameterdeklarationen>) -> <Rumpf>, wobei <Parameterdeklarationen> den formalen Parameterdeklarationen einer Methode onstpicht und <Rumpf> entweder eine einzelne Anweisung oder ein Block von Anweisungen, entsprechend einem Methodenrumpf (inkl. der geschweiften Klammern) ist. Falls nur ein Parameter deklariert wird, können die runden Klammern auch weggelassen werden.

Wie man sieht, können in Java Ausdrucke rekursiv aus anderen aufgebaut werden: Methodenausdrucke beinhalten einen Ausdruck, der für den Empfanger steht sowie moglicherweise weitere, die für die Parameter des Methodenaufrufs (,,der Nachricht") stehen, ArrayZugriffe und -Instanzierungen beinhalten Ausdrucke zur Bestimmung des Indexes bzw. der Grosse, etc. Dabei mussen die Ausdrucke alle korrekt typisiert sein in dem Sinne, dass der Typ jedes Ergebnisse eines inneren Ausdrucks mit dem der Stelle des aüberen, an der er eingesetzt wird, zuweisungskompatibel sein muss.

Genau wie in Smalltalk, aber anders als in einigen anderen objektorien-tierten Programmiersprachen (z. B. C++, C#) gibt es in Java nur _Call by value_ und kein _Call by reference_; Methoden, die einem tatsachlichen Parameter einen anderen Wert zuweisen (wie z. B. eine Methode, die den Inhalt zweier Variablen tauscht), sind daher in Java nicht moglich.60 Dies stellt eine erhebliche Einschrankung dar.

Die Lambda-Ausdrucke von Java, die mit Version 8 eingefuhrt wurden,

**Typ von Lambda-**

ersetzen die bis dahin geubte Pravis, Funktionen über anonymme innere

**Ausdrucken**

Klassen, die ein Interface (s. Abschnitt 40) mit nur einer Methode implementieren, in Objekte zu verbacken. Gebleben ist die Tatsache, dass Lambda-Ausdrucke den Typ eines Interfaces haben, der allerdings nicht direkt angegeben, sondern inferiert wird, und dass die Funktionen, die die Lambda-Ausdrucke darstellen, über das Interface einen Namen erhalten.,,Anonyme" Funktionen oder Blocke wie in Smalltalk können in Java über vorderfinierte Interfaces erstellt werden: So liefert

1010Function<Integer, Integers> f = x -> x * x:

ein Objekt vom (Interface-)Typ Function, der wie folgt deklariert ist (zur Bedeutung von <T, R> s. Kapitel 43):

1011public interface FunctionsT,R> {R apply(T t): }

Demnach heilst die Funktion des Funktionsobjekts,,apply"; der Ausdruck f.apply(2) liefert entsprechend 4. Hierbei entspricht apply(.) dem aus Smalltalk bekannten value: (s. Abschnitt 4.4 in Kurseinheit 1).

Ahnlich wie in Smalltalk Blockce können Lambda-Ausdrucke in Java Kontext einfangen und mitnehmen (vgl. Abschnitt 4.4.1 in Kurseinheit 1). Allerdings mussen die freien (lokalen) Variablen, die aus dem Kontext eingefangen werden können, final deklariert sein (oder zumindest final deklariert sein können, also ihren Wert nicht mehr andern) und ein Ruckspringen aus dem Home context mittels return aus dem Lambda-Ausdruck ist nicht vorgesehen.

Abgesehen von der Typisierung sind die wesentlichen Unterschiede zu

Smalltalks Ausdrucken (Abschnitt 4.1 in Kurseinheit 1) die folgenden:

\begin{tabular}{c c}  & **wesentliche** \\  & **Unterschiede zu** \\  & **Smalltalk** \\  & **Smalltalk** \\  & **In Java gibt es keine indiierten Instanzvariablen -- diese werden durch Arrays als eigenstandige Objekte ersetzt. Array-Objekte können über keine benannten Instanzvariablen verfugen. \\  & **In Java** wird zwischen Operatoranwendungen (**+**, - etc.), Methodenaufrufen, dem Aufruf von Konstruktoren und Arrayzugriffen unterschieden -- in Smalltalk gibt es nur Methodenaufrufe. \\ \end{tabular}

## 38 Anweisungen, Blocke und Kontrollstrukturen

Genau wie in Smalltalk werden in Java Ausdrucke im Rahmen der Ausfuhrung von Anweisungen ausgewertet. Anders als in Smalltalk gibt es in Java jedoch eine Vielzahl von Schlusselwortern, die Anweisungen einleiten. Dennoch ist es auch in Java moglich, bestimmte Ausdrucke zu Anweisungen zu machen: Man schliebst einfach einen betreffenden Ausdruck durch ein Semikolon ab. Insbesondere werden so Variablendeklarationen, Wertzuweisungen, Methodenaufrufe und Klasseninstanzierungen (s. Kapitel 37) direkt zu Anweisungen. Man beachte, dass, anders als das Semikolon in Pascal oder der Punkt in Smalltalk, das Semikolon in Java kein Trennzeichen, sondern Teil der Anweisung ist.

Nahezu alle Anweisungen finden sich in Java-Programmen innerhalb von Methoden.61 Blokce sind in Java lediglich (in geschweifte Klammern eingefasste) Abschnitte des Quelltextes, die die an die Stelle einzelner Anweisungen treten können und die einen Sichtbarkeitsbereich für darin enthaltene Variablendeklarationen darstellen. Blocke wie in Smalltalk kennt Java erst seit Version 8, als _Lambda-Ausdrucke_.

Es sind also Variablendeklarationen, Methodenaufrufe (inkl. der Konstruktoraufrufe) und Zuweisungen Anweisungen. Alle anderen Anweisungensungen werden durch Schlusseworter eingeleittet und realisieren allesamt Kontrollstrukturen, die den Kontrollfluss eines Programms dazu bringen, von der normalen, sequentiellen Ausfuhrung abzuweichen. Im einzelnen sind dies

die If-Anweisung der Form if (<Boolescher Ausdruck>) <Statement>, bei der <Statement> genau dann ausgefuhrt wird, wenn <Boolescher Ausdruck> zu true auswertet;

die If-else-Anweisung der Form if (<Boolescher Ausdruck>) <Statement 1> else <Statement 2>, bei der <Statement 1> genau dann ausgefuhrt wird, wenn <Boolescher Ausdruck> zu true auswertet, und <Statement 2> sonst;

die Switch-Anweisung der Form

switch (<Ausdruck>) {

case <Literal 1> : <Anweisungsliste 1>

case <Literal 2> : <Anweisungsliste 2>

-

default: <Anweisungsliste>

)

wobei <Ausdruck> sowie <Literal 1>, <Literal 2> etc. alle vom Typ char, byte, short, int (bzw. einem der dazugehrigen Wrapper-Typen), String oder von einem Aufzahlungstyp sein mussen und <Anweisungsliste 1> etc. für Folgen von Anweisungen stehen können, die jeweils mit einem break; abgeschlossen werden können (aber nicht mussen);

die While-Anweisung der Form while (<Boolescher Ausdruck>) <Statement>, die im wesentlichen der If-Anweisung entspricht mit dem Unterschied, dass <Statement> nicht nur einmal ausgefuhrt wird, sondern solange, bis <Ausdruck> zu false auswertet;

die Do-Anweisung der Form do <Statement> while (<Boolescher Ausdruck>), die im wesentlichen dem While-Statement entspricht mit dem Unterschied, dass <Ausdruck> immer erst nach Ausfuhrung von <Statement> ausgewertet wird (man beachte, dass Statement kein Block sein muss; das das Statement abschliesende Semikolon wirkt dann etwas deplaziert (so wie das vor else beim If-Statement);

die For-Anweisung in der Form

for (<Initialisierungsausdruck>; <Boolescher Ausdruck>; <Veränderungsausdruck>) <Statement>62die <Statement> solange ausfuhrt, bis der Boolesche Ausdruck zu **true** auswertet (auf die schier unendlichen Moglichkeiten, was sich alles in <Initialisierungsausdruck> und <Veränderungsausdruck> unterbringen lasst, gehen wir hier nicht ein; traditionell wird im Initialisierungsausdruck jedoch ein Anfangswert für eine Laufvariable63 gesetzt, der dann im Veränderungsausdruck modifiziert, nicht selten hochgezahlt, wird);
* die (enweiterte) For-Anweisung in der Form for (<Variable> : <Ausdruck>) <Statement>, die <Statement> für alle Werte, die <Ausdruck> liefert, einmal ausfuhrt, und zwar mit dem jeweiligen Wert als Inhalt der Variable (wobei <Ausdruck> zu diesem Zweck entweder vom Typ eines Arrays sein oder das Interface Iterable implementieren muss, was soviel bedeuttet wie dass das Objekt, zu dem <Ausdruck> auswertet, die Methoden hasNext() und next() anbieten muss);
* die Break-Anweisung der Form break; bzw. break <Label>:, die innerhalb von Schleifen oder Switch-Statements dazu fuhrt, dass diese sofort verlassen werden, wobei <Label> sich auf ein Label bezieht, das einer auseren Schleife oder einem ausBeren Switch-Statement vorangestellt wurde;
* die Continue-Anweisung der Form continue; bzw. continue <Label>:, die innerhalb von Schleifen dazu fuhrt, dass der Rest des innersten bzw. des durch <Label> bezeichneten Schleifenrumpfs für den aktuellen Durchlauf nicht mehr ausgefuhrt wird, sondern sofort mit dem nachsten Durchlauf, falls vorhanden, weitergemacht wird (Continue-Anweisungen außerhalb von Schleifen bzw. mit einer Nicht-Schleife als Label sind ein Syntaxfehler);
* die Return-Anweisung der Form return; bzw. return <Ausdruck>:, die bewirkt, dass die umschliessende Methode sofort beendet und ggf. der Wert der Auswertung von <Ausdruck> zuruckgegeben wird (return; daf auch in einem Konstruktor vorkommen);
* die Synchronized-Anweisung der Form synchronized (<Ausdruck>) <Block>, die dafur sorgt, dass der durch <Block> bezeichnete Anweisungblock nur ausgefuhrt wird, wenn das mit dem Objekt, zu dem <Ausdruck> auswertet, verbundene Lock dies zulast (s. Abschnitt 47.3);
* die Try-Anweisung der Form

try <Try-Block>

catch (<formaler Parameter 1>) <Catch-Block 1>

catch (<formaler Parameter 2>) <Catch-Block 2>

-

finally <Finally-Block>wobei <Try-Block> für einen Block steht, von dessen Ausfuhrung man weiss, dass sie durch einen Laufzeitfehler abgebrochen werden kann, wobei mit den Sequenzen catch (<formalerParameter1>) <Catch-Block1> usw. für verschiedene Arsten von Laufzeitfehlenm verschiedene Behandlungsblocke angegeben werden können und wobei finally <Finally-Block> einen Block zu spezifizieren erlaubt, der immer ausgefuhrt wird, nachdem alle anderen Blocke ausgefuhrt (oder abgebrochen) wurden (kann auch weggelassen werden);
* die Throw-Anweisung der Form throw <Exception>;, die das Programm eine Exception werfen lasst;
* die Assert-Anweisung der Form assert <Ausdruck 1>; oder assert <Ausdruck 1> : <Ausdruck 2>;, wobei <Ausdruck 1> ein Boolescher Ausdruck und <Ausdruck 2> von beliebigem Typ ausser dem von void sein muss, mit der Bedeutung, dass wenn <Ausdruck 1> zu false auswertet, dass dann das Programm mit einer entsprechenden Fehlemmedung abgebrochen wird, wobei ggf. das Ergebnis von <Ausdruck 2> mit der Fehlemmedung ausgegeben wird.

Ausserdem ist die leere Anweisung, bestehend aus einem einzelnen Semikolon, eine Anweisung.

Bemerkungen:

* Das Weglassen von **break**; am Ende einer Liste von Anweisungen in einem Case-Zweig der Switch-Anweisung wird als _Fall through_ bezeichnet und bewirkt, dass mit den Anweisungen des nachsten Case-Zweigs fortgefahren wird. Dies ermoglicht, mehrere Falle zusammenzufuhren, ist aber eines der fehlertrachtigsten Konstrukte C-artiger Sprachen.
* Die Assert-Anweisung kann _Seiteneffekte_ haben, also z. B. die Werte von Variablen aus umgebenden Blocken oder von Instanzvariablen andern. Wenn der Ablauf des Programms von diesen Werten abhangt, macht es einen Unterschied, ob ein Programm mit oder ohne Prufung der Assertions ausgefuhrt wird. Das ist ein starkes Stuck.

* Assert-Anweisungen sind ein erster zarter Versuch, in Java auch noch andere Invarianten als die Typinvarianten unterzubringen. Dabei findet die Oberprufung dieser, mittels assert eingebrachten Invarianten im Gegensatz zum Grossteil der Typprufung erst zur Laufzeit statt, indem namlich die entsprechenden Statements ausgefuhrt werden. Dabei beziehen sich die Bedingungen, die die Invarianten formulieren, haufig auf Methoden des Programms, für die invarianten angegeben werden sollen. Da diese Methoden aber auch den Zustand des Programms andern können, kann man einer Zusicherung mit assert nicht ansehen, ob sie seiteneffektfrei ist. Fortschrittlichere Verfahren zur Zusicherung von Invarianten werden nicht als Anweisungen formuliert, sondern als Quellcodeannotationen, und stellen zudem sicher, dass alle Zugriffe auf Programmelemente, die zur Laufzeit notwendig sind, den Zustand des Programms nicht verändern (mehr zu diesem Thema im Kurs 01853 sowie in Abschnitt 52.6 von Kurseinheit 5).

## 39 Module

Ein **Modul** ist eine Einheit von Programmelementen, die (bzw. deren Funktion) von aussen (also z. B. von anderen Modulen) nur über die _Schnittstelle des Moduls_ zuganglich sind. Damit behalt ein Modul einen Teil seiner Implementation für sich -- es hutet quasi ein _Implementationsgeheimnis_. Der Teil, den es (über seine Schnittstelle) nach außen tragt, gilt gemeinhin als offentlich. Die _,Offentlichkeit" kann dabei durchaus beschrankt sein (s. dazu auch Abschnitt 52.2 in Kurseinheit 5).

Ein wesentlicher Grund, zwischen offentlichen und nicht offentlichen -- privaten -- Teilen eines Moduls zu unterscheiden, ist, dass die Programmierinnen eines Moduls Hoheit darb berhalten wollen, wie sie das Modul programmieren. Indem sie sich auf eine Schnittstelle festlegen und alles andere hinter der Schnittstelle verbergen, ist es ihnen moglich, jederzeit die verborgenen Teile zu andern, ohne dass irgendeine andere davon in Kenntnis gesetzt werden muss -- weil die privaten Teile von aussen unsichtbar sind, hangt auch niemand davon ab, und insofern ist auch niemand davon betroffen, wenn an einem Modul eine Anderung durchgefuhrt wird, die die Schnittstellen unberuhrt lasst.

In Java wurden bis Version 8 Module durch Klassen und Pakete (engl. packages) mehr oder weniger gut simuliert. Mit Java 9 wurde schliesslich -- nach langer Vorbereitungszeit -- ein Modulbegriff eingefuhrt, der diesen auch Namen verdient.

### Klassen und Pakete als Module

Klassen haben in Java mehrere Funktionen: Neben der offensichtlichen, der Vorlage für die Erzeugung von Objekten, liefern sie auch noch Typen eines Programms und dienen der Modulariserung.

Pakete hingegen dienen der Sammlung von Klassen und sind zugleich Namensraume für sie (keine zwei Klassen innerhalb eines Pakets durfen gleich heissen). Ausserdem gelten für Klassen innerhalb eine Pakets laxere gegenseitige Zugriffsbeschrankungen als für Klassen aus verschiedenen Paketen. Zwar können Pakete hierarchisch organisiert sein, aber diese Organisation hat keine Bedeutung. Insbesondere erlauben Pakete keinen privilegeierten Zugriff auf Klassen ihrer Subpakete. Damit Klassen paketübergreifend aufeinander zugereifen können, bedarf es expliziter Import-Deklarationen unter Nennung der jeweiligen Paketnamen.

Die Zugereifbarkeit von Klassen oder Typen und den Elementen ihrer Definition (den Membern) wird in Java durch sog. Zugriffsmodifikatoren (engl. access modifiers) eingeschrankt.64 Es sind dies private, protected, public sowie das sog. Package local, für das es kein Schlussewort gibt und das in Klassen bei Fehlen eines der drei anderen angenommen wird (bei Interfaces wird public angenommen). Innerhalb der Klasse selbst sind alle Elemente seiner Definition zugereifbar, innerhalb ihrer Subklassen die, die public oder protected deklariert wurden, innerhalb der Klassen desselben Pakets alle, die public, protected oder ohne Zugriffsmodifikator deklariert wurden, und in anderen Paketen nur noch die, die public deklariert wurden. Faktisch werden Typdefinitionen somit relativ: Was ein Typ anbietet, hangt nicht nur vom Typ selbst ab, sondern auch davon, wo er verwendet wird. Konzeptionell hat die mit einem Typ gemeinsam deklarierte Zugriffsbeschrankung jedoch nichts mit dem Typ z tun, sondern ist vielmehr die _Schnittstellenspezifikation eines Moduls_, wobei das Modul die Klasse ist.

Footnote 64: Die Zugereifbarkeit in Java wird oft, und dabei irrümlich, auch als _Sichtbarkeit_ (visibility) bezeichnet. Sichtbarkeit bezieht sich in Java aber auf lekalkische Scopes; sie wird durch Hiding, Shadowing und Obscuring eingeschrankt (und kann dann bisweilen über Qualifizierer wiederhergestellt werden).

Auf die Bedeutung von Klassen als Module gehen ich in Kapitel 59 von Kurseinheit 6 noch genauer ein. Hier schauen wir uns noch kurz die konkreten Auswirkungen der Zugereifbarkeitsbeschrankungen an:

```
1012packagea;
1013publicclassA{
1014publicinti;
1015protectedintj;
1016intk;
1017privateintl;
1018publicintm(){_}
1019protectedintn(){_}
1020into(){_}
1021privateintp(){_}
1022}
1023packagea;
1024publicclassB{}
1025packagea.a;
1026publicclassC{}
1027packagea.a;1028 public class D extends A {}

Auf einer per A a deklarierten Variable sind abhangig davon, innerhalb welcher Klasse die Deklaration steht, die folgenden Elemente zugreifbar (ergeben die folgenden Ausdrucke keine Typfehler):

* in Klasse A selbst: alle
* in Klasse B: **a.i**, **a.j**, **a.k**, **a.m()**, **a.n()** und **a.o()
* in Klasse C: **a.i** und **a.m()
* in Klasse D: **a.i**, **a.j**, **a.m()** und **a.n()

Die Verquickung von Typ und Zugriffsbeschrankung (Schnittstelle) ist etabliert und kommt auch in anderen Sprachen vor (Z. B. Eiffel, C# und C++). Sie hat den Vorteil der sprachlichen Knappheit (Typ- und Schnittstellendeklaration in einem) und den Nachteil, dass die Zugriffbeschrankung kungen nur sehr grob eingestellt werden können -- insbesondere ist es nicht moglich, dass sich zwei (inhaltlich eng zusammengehrende) Klassen gegenseitig einen freieren Zugriff gestatten als allen anderen, es sei denn, man packt diese beiden in ein Paket.65 AusBedem hat sie den Nachteil, dass zwei unterschiedliche Konzepte der Programmierung zusammen-geworfen und dadurch von Programmierrinnen u. U. nicht mehr als unterschiedlich wahrgenommen werden. Java-Compiler unterscheiden aber immerhin zwischen Typfehlern und Zugriffsfehlern (Z. B.,,is undefined" vs.,,is not visible" in Eclipse, wobei letzteres freilich,,is not accessible" hatte heissen mussen).

Footnote 65: Benötigt wird der freiere Zugriff auch bei der Realisierung sog. _Multi-Methoden_ (Methoden, deren Aufruf auf mehr als nur dem Empfängerobjekt gedispatcht wird; vgl. dazu auch Abschnitt 12.3 in Kurseinheit 1).

### Abhangigkeiten zwischen Modulen

Die Aufteilung eines Programms auf Module dient vor allem dem Zweck der unabhangigen Entwicklung der Programmteile. Damit dies erreicht wird, muss die Abhangigkeit der Module moglichst gering ausfallen. Dabei bedeutet Abhangigkeit in der Regel Anderungsbhangigkeit: Wenn sich in einem Teil etwas andert, muss sich auch im davon abhangigen Teil etwas andern. Sie ergibt sich regelmassig aus einer Benutzt-Beziehung; in der objektorientierten Programmierung kommt jedoch noch die **Verebrungsbhangigkeit** hinzu. Module, die vollkommen unabhangig voneinander sind, sind ein Indikator dafur, dass man nicht ein Programm entwickelt, sondern mehrere -- wo keine Abhangigkeiten bestehen, da gibt es auch kein Zusammenspiel.

Abhangigkeit ist eine gerichtete Beziehung: Dass A von B abhangt heilst nicht, dass auch B von A abhangt. Und so manifesteren sich auch in den

**Manifestation der Abhangigkeit**

**zwischen Modulen**Klassen als Modulen der Java-Programmierung die zwei Richtungen von Abhangigkeit in zwei verschiedenen Formen:

1. Dass eine Klasse von (der Schnittstelle) einer anderen abhangt, erkannt man an der Tatsache, dass auf Objekte der anderen Klasse zugegriffen wird, was man wiederrum daran erkennt, dass Variablen des dazugehorigen Typs deklariert werden sowie, soweit sich die andere Klasse in einem anderen Paket befindet, die Klasse oder gleich das ganze Paket importiert wird.
2. Dass eine Klasse manche Teile ihrer Member anderen zur Benutzung anbietet und diese damit von ihr abhangig werden können, erkannt man an der Verwendung von anderen Zugriffsmodifikatoren als **private** sowie an der Implementierung von Interfaces.

In Java sind zirkulare Abhangigkeiten zunächst erlaubt. Insbesondere durfen sich zwei Klassen (genauer: _Compilation units_) wechselseitig importieren. In der Softwareentwicklung ist dies jedoch verpont, schon weil durch eine wechselseitige Abhangigkeit eine enge Kopplung dokumentiert wird, die zwischen Modulen grundsatzlich nicht bestehen sollte. für Java-Module (s. u.) sind zirkulare Abhangigkeiten denn auch verboten. Wenn Sie einmal in die Verlegenheit kommen sollten, selbst Java-Module zu definieren, werden Sie feststellen, dass dieses Verbot eine sehr sorgfaltige Planung der Modulariserung erzwingt (was für sich genommen schon einen Wert darstellt).

Verebrungsbhangigkeiten zwischen Klassen, die in Java durch Verwendung des Zugriffsmodifikators **protected** und der Annotation **@Override** zumindest angedeutet werden (mehr dazu in Kurseinheit 6, Kapitel 55), sind naturgemas nicht zirkular, bei der Aufweitung der Abhangigkeit von Klassen auf Pakete können jedoch auch zirkulare Abhangigkeiten entstehen.

### Die Module von Java 9

Als Java entworfen wurde, ging man wohl davon aus, dass ein Programm aus mehreren Klassen besteht, die alle zu einem Paket zusammengefasst werden können. Die Klassen eines Programms gewahren sich somit unteerinander privilegierten Zugriff (alles, was nicht **private** deklariert ist, ist zugerifbar), nach auBen sind jedoch nur **public** deklarierte Programmelemente sichtbar.

Dieser Ansatz funktioniert jedoch in dem Moment nicht mehr, in dem Programme auf mehrere Pakete aufgeteilt werden. Wenn zwischen den Paketen namlich Abhangigkeiten bestehen (was, wenn die Pakete zusammen _ein_ Programm reprasentieren, naturgemas der Fallist), dann sind hierfur public Deklarationen erforderlich, die die so deklarierten Programmelemente jedoch für alle gleichermaßen sichtbar machen.66 Ein Programm kann also keine andere (eingeschranktere) offentliche Schnittstelle haben als die Summe seiner Pakete.

Diese unbefriedigende Situation wurde von der Java-Community aufgegriffen, die mit der _Open Services Gateway Initiative_ (_OSG_) einen Standard etablierte, der die Zusammenfassung von Java-Paketen zu Modulen mit einer eigenen Schnittstellenspezifikation erlaubte. Dieser Standard ist u. a. Grundlage von Eclipse, das nicht nur eine Java-IDE, sondern im Kern ein Framework für die Entwicklung beliebig komplexer Java-Programme (sog. Rich Clients) ist.

Mit Java 9 wurde dann Java ein eigenes, über Klassen und Paketen stehendes Modulkonzept verpasst. Ein Modul ist demnach eine Menge von Paketen, die, über eine Moduldeklaration, eine gemeinsame Schnittstelle spezifizieren. Eine Moduldeklaration besteht aus einem (eindeutigen) Namen des Moduls, einer Deklaration der angebotenen Schnittstelle (bislang über **public** Deklarationen hergestellt) und einer Deklaration der benotigten Schnittstelle (bislang ausschliesslich über **import** Direktiven deklariert). Neben den allgemeinen Export tritt der sog. qualifizierte Export, wie er auch in Effrel vorgesehen ist: Er nennt die Module, an die exportiert wird, namentlich und erlaubt so einen,,privaten" Austausch zwischen bestimmten Modulen (die somit ihre eigenen, oder privaten, Schnittstellen haben).

Das besondere an der Moduldefinition von Java ist, dass die Einhaltung der damit einhergehenden Schnittstellenspezifikationen sowohl zur übersetzungszeit als auch zur Laufzeit erzwungen wird. Außerdem kontrolliert sie auch den _reflexktiven Zugriff_ auf Programmelemente, der bislang gar nicht unterbunden werden konnte. Java-Programme werden dadurch erhellich sicherer.

## 40 Interfaces

Modul und Interface sind eigentlich ein Begriffspaar -- das eine lasst sich nur mithlife des anderen definieren. Die Interfaces in Java sind jedoch durchaus eigenstandige Konstrukte, die inzwischen weit über die eigentliche Bedeutung des Begriffs, namlich eine Schnittstelle zu definieren, hinausgehen. Auch wenn Javas Interfaces Vorganger haben, betrachte ich sie doch als einen von Javas wichtigsten Beitragen für die Entwicklung objektorientierter Programmiersprachen.

[MISSING_PAGE_FAIL:237]

aneinandergehanglt); zugleich ist die Angabe der implementierten Interfaces eine _nominale Typkonformitatsdeklaration_, d. h., Instanzen der Klasse sind mit allen Variablen jedes der genannten Interfaces zuweisungskompatibel. Es definieren also die Interfaces von Java genau wie Klassen Typen und können daher genauso wie Klassen in Variablendeklarationen verwendet werden:

1034 <<Interfacename> <<Variablenname>

ist eine solche Deklaration. Der Type checker garantiert dann, dass auf der Variable mit Namen,,Variablenname" nur die Methoden aufgerufen werden können, die im Interface mit Namen,,Interfacename" deklariert sind, selbst wenn das Objekt, das die Variable benennt, mehr anbietet. So ist es moglich, dass Methoden und Felder einer Instanz vor anderen Instanzen anderer oder derselben Klasse verborgen werden können: Man deklariert einfach die Variablen, die auf die Instanz verweisen, mit dem Interface als Typ. Eine genauere Betrachtung der Bedeutung der Verwendung von Interfaces erfolgt in Kapitel 45. Es kann also eine Klasse in Java zwar nur direkte Subklasse genau einer <<Interfaceverbung" anderen Klasse sein, daftur aber mehrere Interfaces gleichzeitig implementieren. Diese mogliche,,Mehrfachimplementierung" von Interfaces wurde haufig als Ersatz für die in Java fehlende Moglichkeit der Mehrfachwerebung angepreisen -- das aber war Unsinn, denn bei der Implementierung eines Interfaces wurde nichts verebt (sieht man mal von der sog. _Interfacevererbung_ ab, die aber auch keine wirkliche Vererbung ist, denn auch die Deklarationen werden nicht automatisch von einem Interface auf seine implementierenden Klassen übertragen, sondern mussen dort wiederholt werden). Vielmehr hat man es mit einer Art Mehrfach-Subtyping zu tun, das aber auch ganz nett ist, wie die überlegungen in Kapitel 45 zeigen werden.

### Interfaces als abstrakte Klassen

Wenn ich im vorangegangenen Absatz das Prateritum bemuht habe, dann liegt das daran, dass Interfaces in Java seit Version 8 einen Bedeutungswandel erfahren haben. Der ursprungliche Anlass hierfur ergibt sich aus der Evolution von Software, genauer aus der Erweiterung von Interfaces im Laufe der Zeit um zusatzliche Methoden und der Tatsache, dass solche Erweiterungen ein Nachfuhren der Klassen, die die Interfaces implementieren, zwin-gend erfordern. Insbesondere bei sog. Black-box-Frameworks, deren Interfaces dazu gedacht sind, von Anwendungsklassen implementiert zu werden, deren Entwicklung in den Handen Dritter liegt, ist dies ein erhebliches Problem. Dasselbe Problem hatte man nicht, wenn man statt der Interfaces abstrakte Klassen nehmen wurde -- dann konnte man nimlich die zusatzlichen Methoden mit einer Default-Implementierung versehen, die von den,,implementierenden" Klassen geerbt wurde, sofern diese Klassen keine eigenen Implementierungen angeben.

Genau das wurde in Java 8 auch für Interfaces eingefuhrt: Ein Interface

**Default-Methoden**

kann die Implementierung einer Methode vorgeben, die dann an implementierende Klassen (oder per **extends** abgeleitete Interfaces) werrebt wird. Dafur hat Java ein neues Schlusselwort spendiert bekommen: **default**. Allerdings haben Interfaces immer noch keine Instanzvariablen und entsprechend können **Default-Methoden** allenfalls auf abstrakte _Getfer und **Setter_ zugereifen.

Mit Java 9 schliesslich wurde -- letztlich nur konsequent -- erlaubt, in

**private Methoden**

Interfaces auch private Methoden zu definieren. Da diese ausschliesslich aus dem Interface selbst heraus zugereifbar sind, dienen sie ausschliesslich der Verbesserung der Lesbarkeit von Default-Methoden, indem man zusammenhangende Teile aus ihnen herauslost und in private Methoden verlegt.

## 41 Arrays

In Java ist es moglich, sowohl von primitiven (Wert-)Typen als auch von Referenztypen Arrays zu bilden. Anders als z. B. in Pascal können aber über den Array-Typkonstruktor keine neuen Typen benannt werden; die Typkonstruktion erfolgt immer implizit in einer Variablendeklaration.

```
1035float[]f;
1036Object[]o;
```

vereinbart in Java zwei Variablen, wovon die erste ein Array von FlieBKommazahlen zum Typ hat und die zweite ein Array von Objekten. Die alternative Schreibweise

```
1037floatf[];
1038Objecto[];
```

ist auch gebrauchlich. Anders als z. B. in Pascal wird die Grosse des Arrays in der Deklaration nicht festgelegt -- dies geschieht erst bei der Initialisierung.

In Java ist es moglich, Arrays bei ihrer Deklaration zu initialisieren:

```
1039floatf[]=(1.0,3.142);
```

Man beachte die Annlichkeit zu literalen Arrays Smalltalks (Abschnitt 1.2); allerdings mussen die Elemente der Arrays in Java nicht selbst Literale sein, sondem durfen auch andere Ausdrucke sein. Die Grosse des Arrays (in diesem Fall 2) wird bei der Initialisierung automatisch mit festgelegt; ansonsten muss dies bei der Erzeugung des Arrays mittels eines Konstruktors explizit geschehen:

```
1040Object[]o=newObject[2];
```Alle Elemente des Arrays enthalten danach jedoch **null** (Javas aquivalent von SMALITALS nil). Java-Arrays sind überigens 0-basiert, was sowiel heilst wie dass das erste Element den Index 0 hat. (Zur Erinnerung: In SMALITALS hat es den Index 1.)

Array-Initialisierer können auch geschachtelt werden und somit mehrere Dimensionen umfassen:

1641 **int integers[][]** = ( (1, 2), null, (238) )

beispielsweise liefert einen moglichen Anfangswert für ein zweidimensionales Array mit der Deklaration int integers[][] (also ein Array mit Elementtyp int und mit zwei Dimensionen). Wie man sieht, mussen die Grossen der zweiten und aller weiteren Dimensionen nicht für jedes Element der ersten Dimension gleich viele Elemente enthalten (sg. Ragged oder Jagged arrays sind moglich; tatsachlich handelt es sich bei mehrdimensionalen Arrays in Java auch gar nicht um mehrdimensionale Arrays, sondern um Arrays von Arrays).

Interessanterweise haben in Java Array-Variablen immer und unabhangig

**Referenzsemantik** vom Basistyp _Referenzsemantik_. Bei der Zuweisung an die Variable **f** von Array-Variablen ** von Array-Variablen** oben wird also nicht ein ganzes Array als Kopie übergeben, sondern lediglich ein Pointer darauf. Dies hat vermutlich den Hintergrund, dass Array-Kopieroperationen sehr teuer sind und zudem selten benotigt werden. Warum auch immer, im Ergebnis kann **f** an eine Variable vom Typ **Object** zugewiesen werden. Eine Zuweisung von **f** an eine Variable vom Typ **Object[]** ist hingegen nicht zulasig **- float[]** ist kein Subtyp von **Object[]** und somit auch nicht damit zuweisungskompatibel. Man beachte überigens, dass Arrays, selbst wenn sie wie Klassen und Interfaces Typen bilden, die automatisch Subtypen von **Object** sind, außer ihrem Basistyp (also beispielsweise float oder **Object**) keine weiteren Definitions-elemente anzugeben erlauben; insbesondere kann man für einen Array-Typen keine weiteren Eigenschaften (Felder oder Methoden) definieren. Allerdings ist für jedes Array die (Pseudo-)Variable **length** definiert, deren Inhalt die Grosse des Arrays (Anzahl Elemente) angibt. Außerdem wird die Methode clone() aus **Object** so überschrieben, dass sie ein Objekt gleichen Typs, also ebenfalls ein Array des Basistyps, zuruckgibt.

Die bemerkte mangelnde Zuweisungskompatibilitat von **Object[]** und **Float[]** wirft naturlich sofort die Frage auf, ob denn auch die Zuweisung einer Variable vom Typ **A[]**, wobei A ein Referenztyp sei und damit automatisch ein Subtyp von **Object**, an eine Variable vom Typ **Object[]** unzulassig ist. Wir hatten ja in Abschnitt 29.3 von Kurseinheit 3 am Beispiel zweier Instanzen eines parametrischen Typs benerkt, dass dies zu einem nicht ganz offensichtlichen Problem fuhrt, dass sich analog auf Arrays übertragen lasst. Die **Oberraschung folgt hier auf den Fuss**: Die Zuweisung ist in Java zulassig.

Am besten lasst sich dies an einem Beispiel erlautern. Man kann tatsachlich in Java bei Vorliegen der Deklarationen

1642 **class Hund extends Tier {}**
1643 **Tier[]** tiere:1844Hund[1]hunde; die Zuweisung

1845tiere=hunde

durchfuhren. Die anschlie8ende Zuweisung

1846tiere[1]=newTier()

fuhrtdann in Java allerdings prompt zu einem _Laufzeittypfehler_ (eine sog.

_Array store exception_), denntiere ist ja lediglich ein _Alias_ auf ein Array

mit Hunden, so dass die Zuweisung ein Tier anstelle eines Hundes an Arrayposition 1 setzt und das Array hunde, das ja per Deklaration nur Hunde zu enthalten verspricht, damit nicht mehr typkorrekt ist. Wurde man die Zuweisung aus Zeile 1046 zulassen, dann wurde in der Folge die scheinbar korrekte Zuweisung

1847Hundhund=hunde[1]

bei der hund ein Tier (das aus Zeile 1046) zugewiesen wird, die Typinvariante von hund verletzen, was ein Compiler aber beim besten Willen nicht mehr erkennen kann (und eine Programmiererin ubrigens auch kaum).

Warum aber geht man dieses Risiko ein und übertragt die Zuweisungskompatibilitat von Typen auf Arrays von diesen Typen? zunächst einmal

**Kompromiss**

kann man festhalten, dass hier auf die Moglichkeit der _statischen Typprufung_, die (auf Basis mangelnder Typkonformitat) einen Typfehler bei der Zuweisung aus Zeile 1045 gemeldet hatte, zugunsten einer _dynamischen Typprufung_ mit moglicher Meldung eines Laufzeitfehlers verzichtet wurde. Dies tut man immer dann, wenn die statische Typprufung Programme verhindert, die man gern schreiben mochte und die auch korrekt sein können, ohne dass dies jedoch vom Compiler garantiert werden konnte. Es ist namlich gar nicht gesagt, dass die Zuweisung der Zeile 1045 immer zu einem Laufzeitfehler fuhrt -- nur wenn man anschlie8end schreibend (wie in Zeile 1046) auf das Array zugereift und dann noch mit dem falschen Typ, kommt es zu einem solchen Fehler (zu typunkorrekten Variablenbelegungen). Da man diese Bedingung aber schlecht zur übersetzungszeit abprufen kann, wird eben ein Laufzeittest durchgefuhrt. Ein klassischer Kompromiss, der diesmal zugunsten der Flexibilitat beim Programmieren augging.

Warum aber will man Zuweisungskompatibilitat zwischen Arrays nicht

gleichen Typs und damit Zuweisungen wie die in Zeile 1045 unbedingt

haben? Die Antwort ist einfach: weil es Prozeduren gibt, die den (statischen) Typ der Array-Elemente nicht genau festlegen, sondern lediglich nach oben beschranken wollen. So gibt es beispielsweise in Java den Interfacetyp Comparable, der wie folgt definiert ist:

1848interfaceComparable{

1849intcompareTo(Objecto):Die Methode compareTo soll dabei einen Wert zuruckgeben, der angibt, wie der Vergleich des Empfanger- mit dem Parameterobjekt ausgegangen ist. Eine Methode mit der Signatur sort(Comparable[]) kann dann Arrays beliebiger Elementtypen zum Sortieren annehmen, solange diese nur Comparable implementieren und damit Auskunft über ihre relative Ordnung zu geben in der Lage sind. Da beim Sortieren die Elemente eines Arrays nicht ersetzt, sondern nur umgeordnet werden, kann dabei auch kein Typfehler von der Art der Zeile 1046 auftreten. Diese Methode sort ist also faktisch sicher -- ein konservatiweres statisches Typsystem hatte ihre Verwendung jedoch nicht zugelassen. Der eingegangene Kompromiss zwischen statischer und dynamischer Typprufung ist also durchaus vertretbar.

## 42 Aufzahlungstypen

Bis Java 1.4 waren class, interface und [ ] (Array) die einzigen Typkonstruktoren; mit Java 1.5 ist auch noch enum für Aufzahlungstypen hinzugekommen, wobei diese unter die Klassentypen fallen: Neben der Angabe der Elemente der Aufzahlung kann man auch noch Felder und Methoden angeben, die auf ihnen definiert sind. Damit werden die Elemente einer Aufzahlung gewissermanen zu konstanten, also zu lebenslang gultigen, Namen für Objekte einer Klasse, die den Aufzahlungstyp reprasentiert.

## 43 Generische Typen

Analog zu der Einfuhrung von parametrisierten Typen in Kapitel 29 von Kurseinheit 3 abstrahieren die generischen Typen Javas von Typen, indem sie die Referenzierung eines oder mehrerer Typen innerhalb einer Typdefinition durch Typvariablen zu ersetzen erlauben. Anders als in Strongtalk stehen die Typvariablen in Java jedoch nicht in eckigen, sondern in spitzen Klammern. Da es dadurch zu Verwechselungen mit metasyntaktischen Variablen kommen kann, werden wir in diesem Kapitel keine mehr verwenden.

### **Einfache parametrische Typdefinitionen**

So, wie auch unparametrisierte (nicht generische) Typen in Java nicht aus eigenstandigen Typdefinitionen hervorgehen, sondern mit der Definition einer Klasse oder eines Interfaces einhergehen, so werden auch parametrische (generische) Typen nicht separat definiert, sondern sind das Produkt parametrischer Klassen- bzw. Interfacedefinitionen. Da aber die formalen Typparameter einer Klassen- bzw. Interfacedefinition durch verschiedene Typen ersetzt werden können, wird die alte 1:1-Beziehung zwischen Klassen und Typen aufgebrochen: Jede Klasse, deren Definition einen Typparameter enthalt, steht tatsachlich für eineganze Menge von Typen, namlich einen pro moglicher Belegung des Typparameters. Insbesondere fuhrt die _Instanziierung"68 einer parametrisch definierten Klasse mit einem tatsachlichen Typparameter nur zu einem neuen Typ, aber nicht zu einer neuen Klasse. Deswegen sind auch die Klassenvariablen und -methoden einer parametrischen Klasse für alle Instanzen ihrer generierten Typen gleich; Instanziarablen und -methoden können dagegen den Typparameter als Typ verwenden und sich insofern unterscheiden.

Die klassische Anwendung generischer Typen findet man bei Collections:

Genauso, wie man in Java Arrays über einen bestimmten Elementtyp bilden kann, will man auch andere Arten von Collections über Elementtypen haben. Zu diesem Zweck verfugt Java nhnlich wie Smalltalk über eine ganze Reihe von Collection-Klassen wie z. B. Sets (fur Mengen) oder Maps (die Java-Variante von SmalltalkS Dictionaries). Nun sind diese Collections (anders als Arrays) nicht Bestandteil der Sprachdefinition Javas, sondern Elemente einer Bibliothek, also in der Sprache selbst programmierte, für die allgemeine Verwendung gedachte Klassen. Da es vor Java 5 keine Moglichkeit gab, bei der Deklaration einer Variable mit einer Collection als Typ anzugeben, welchen Typ die Elemente der Collection haben sollen, wurde implizit davon ausgegangen, dass diese vom Typ Object sind. So hatte z. B. die Klasse ArrayList ein (privates) Feld elementData vom Typ Object[ ], in dem die Elemente gespeichert wurden. Da Object Supertyp aller Referenztypen in Java ist, konnten auch Instanzen aller Referenztypen in elementData und somit in Instanzen von ArrayList gespeichert werden.

Dank der generischen Typen ist es aber moglich, bei der Deklaration einer Variable vom Typ einer Collection -- in Analogie zur Deklaration einer Variable vom Typ eines Arrays über einen Elementtyp -- den Elementtyp mit anzugeben. Um beispielsweise eine Liste von Integern zu deklarieren und zu initialisieren, muss man lediglich

1651List<Integers>liste=newArrayList<Integers>();schreiben.69 Die Klassendefinition von ArrayList ist dazu wie folgt parametrisiert:

1652publicclassArrayList<E>-{

1653privateE[]elementData;

1654publicEget(intindex){

1655returnelementData[index];

1657}

1658publicvoidadd(Eelement){

68nichtzuverwechseln mit der Instanziierung einer Klasse -- insbesondere wird hier auch kein Typ aus einem Metatyp erzeugt

69Man beachte, dass hier als Typ der Variable ein Interface, namlich List, gewaht wurde und nicht die Klasse ArrayList, von der ihr Inhalt eine Instanz ist. Dies hat den Vorteil, dass die Instanz auch gegen solche anderer Klassen ausgetauscht werden kann, solange diese nur ebenfalls den Typ List implementieren. Sie sollten sich zur Angewohnheit machen, immer den allgemeinsten verfugbaren Typ zu verwenden, solange Sie nicht eine speziellere Filterunktion beabschtigen.

* [106] Dabei ist das in spitzen Klammern stehende E der (formale) Typparameter der Definition von ArrayList. Die bereits in Abschnitt 29.1 erwahnte Konvention, einzelne Grossbuchstaben für Typparameter zu wahlen, wurde auch in Java übernommen, ganz einfach, um Typparameter von Klassen- und Variablennamen im Programmtext besser unterscheiden zu können. So steht E ublicheweise für den Elementtyp von Containern, wie es die Collections sind. Durch die Sprachdefinition erzwungen wird das jedoch nicht. Die Zuweisung von Zeile 1051 ist ubrigens nur gultig, wenn der (parametrisierte) Typ ArrayList<Integer> Subtyp von List<Integer> **Subtyping** parametrischer ist. Dies wird, in Java-Syntax, durch die Deklaration
* [1063]**class ArrayList<E> implements List<E>** (nominales Subtyping) sichergestellt. Man beachte, dass die Variable E hier eine logische Bedingung ausdruckt, namlich die, dass ein bei der Verwendung von ArrayList<E> angegebener tatsachlicher Typparameter auch in die Definition von List<E> eingesetzt werden muss. Der Compiler weiss nun aufgrund der Ersetzung des formalen Parameters E mit dem tatsachlichen Parameter Integer in Zeile 1051, dass die Elemente der Variable liste alle vom Typ Integer sind und dass eine Zuweisung der Form
* [1064]**Integer i = liste.get(1): typkorrekt ist. Um das zu überprufen, muss er namlich nur den Wert des Typparameters in der Deklaration von liste, Integer, in die Variable E der Implementierung von get einsetzen. Er kann dann feststellen, dass der Rockgabetyp des Ausdrucks mit der Variable zuweisungskompatibel ist. Man beachte, dass ohne Typparameter in Zeile 1064 eine _Typumwandlung_ von **Object** auf **Integer** (_Down cast_) notwendig ware, die aber zu einem Laufzeitfehler fuhren kann (s. Abschnitt 44.1). Die Einfuhrung von Generics erhoht hingegen die Typischerheit statisch, also zur übersetzungszeit. Ein fundamentaler Gewinn. Nun wissen Sie ja bereits aus der Schilderung aus Kapitel 41, dass List<Integer> nicht unbedingt ein Subtyp von List<Object> sein sollte, selbst wenn Integer ein Subtyp von Object ist. Und so fuhrt in Java bei generischen Typen anders als bei Arrays schon die Zuweisung
* [1065]**List<Object> objektliste = liste:**(bei Beibehaltung obiger Deklaration von liste) zu einem statischen Typfehler, der schon wahrend der übersetzung gemeldet wird Man hat den oben diskutierten Kompromiss offenbar nicht weiter fortfuhren wollen.

### Parametrische Typen und Subtping: Wildcards

Nun ist es aber für generische Typen genau wie für Arrays durchaus sinnvoll, eine liberalere Form von Zuweisungskompatibilitat zuzulassen, z. B. um Objekte verschiedener Instanzen70 eines parametrisierten Typs bei einem Methodenaufruf demselben formalen Parameter zuweisen. S mochte man eben auch für generische Collections eine Methode sort mit einem Parameter, der eine zu sortierende Liste o. a. enthalten soll, definieren und diese dann mit Objekten verschiedener Instanzen von ArrayList<E> (wie in Zeile 1052 ff. definiert) aufrufen können, also z. B. mit Objekten vom ArrayList<Integer> und ArrayList<String>. Intuitiv mochte man dazu zunächst

Footnote 70: s. Füßnote 68

Footnote 71: Man beachte, dass die Varianz bei der Verwendung des generischen Typs bei seiner Benutzung in einer (anderen) Deklaration hergestellt wird. Man nennt dies daher auch _Use-site variance_, im Gegensatz zur _Declaration-site variance_, wie man sie beispielsweise in C# vorfindert (s. Abschnitt 50.4.3 in Kurseinheit 5).

#### Parametrische Typen und Subtping: Wildcards

Nun ist es aber für generische Typen genau wie für Arrays durchaus sinnvoll, eine liberalere Form von Zuweisungskompatibilitat zuzulassen, z. B. um Objekte verschiedener Instanzen70 eines parametrisierten Typs bei einem Methodenaufruf demselben formalen Parameter zuzuweisen. S mochte man eben auch für generische Collections eine Methode sort mit einem Parameter, der eine zu sortierende Liste o. a. enthalten soll, definieren und diese dann mit Objekten verschiedener Instanzen von ArrayList<E> (wie in Zeile 1052 ff. definiert) aufrufen können, also z. B. mit Objekten vom ArrayList<Integer> und ArrayList<String>. Intuitiv mochte man dazu zunächst

Footnote 70: s. Füßnote 68

1066voidsort(ArrayList<Comparable>liste)(-)

schreiben, aber wie wir schon gesehen haben, sind, obwohl **Integer** und String Subtyping von **Comparable** sind, **ArrayList<Integer>** und **ArrayList<String>** nicht zuweisungskompatibel mit **ArrayList<Comparable>**.

Was also tun? In Java hat man dafur das Konzept der Typ-Wildcards (zu deutsch vielleicht Typ-Joker oder -Platzhalter) eingefuhrt, die bei der Instanziierung eines generischen Typs den Platz des tatsachlichen Typparameters einnehmen können und dort zunächst für einen beliebigen Typ stehen. Das Symbol für das Typ-Wildcard ist das Fragereichen: List<?> ist also ein Typ, mit dem Variablen (inkl. formale Parameter) deklariert werden können. Per Definition ist dieser Typ, List<?>, Supertyp aller Instanziierungen von List<T> -- List<Integer> beispielsweise und List<String> sind mit List<?> zuweisungskompatibel. Man beachte, dass bei einer Deklaration und anschlies@enden Zuweisung

1067List7>liste=newArrayList<Integer>**.

1068liste=newArrayList<String>**.

ist also moglich.71List<?> ist genau ein Typ; das fragzeichen selbst ist jedoch keiner (und **Wildcard-Typen** ist auch keine Typvariable). Mit Typ-Wildcards parametrisierte Typen wie List<?> und auch ArrayList<?>, im folgenden **Wildcard-Typen** genannt, sind abstrakt in dem Sinne, dass es keine direkten Instanzen von ihnen gibt:

1069new ArrayList<?>() ist also illegal.

Nun kann man mittels Typ-Wildcards naturlich nicht die oben geschilderten Probleme im Zusammenhang mit dem Aliasing aushebeln. Es ist also insbesondere nicht moglich, nach Deklaration und Zuweisung von Zeile 1067

1070liste_add(2) zu schreiben, da ja nicht sichergestellt werden kann, dass Liste tatsachlich auf ein Objekt vom Typ List<Integer> verweist. Tatsachlich ist die einzige gultige Zuweisung an Elemente von liste die von null. Umgekehrt kann beim Lesen der Elemente aus liste kein anderer Typ als Object angenommen werden, da ja liste Listen mit beliebigem Elemente-typ zugewiesen werden durfen. Das aber ist unbefriedigend.

Nun kennen Sie aus Abschnitt 29.4 bereits das Konzept der Beschrankung von Typparametern. Dies lasst sich auch auf Typ-Wildcards übertragen.

Wenn man also sicherstellen will, dass die Elemente einer Liste eines unbekannten Elementtps mindestens vom Typ Number sind, schreibt man in der Deklaration der entsprechenden Variable, hier wieder liste, einfach

1071liste? extends Numbers=liste; Es sind damit nur noch Zuweisungen von Listenobjekten an liste gestattet, deren Elementtyp den Typ Number oder einen Subtyp davon (z. B. **Integer**) hat:

1072liste = new ArrayList<Integer>(); ist also legal,

1073liste = new ArrayList<objects(); hingegen nicht. Das erlaubt einer lesende Zugriffe der Form

1074Number n = liste_get(1); wobei Number auch durch einen beliebigen Supertyp von Number ersetzt werden durfte, jedoch durch keinen Subtyp. Das Einfugen von Elementen in liste bleibt jedoch weiter nicht gestattet, da nicht bekannt ist, welchen Typs die Elemente mindestens sein mussen.

* [107] überprufen Sie die letzte Aussage, indem Sie versuchen, ein Gegenbeispiel zu finden.

Per **extends** beschrankte Typ-Wildcards erlauben also eine spezielle Art des Subtypings, namlich eine, bei der Zuweisungen von Objekten eines

Subtypings ganz normal an Variablen eines Supertyps erlaubt sind, aber in der Folge schreibende Zugriffe auf Variablen, die mit dem Typparameter als Typ deklariert sind, verboten (lesende Zugriffe sind hingegen erlaubt). Die Situation unterscheidet sich von der bei den Arrays (Kapitel 41) lediglich dadurch, dass die Typprufung statisch, also bereits zur übersetzungszeit durchgefuhrt wird. Es ist damit sichergestellt, dass es niemals zu einem Laufzeitfehler entsprechend der _Array store exception_ kommt; ein entsprechender dynamischer Typtest kann damit entfallen. Wie allgemein ublich werden damit auch Verwendungen ausgeschlossen, die eigentlich legal waren; so ist z. B.

```
1075List<?extendsInteger>liste=newArrayList<Integer>();
1076liste.add(newInteger(1));
```

nicht zulasig, obwohl hier eigentlich kein Problem vorliegt.

Nun kann man sich fragen, ob nicht auch eine umgekehrte, nur schreibenden Zugriff erlaubende Art des Subtyping moglich ist. Die Antwort ist

einfach: ja. Man muss dazu nur die Beschrankung des Typ-Wildcards umkehren und verlangen, dass nur Supertypen der Schranke eingesetzt werden durfen. Da Supertypen mit ihren Subtypen zuweisungskompatibel sind, weiss der Compiler, dass er Elemente jedes beliebigen Subtyps der Schranke zuweisen darf. für eine Deklaration

```
1077Liste?superInteger>liste;
```

beispielsweise, bei der superInteger die untere Schranke für tatsachliche Typparameter

bei einer Zuweisung angibt, ist

```
10781liste=newArrayList<Number>();
```

und in der Folge sogar

```
10791liste.add(1);
```

erlaubt, denn Listen mit Elementtyp Number (oder einem beliebigen anderen Supertyp von Integer) können, aufgrund des Subtypings der Elementtypen, problemlos Integer zugewiesen werden. Der lesende Zugriff auf Elemente von liste hat jedoch immer den Typ Object zum Ergebnis, so dass

```
10881integeri=liste.get(1)bei obiger Deklaration von liste nicht erlaubt ist: Der Elementtyp durfte ja auch ein Superpty von Integer sein, so dass die Zuweisung zu i ungultitig ware. List<? super Integer> ist also spezieller Supertyp von allen Instanzen von List<E>, deren tatsachlicher Typparameter (also der für E eingesetzte Typ) ein Supertyp von Integer ist. Der Supertyp ist speziell, weil zwar eine Zuweisungskompatibilitat gegeben ist, der Zugriff auf die Elementtypen (die mit dem Typparameter typisierten Elemente des Typs) auf schreibenden beschrankt ist.

**Selbsttestaufgabe 43.2**

überlegen Sie, ob es moglich und sinnvoll ist, für einen Typparameter ein Typ-Wildcard mit oberer und unter Schranke anzugeben.

Durch die mogliche Beschrankung von Typ-Wildcards entsteht für jeden

**Subtyping von**

generischen Typ eine (potentiell unendlich große) Menge von Typen, so

**Wildcard-Typen**

dass man sich fragen kann, ob diese Typen in einer bestimmten Subtypbeziehung zueinander stehen. Dies ist tatsachlich der Fall: für mit **extends** nach oben beschrankte Wildcard-Typen gilt, dass wenn die Schranken Subtypen sind, dann auch die Wildcard-Typen Subtypen sind. Wenn also **Integer** ein Subtyp von **Number** ist, dann ist auch List<? extends Integer> ein Subtyp von List<? extends Number>. Umgekehrt gilt für mit super nach unten beschrankte Typen, dass List<? super Integer> ein Supertyp von List<?

**super Number>** ist. Man sagt auch, das Subtyping mit **extends** beschrankter Wildcard-Typen sei **kovariant** (da das Subtyping der Wildcard-Typen sich am Subtyping der Schranken orientiert) und das mit super beschrankter Wildcard-Typen **kontravariant** (aus entsprechendem Grund).

**Selbsttestaufgabe 43.3**

überlegen Sie sich, ob ArrayList<? extends Integer> ein Subtyp von List<? extends Number> ist.

Ein typisches Beispiel für die Verwendung von Wildcard-Typen ist das folgende:

1081 class List<I> {

1082 copyFrom (List<? extends T> andereList) {_}

1083 copyTo (List<? super T> andereListe) {_}

1084 =

1085 }

### Beschrankter parametrischer Polymorphismus in Java

Wie bereits in Kurseinheit 3, Abschnitt 29.4 erwahnt, kauft man sich mit einfachem parametrischem Polymorphismus aüberhalb der Typdefinition Typischerheit zum Preis der mangelnden Typischerheit innerhalb: Solange man keine Aussagen über den konkreten Typ, der für einen Typparameter eingesetzt wird, machen kann, kann man bei der Implementierung einer Klasse, die den parametrischen Typ definiert, auch keine Eigenschaften der Objekte, die von dem (unbekannten) Typ sein sollen, voraussetzen. Was man vielmehr braucht, ist beschrankter parametrischer Polymorphismus. Naturlich gibt es den auch in Java.

Wenn man beispielsweise die parametrische Definition sortierter Listen, SortedList<E>, auf Elementtypen einschranken will, die Subtypen von Comparable sind (damit die in Comparable definierte Methode compareTo(.) zur Verfugung steht), dann schreibt man in JAVA

```
1886interface SortedList<E extends Comparable>{
1887voidinsert(Eelement);
1888voidremove(Eelement);
1889
1990
1991
2001
2010Die moglichen Werte der Typvariable E werden dadurch auf Typen eingeschrankt, die Comparable (direkt oder indirekt) erweitern. Die Implementierung der Methode zum Einfugen und Entfernen von Elementen in sortierten Listen kann also davon ausgehen, dass alle Objekte, die in einer solchen Liste gespeichert sind, die Nachricht compareTo(.) verstehen, die vom Interface Comparable vorgeschrieben wird. Man beachte, dass dadurch keine neue Subtyppenrelation zwischen irgendwelchen Typen hergestellt wird -- es werden lediglich die Moglichkeiten, konkrete Typen (z. B. in Variablendeklarationen) zu bilden, eingeschrankt. Eine Variablendeklaration
```
1991SortedList<String>liste: wobei String ein Subtyp von Comparable ist, ist also moglich, eine wie
1992SortedList<Point>liste: hingegen nicht. Dennoch ist SortedList<String>, wie bereits in Abschnitt 29.3 Demerkt, kein Subtyp von SortedList<Comparable>.

```
1993Selbstestestaufgabe43.4(nurfur Java-Programmiererinnen) Probieren Sie aus, ob zwei Instanzen generischer Typen (also z. B. ArrayList<Object> und ArrayList<String> als Instanzen von ArrayList<E>) in Java zur Laufzeit denselben oder verschiedene Typen haben. Verwenden Sie dazu die Methode getClass() auf Objekten, die Sie von diesen Typen erzeugt haben.

### Rekursiv beschrankter parametrischer Polymorphismus

Wenn Ihnen das noch nicht kompliziert genug ist, geht es noch weiter: Es ist namlich Comparable selbst ein Typ, der von einer Parametrisierbarkeit profitieren wurde. In einem ersten Ansatz wurde man verlangen, dass von zwei vergleichbaren Elementen beide vom selben Typ sein mussen. Dies konnte man durch die Deklaration von

```
1093interfaceComparable<T>{
1094intcompareTo(T o);
1095}
```

(tatsachliche Definition von Comparable in Java) sowie
1096interfaceSortedList< extends Comparable<E>> _

erreichen. Man beachte die Parallelitat zu STRONGtalk (Abschnitt 29.5).

\begin{tabular}{c c}  & **Wildcards in** \\ \end{tabular} \begin{tabular}{c c}  & **Typedefinitionen** \\ \end{tabular} \begin{tabular}{c c}  & **Uplz** \\ \end{tabular} \begin{tabular}{c c}  & **Wildcards in** \\ \end{tabular} \begin{tabular}{c c}  & **Typedefinitionen** \\ \end{tabular} 
\begin{tabular}

### Generische Methoden

Ausser in Typdefinitionen können Typvariablen (formale Typparameter) auch in Methodendefinition eingefuhrt (deklariert) werden. In diesem Fall ist die Sichtbarkeit der Typparameter auf die jeweilige Methode beschrankt.72 Es lassen sich damit variable über- und Ruckgabeparametertypen für eine Methode deklarieren.73 Die Belegung der Typparameter mit konkreten Typen als Werten erfolgt dann bei der Bindung eines Methodenaufrufs zur übersetzungszeit. Der tatsachliche Typparameter muss dabei nicht angegeben werden, wenn er sich aus dem Kontext eindeuttig ergibt (sog. Typinferenz).

So handelt es sich beispielsweise bei der Deklaration

```
1101publicstatic<T>List<T>toList(T|array):
```

wobei T nicht zugleich Typparameter der die Methodedefinition enthaltenden Klasse sein darf, um die Deklaration einer Methode, die ein Array eines beliebigen Typs, hier durch T reprasentiert, in eine Liste mit Elementen desselben Typs konvertiert.

Beim Aufruf einer parametrischen Methode muss der tatsachliche Typparameter angegeben werden. Allerdings erlaubt der Java-Compiler, diesen wegzulassen, wenn er sich aus dem Aufruf erschlieBen lasst (die oben erwahnte Typinferenz). Bei obiger Methodedeklaration ist das z. B. beim Aufruf

```
1102Lists.toList(newInteger[]{1,2,3}):
```

oder

```
1103Lists.toList(new String[]{"abc","def"}):
```

der Fall: Hier wird der Typ Integer beziehungsweise String aus dem Typ des tatsachlichen Parameters abgeleitet. Dies ist jedoch nicht immer moglich; ein Aufruf wie

```
1104Lists.<Integer<toList(new Integer[]{1,2,3}):
```

macht den tatsachlichen Typparameter dann explizit.

```
1105publicstaticList(object[]array):
```

```
1106hat.

Der (formale) Typparameter einer generischen Methode kann zunächst an jeden beliebigen Typ gebunden werden. Genau wie bei generischen Klassen reduziert dies jedoch entweder die Verwendbarkeit oder die Typ- sicherheit der mit dem Parameter übergebenen Objekte, da deren Typ innerhalb der Methode unbekannt ist. Es ist also, wieder genau wie bei generischen Klassen, moglich, den Typparameter mit **extends** zu beschranken.

Nicht selten wird der Typparameter (nicht die mit ihm deklarierten Parameter!) innerhalb der Methode nicht mehr verwendet. Eine Variable, die nur einmal vorkommt, kann man aber auch weg- oder zumindest unbenannt lassen. Und so ist es in diesen Fallen quite Praxis, anstelle des Typparameters ein (entsprechend beschranktes) Typ-Wildcard zu verwenden.

### Generische Variablen

Schliesslich ist es in Java auch noch moglich, Variablen generisch zu deklarieren, also ohne dass die in der Variablendeklaration verwendete Typvariable bereits von einer umschliessenden Methode oder Klasse eingefuhrt worden ware. Allerdings geht das, da eine Variable anders als eine Klasse oder Methoden keinen neuen Sichtbarkeitsbereich definiert, nur mit anonymen Typvariablen, also Wildcards. Man beachte jedoch, dass eine solche Variablen-deklaration, genau wie eine generische Methodedefinition, keinen neuen Typ einfuhrt (s. Fussnote 72); vielmehr handelt es sich mit dem durch ein Typ-Wildcard als tatsachlichem Parameter eingesetzten Typ selbst um einen konkreten Typ. Der per

116 List*> List*:

deklarierten Variable liste können also Listen beliebigen Elementtyps zugewiesen werden, einfach weil List*?> (unter den in Abschnitt 43.2 genannten Einschrankungen) Supertyp aller Instanziiierungen von List*:

## 4 Dynamicsche Typprufung in Java

Wie Sie gesehen haben, hat das Typsystem Javas eine starke statische Komponente. Gleichwohl können nicht alle Typprufungen zur übersetzungszeit durchgefuhrt werden. Wahrend man die dynamischen Typprufungen bei Arrays (Kapitel 41) noch durch die Einfuhrung von Wildcards hatte vermeiden können, gilt das nicht für die gelegentlich notwendigen Typumwandlungen (Type casts; zumindest nicht für alle).

### Type casts

Wie bereits in Kapitel 27 von Kurseinheit 3 erlautert, versteht man unter einem Type cast (einer _Typumwandlung_) den Vorgang, bei dem einem Programmelement ein anderer Typ aufgezwungen wird als der, mit dem es deklariert wurde. Type casts werden also insbesondere auf Variablen und auf Methodenausdrucke angewendet, und zwar immer dann, wenn man diese einer Variable zuweisen will, zu der keine Zuweisungskompatibilitat besteht, oder wenn man darauf eine Methode aufrufen (oder ein Feld zugreifen) will, das der deklarierte Typ nicht anbietet. So fuhrt z. B.

```
1107Objecto=newString("abc");
1108.substring(2,3);
1109Strings=o;
```

zu zwei Typfehlern: einem, weil o vom Typ Object ist, der keine Methode substring kennt, obwohl das Objekt, auf das o verweist, diese Methode sehr wohl kennt, und einem, weil Object nicht zuweisungskompatibel mit String ist. Zwei Type casts losen das Problem:

```
11110((String)o).substring(2,3);
1111Strings=(String)o;
```

Wie schon in Kapitel 27, so unterscheiden wir auch hier in Abhangigkeit davon, wie die betelijten Typen, der Ausgangstyp und der Zietlype eines ```
Type casts, miteinander in Beziehung stehen, drei Arten von Typumwandlungen:

* _Up casts_: der Zietlyp ist ein Supertyp des Ausgangstyps
* _Down casts_: der Zietlyp ist ein Subtyp des Ausgangstyps
* _Cross casts_: Zietlyp und Ausgangstyp stehen in keiner Subtypenbeziehung zueinander, stehen also gewissermassen nebeneinander.

Bei obigem Beispiel handelt es sich um (die bei weitem haufigsten) Down casts.

Wie man sich leicht vor Augen halt, ist ein Up cast auch in Java immer sicher, da jedes Objekt neben seinem Typ zugleich auch den Typ all seiner Supertypen hat (weswegen der Up cast auch immer weggelassen werden kann); Down und Cross casts sind jedoch nur erfolgreich, wenn das Objekt, zu dem der typumgewandlet Ausdruck auswertet, tatsachlich den Zietlyp (oder einen Subtyp davon) hat. Dies kann jedoch zur Obersetzungszeit nicht garantiert werden; Down und Cross casts können daher zu Laufzeittypfehlem (der in Java sog. Class cast exception) fuhren.

Mit der Einfuhrung von Generics ergeben sich ein paar Probleme mit im-
```

Listing Type erasure

pliziten Typumwandlungen. Das nachfolgende Beispiel ist jedoch nur für Interessierte; insbesondere auf sog. _Raw types_ und das damit zusammenhangende Konzept der Type erasure_ wird in diesem Kurs namlich nicht eingegangen.

* [1112]**Class Kiste<T> {**
* [1113]**T inhalt;**
* [1114]**void reintun (T x) {**inhalt = x; }
* [1115]**T rausnehmen () {**return inhalt; }
* [1116]**

**und folgender Variablendeklarationen und Initialisierungen**

* [1117]**Kiste kiste = new Kiste(); // sog. Raw type**
* [1118]**Kiste<Tier> **tierkiste = new Kiste<Tier>():**

**ergeben die Zuweisungen**

* [1119]**Kiste = tierkiste; // geht ohne Warnung**
* [1120]**Kiste.reintun(new Object()); // Warning:**
* [1121]**// Type safety: The method reintun(Object)**
* [1122]**// belongs to the raw type Kiste. References to generic**
* [1123]**// type Kiste<T> should be parameterized**
* [1124]**Tier tier = tierkiste.rausnehmen(); // geht ohne Warnung**,**
* [1125]**// aber ClassCastException!!!!**

**bei der letzten einen Laufzeitfehler vom Typ Class cast exception.**

### Typtests

**Laufzeitfehler der obigen Art vermeidet man in Java mit Hilfe sogenannter Typtests, die man vor einer Typurmwandlung durchfuhrt. Das dazugehorige Schlussewort heilst**

**instanceof:**

* [1126]**if (o instanceof String)**
* [1127]**((String) o).substring(2, 3):**
* [1128]**if (o instanceof String)**
* [1129]**String_s = (String)_o:**

**bilden die typsichere Variante der Typumwandlung. Es bleibt allerdings an der Programmierrin hangen, zu sagen, was passieren soll, wenn der Wert von o nicht den geforderten Typ (hier String) hat.**

## 45 Programmieren mit Interfaces

**Oben hatten wir ja bereits enwahnt, dass eine Klasse neben den in ihrem**

**Interface veroffentlichten noch weitere offentliche (public deklarierte)**

**Methoden haben kann. Daraus folgt, dass unterschiedliche Interfaces einer Klasse unterschiedliche Methodenmengen zur Verfugung stellen können. Da auf einer**

[MISSING_PAGE_FAIL:255]

thoden ausschlieflicht über Interfacetypen zuganglich zu machen (s. Kurseinheit 5, Abschnitt 50.4.2). Seit Java 8 kann man allerdings in Interfaces auch statische Methoden definieren, die neue Instanzen von Klassen, die die Interfaces implementieren, zuruckliefern und somit die Konstruktoren dieser Klassen ersetzen. Man braucht dann keinerlei Zugriff mehr auf die Klassen, die deswegen als _package local_ deklariert und die somit vollstandig hinter dem Interface als Schnittstelle verborgen werden können.

Interfaces dienen aber nicht nur der Beschrankung des Zugriffs wie im

**Interfaces erhohen**

obigen Beispiel -- sie dienen auch der besseren Austauschbarkeit von

Klassen. Und das bringt uns zuruck zum eingangs Kapitel 43 benutzten Beispiel (Zeile 1051 ff.): Dadurch, dass die Variable liste mit dem Typ List (ein Interface) und nicht

**ArrayList** (eine Klasse) deklariert wurde, können ihr auch Instanzen anderer Klassen als

**ArrayList** zugeweisen werden, solange sie nur dasselbe Interface implementieren. Das Interface als Typ der Variable verlangt lediglich, dass alle in ihm versammelten Methoden von den Objekten, auf die die Variable per Typsystem verweisen darf, auch angeboten werden, und das wird dadurch sichergestellt, dass der Typ der rechten Seite aller Zuweisungen zur Variablen konform zum Typ der linken Seite sein muss. Die Zuweisungskompatibilitat ist

**in Java** also an die Typkonformitat gebunden, und zwar an die nominale.

Eine weitere, vergleichsweise haufig verwendete Moglichkeit des Einsat-

**Tagging oder Marker interfaces**

**interfaces**

**Tagging oder Marker interfaces**

**Tagging oder Marker interface hat in der Regel keine eigenen Methodendeklarationen, sondern dient lediglich der Filterung von Variablenwerten.**

1151 **Interface Markiert (\(\backslash\))**

ware ein solches Interface. Da in Java die vom Compiler statisch gepruffe Zuweisungskompatibilitat ja Namenskonformitat verlangt, kann die Typisierung einer Variable mit dem Interface Markiert erzwingen, dass dieser Variable nur Instanzen solcher Klassen zugeweisen werden, die das Interface Markiert zu implementieren deklarieren. Da das Interface aber keine Auflagen macht (keine Methodendeklarationen vorgibt, die von der Klasse mit Definitionen versehen werden mussen), ist die Implementierung des Interfaces für die Klasse zunächst ohne Konsequenzen. Die durch das Interface erfolgte Markierung der Klassen (bzw. deren Instanzen) kann jedoch zur übersetzungszeit vom Compiler (s. o.) und zur Laufzeit durch einen Typtest (s. Abschnitt 44.2) überpruft werden.

Ein konkretes Beispiel für ein Marker interface in Java ist das Interface

**Serializable**, mit dessen Implementierung eine Klasse deklariert, dass

ihe Instanzen serialisiert werden können. Die Serialisierung wird aber nicht von der Klasse selbst vorgenommen, sondern von einer anderen; die Klasse muss also zu ihrer Serialisierung nichts weiter beitragen. Seit Java 5 wurde man allerdings solche Marker-Interfaces eher durch Metadaten (auch _Annotationen_ genannt; s. Abschnitt 47.4) ersetzen, so wie das in C# schon langer gehandhabt wird (s. Abschnitt 50.4 in Kurseinheit 5).

Javas Interface-als-Typ-Konzept ist ziemlich interessant und vielleicht so-

gar der großte einzelne Beitrag Javas zur objektorientietten Programmierung. In der Programmierpraxis scheint es jedoch, sieht man einmal von grossen Frameworks ab, nur langsam anzukommen. Das mag zum einen an der schlechten Verkaufsstrategie liegen (,,Ersatz für Mehrfachvererbung" -- jede Anfangerin merkt nach funf Minuten, dass das nicht stimmt), zum anderen aber auch an der Vergrosserung des Programmuffangs, die der parallelen Definition von Klassen und Interfaces geschuldet ist (die auch den Wartungsaufwand erhohen kann, obwohl ja Interfaces eigentlich die Wartung vereinfachen sollen). für so manche Programmiererin scheinen die Moglichkeiten, die Schnittstelle einer Klasse mittels der Zugriffsmodifikatoren innerhalb der Klasse selbst zu definieren, vollig auszureichen. Der Preis dafur ist eine mangelnde Differenzierbarkeit des Zugriffs nach verschiedenen Klimenten sowie eine (haufig vorschnelle) Festlegung von Variablen auf Instanzen einer Klasse. Mehr zur sog. interfacebasierten Programmierung finden Sie im Kurs 01853.

Kurs

## 46 Interne und externe Iteration über Collections

Genau wie in der SMALLtalk-Programmierung kommt man in der JAVA-Programmierung haufig in die Verlegenheit, :\(n\)-Beziehungen umsetzen zu mussen. Wie in SMALLtalk geschieht dies auch in JAVA mit Hilfe von Zwischenobjekten. Anders als in SMALLtalk wird hier aber zwischen zwei Arten von Zwischenobjekten grundsatzlich unterschieden: den Arrays und den Collections.74 Da JAVA-Arrays in ihrer Funktionalitat beschrankt sind (s. Kapitel 41: keine eigenen Methoden zur Unterstutzung des Zugriffs, kein dynamisches Wachstum, dazu die etwas verkorkste Situation beim Subtyping), werden Arrays vornehmlich dort eingesetzt, wo es um Effizienz (geringer Speicherverbrauch und schneller Zugriff) geht.

Footnote 74: Zur Erinnerung: In SMALLtalk sind Arrays spezielle Collections, mit eigenen Methoden.

### Externe Iteration

Bei :\(n\)-Beziehungen mussen ja haufig mehrere Elemente der gleichen Behandlung unterzogen werden oder es werden aus der Menge der Elemente einige gesucht. Sind die Elemente in einem Array gespeichert, so kann man in JAVA dazu etwas der Form

1152for (int i = 0; i < a.length; i = 1 + 1) (- a[i] -)schreiben. Verwendet man aber Collections, die nicht indiiziert sind (es gibt auch in JAVA so Collections wie B\(\hat{\text{a}}\)ume oder verkettete Listen), ist die obige Form der Iteration nicht einsetbar. Stattdessen gibt es in JAVA die beiden Interfaces Enumeration (total veraltet) und Iterator (etwas neuer), die eine einheitliche Iteration über Collections mittels sog. Iteratoren erlauben. Jede Collection-Klasse, die Iterator implementiert, bietet dazu eine Methode iterator() an, die ein solches Iteratorobjekt ( vom Typ Iterator) zuruckliefert. Mit der Methode next() erhalt man von diesem Objekt zunächst das erste und in der Folge

[MISSING_PAGE_FAIL:258]

Streams sind ein mit Java 8 neu eingefuhrtes Konstrukt, das eine Datenverarbeitung in Pipelines ganz ahnlich wie die Collections in Smalltalk erlaubt: Das Ergebnis einer Operation wie filter oder map, auf einem Stream ausgefuhrt, ist wieder ein Stream, auf dem weitere Operationen dieser Art ausgefuhrt werden können (das _Pipelining_). Das besondere an Streams ist, dass sie keine Datenspeicher wie Collections sind, sondern _interne Iteratoren_: Jeder Stream für sich halt zu einem Zeitpunkt immer genau ein Element einer potentiell unendlichen Folge von Elementen. Dabei dienen Streams entweder abgeschlossene Datenspeicher wie Collections und Files oder offene Datenlieferanten wie die Tastatur oder Datengeneratoren (wie beispielsweise ein Zufallszahlengenerator oder eine Vorschrift zur Berechnung einer Fibonacci-Folge) als Quelle. Ein Ergebnis liefert eine Stream-Pipeline (die auch aus nur einem Element bestehen kann) immer erst durch einen sog. Abschluss, also eine Methode wie reduce oder collect, die ein anderes Ergebnis als einen Stream liefert (eine Collection im Falle von collect).

Das Stream-Framework von Java ermoglicht für viele Pipelines eine besonders effiziente Ausfuhrung. So muss jedes Element einer Datenquelle in der Regel nur einmal angefragt werden und die interne Speicherung von Zwischenergebnissen wird automatisch gering gehalten. Insbesondere wird gegenüber einer naiven Implementierung von Pipelines, die eine Iteration je Element der Pipeline benotigt, in vielen Fallen nur eine Iteration gebraucht (die sog. Stream fusion). Zudem kann durch Wahl des Streams (und nicht der Operationen) bestimmt werden, ob die Verarbeitung der Pipeline parallel oder sequentiell erfolgt. Gleichwohl ist die Performanz von Java-Pipelines nicht leicht vorherzusagen und eine gewinnbrignende Verwendung setzt sicherlich einiges an Erfahrung und Kenntnis der Implementierung voraus.

## 47 Spezielle Klassen

Grundsatzlich sollte eine Klassenbibliothek mit den Mitteln der Sprache programmiert, ansonsten aber von der Sprachdefinition unabhangig und damit austauschbar sein. Dies gilt naturlich genauso für die Prozeduren in imperativen Sprachen: Auch diese sollten nicht Teil der Sprache, sondern lediglich darin geschrieben werden. Nun hat man sich aber schon bei den edelsten imperativen Sprachen nicht daran gehalten (in Pascal beispielsweise sind **read** und **write** Bestandteil der Sprache und der Compiler weiss, dass ihnen -- als einzigen Prozeduren -- beliebigiele Parameter übergeben werden durfen, wobei jeder einzelne Parameter in seinem Typ nicht festgelegt ist); bei den objektorientierten tut man es erst recht nicht. So sind in Java einige Klassen mit der Sprache fest vorgegeben und können nicht beliebig ersetzt werden.

### Object

Die Klasse Object gibt die Eigenschaften vor, die allen Objekten, einschlie@lich Array-Objekten, gemeinsam sind. Darunter sind keine Felder (Instanzvariablen), aber elf Methoden. Es sind dies:

* Object clone() zum Erzeugen von Kopien (vergleichbar SmalltalkS copy)
* boolean equals(Object) zum Test auf Gleichheit anstelle von Identtat (ent-sprechend SMALLTAKIS =)
* String toString(), die eine String-Repräsentation des Objekts zuruckgibt (ent-sprechend SMALLTAKIS printString)
* Class<? extends Object> getClass() mit dem offensichtlichen Zweck (ent-sprechend SMALLTAKIS class)
* int hashcode() für die Speicherung von Objekten in Hash-Tabellen (entsprechend SMALLTAKIS hash)
* void finalize(), die vom Garbage collector aufgerufen wird, wenn das Objekt aus dem Speicher entfrent wird (es können damit externe Ressourcen, die mit dem Objekt verbunden sind, freiggebeen werden, also z. B. Dateien geschlossen)
* void notify() und void notifyAll() zur Benachrichtigung von Threads, die am Monitor des Objekt warten
* void wait() in drei Versionen, um den ausfuhrenden Thread zum Warten zu bringen, entweder bis dem Objekt ein Notify gesendet wird oder ein anderes Ereignis eintritt.

In JAVA ist jeder Typ Subtyp von dem von Object. Das gilt auch für Interfaces. Man beachte aber, dass Interfaces ansonsten nicht von Klassen ableiten können.

### Exception handling

Wie Sie schon bei den Anweisungen in Kapitel 38 gesehen haben, sieht JAVA ein sog. Exception handling vor. Beim Exception handling handelt es sich um eine Moglichkeit, bei der Spezifikation des Kontrollflusses eines Programms zunächst mogliche Ausnahmesituationen und deren Behandlung unberuckschtigt zu lassen und so zu tun, als wurde immer alles gutgehen. Da das normalerweise auch der Fall sein sollte, erlaubt es sowohl der Autorin als auch der Leserin eines Programms, bei seiner hauptsachlichen Funktion zu bleiben, ganz nach dem Motto,,zu den Ausnahmen kommen wir spater!"

Die moglichen Ausnahmesituationen eines Programms werden in Java in

Klassen eingeteilt, deren Instanzen jeweils eine konkrete Ausnahmesituation wahrend des Programmablaufs reprasentieren. Wenn also beispielsweise in einem Programm auf ein Element eines

Arrays zuggeriffen

[MISSING_PAGE_FAIL:261]

Eine Methode, die diese Methode aufruft, muss also den Aufruft entweder mit einer Trycatch-Anweisung klammen, die die geforderte Catch-Klasuel enthalt, oder selbst deklarieren, die Exception zu werfen. Diese Pravis fuhrt zwar zu erheblicher Schreibarbeit, stellt aber letztlich die einzige Moglichkeit dar, zu erzwingen, dass sich die Programmiererinnen der moglichen Ausnahmesituationen, die auftreten können, bewusst sind, ohne die Spezifikation des Kontrollfusses dadurch über Gebuhr zu belasten. Jede, die schon einmal in C die Aufrufe von Betriebsystemroutinen durch Abfrage der Return-Codes abzusichern versucht hat, weiss, wovon ich spreche. Man nennt Exceptions, die ein Abfangen innerhalb einer Methode oder eine Deklaration im Methodenkopf verlangen, **Checked exceptions**.

Nun gibt es aber Exceptions, die so gut wie überall auftreten können. Das prominenteste Beispiel ist vielleicht die Out of memory exception, die auftritt, wenn eine Speicheranforde- rung des Programms von der JVM nicht bedient werden kann. In der Pravis haufiger, wenn auch durch das Programm selbst vermeibbar, ist die Null pointer exception, die immer auftritt, wenn ein Ausdruck, auf dem ein Feld oder eine Methode zugegriffen werden soll, zu null ausgewertet wird (vgl. Selbsttestaufgabe 11.1). In dieselbe Kategorie fallt auch die Array index out of bounds exception, die sich naturlich durch vorsichtige Programmierung vermeiden liese, die aber in der Pravis trotzdem immer wieder vorkommt. In all diesen Fallen ware es ausserordentlich muhsam, wenn man alle Anweisungen, bei denen die jeweilige Exception auftreten konnte, mit einer entsprechenden Try-catch-Anweisung absichern musste.

Deswegen gibt es in Java Exceptions, bei denen das nicht notig ist, die sogenannten **Unchecked exceptions**. Man konnte meinen, dass ob eine

Exception checked oder unchecked ist, von Fall zu Fall (von Auftreten zu Auftreten) von der Programmiererin, die sie wirft, zu unterscheiden ware -- dies ist aber nicht so. Stattdessen sind alle Exceptions, die von der Klasse **RuntimeException** abgeleittet sind, per Definition unchecked. **RuntimeException** ist selbst Subklasse der Klasse **Exception**, die wiederum Subklasse von **Throwable** ist. **Throwable** ist die Superklasse aller Klassen, die in einer Throw-Anweisung und in Catch-Zweigen bzw. Throws-Klauseln vorkommen durfen. Mit **RuntimeException** wird also ein Zweig der Exception-Klassenhierarchie eingeleitet, dessen Elemente alle unchecked sind.

Neben **Exception** ist auch **Error** Subklasse von **Throwable**. Errors jedoch nicht gefangen werden, sondern zu einem sofortigen Programmabbruch fuhren. Die Konstruktion

1175 **if (_) throw new Error("das ist schiefgeangen!"):**

wobei die Auslassungszeichen für die Formulierung einer Invariante stehen, hat man fruher zur Emulation der inzwischen vorhandenen Asert-Anweisung verwendet; auch heute sollte man Errors eigentlich nur wahrend der Testphase eines Programms einsetzen. Genau wie Exceptions der Sorte RuntimeException sind Errors unchecked.

### Multi-threading

Ahnlich wie Smalltalk erlaubt auch Java, parallele Ausfuhrungstrange zu programmieren. Diese heissen in Java jedoch nicht Prozesse, sondern Threads. Threads sind im Gegensatz zu den Prozessen eines Betriebsystems leichtgewichtig, was sovi heissen soll wie dass sich Threads die getrennte Allokierung von Ressourcen (wie Hauptspeicher) sparen, und alle auf denselben Ressourcen operieren. Es können also mehrere Threads innerhalb eines Prozesses laufen. Der Preis dafur ist, dass die Mechanism zur Synchronisation bei Threads selbst realisert werden mussen; bei Prozessen sind sie über die Inter-Prozess-Kommunikation des Betriebsystems geregelt. (Bei den Prozessen Smalltalks handelt es sich also auch eher um Threads als um Prozesse im eben beschriebenen Sinn.)

In Java wird ein neuer Thread gestartet, indem man eine neue Instanz der **Thread erzeugen und** **Klasse Thread erzeugt und** **aufir die Methode start() aufruft.**

### **[new Thread()].start()**

**startet also einen neuen Thread. Bleibt die Frage, was dieser Thread tut.**

**Die Klasse Thread besitzt dafur eine Methode run(), die von start() aufgerufen wird. Diese Methode ist jedoch leer, so dass der Thread gleich wieder beendet wird. Damit ein neuer Thread etwas Sinnvilles tut, gibt es zwei Moglichkeiten:**

1. **Man definiert eine neue Subklasse von Thread und** **überschreibt darin die Methode run() so, dass sie das Gewunschte tut oder zumindest anstosst.**
2. **Man lasst eine Klasse das Interface Runnable** **implementieren, implementiert dann in der Klasse die vom Interface gefoerderte Methode run(), erzeugt von dieser Klasse eine Instanz i und startet deren Methode run() mittels (new Thread(i)).start()(start()ruft dann run() auf i auf).**

**Auch im zweiten Fall wird eine Instanz der Klasse Thread erzeugt, die den neuen Thread reprasentiert. Man beachte jedoch, dass diese Instanz nicht selbst der Thread ist -- der Thread ist, wie gesagt, ein paralleler Ausfuhrungstrang der JVM, der, genau wie der Ausfuhrungstrang, mit dem das Programm startet, nicht an ein Objekt gebunden ist, sondern mit dem Kontrollfluss zwischen den Empfangerobjekten hin- und hewechselt. Aktive Objekte, also Objekte, die ihren eigenen Ausfuhrungstrang haben und auch behalten (s. Kapitel 16), mussen in Java genau wie in Smalltalk simuliert werden. Jeder Thread hat aber ein Thread-Objekt, das ihn reprasentiert; es kann mit Thread.currentThread() erfragt werden. Mit ihm sind so spezifische Daten wie der Name des Threads, seine Prioritat etc. gespeichert.**

**Die Threads Javas benotigen also eine explizite Synchronisation. Ahnlich** **Synchronisation****über** **Locking: Monitorer** **wie die Prozesse Smalltalks funktioniert dies mit Semaphoren, die hier** **Locking: Monitorer** **allerdings** **Monitore** **genannt werden. Jeder Monitor ist mit einem Objekt verbunden (und jedes Objekt mit einem Monitor); wenn ein Thread einen Monitor eines Objektes sperrt(_,lockt"), dann kann kein anderer Thread den Monitor sperren, bevor die Sperre durch den ersten Thread wieder aufgehoben wird.

Es gibt zwei Moglichkeiten, die Synchronisation von Threads zu erzwingen. Die eine erfolgt mittels der Synchronized-Anweisung, die Sie oben schon kurz kennengelernt haben: Die Anweisungen eines Blocks können nur ausgefuhrt werden, wenn sie nicht gerade von einem anderen Thread ausgefuhrt werden. Das mit dem Block assozierte Objekt, auf dessen Monitor die Sperre durchgefuhrt wird, wird explizit mit der Synchronized-Anweisung angegeben (haufig ist es this, also das Objekt, in dessen Kontext sich der Block befindet).

Die zweite Moglichkeit ist, eine ganze Methode mit **synchronized** zu deklarieren. Wenn es sich dabei um eine Instanzmethode handelt, wird die Sperre auf dem Objekt, auf dem die Methode aufgerufen wurde, erwirkt; handelt es sich dagegen um eine Klassemmethode (also um eine, die static deklariert wurde), dann geht die Sperre auf das Objekt, das die Klasse reprasentiert. Felder lassen sich ubrigens nicht **synchronized** deklarieren

### Metaprogrammerung

Obwohl in Java langst nicht alles ein Objekt ist, gibt es doch die Moglichkeit, auf die Elemente eines Programms zuzugreifen. Daftur ist das sog. _Reflection_ API zustandig, in dem für jede Art von Programmelement eine Klasse existiert, deren Instanzen entsprechende Programmelemente reprasentieren. (So gibt es dort eine Klasse **Method**, eine Klasse **Field** etc.) Eine genauere Betrachtung dieser API wurde an dieser Stelle jedoch zu weit fuhren; sie wird im Kurs 01853 (_,Moderne Programniertechniken und -methoden") ausführlicher behandelt.

Eine andere Form der Metaprogrammerung, die sog. **Annotationen**, haben zunächst nichts mit Objektorientierung zu tun -- es werden damit lediglich Programmelementen im Queltext Daten, sog. Metadaten, zugeordnet. Diese können dann wahrend der übersetzung und/oder wahrend der Austfuhrung des Programms abgefragt werden und so den jeweiligen Prozess beeinflussen oder sogar steuern. In Java 5 wurden Annotationen als eine spezielle Art von Interfaces eingefuhrt, die jedoch keine Methoden, sondern nur Felder (!) deklarieren. Annotation sind ebenfalls Gegenstand des Kurses 01853.

## 48 Ein abschliessendes Beispiel

Um Ihnen eine grobe Vorstellung davon zu geben, wie Java-Programme aussehen, finden Sie nachfolgend den Quellcode für ein Programm, das ein einfaches Ratespiel umsetzt. Das Programm besteht aus vier Klassen, namlich der Klasse **Ratespiel**, die im wesentlichen die Startmethode nebst Initialisierung der Datenstruktur enthalt, sowie den Klassen **Knoten**, **Tier und Merkmal**. Das Interface Frage dient der gemeinsamen Abstraktion von Tierund Merkmal und verlangt von den beiden Klassen lediglich, dassie eine Methode stellen() implementieren und auf den Aufruf derselben einen Wahrheitswert (die Antwort auf die gestellte Frage) zuruckliefern. Die Methoden der Klasse KeyboardInput dienen der Interaktion mit der Benutzerin über die Konsole, deren Moglichkeiten in Java (wie in SMALLtalk) von Haus aus nur schwach ausgepragt sind. System.out bezeichnet den auch den Ausgabestrom, der mit der Konsole verbunden ist, und die Methode printIn(.) gibt etwas darauf aus.

```
1177publicclassRatespiel{
1178publicstaticvoidmain(String[]args){
1179KnotenstartKnoten=newKnoten(newTier("Huhn"));
1180do{
1181System.out.println("DenkedireinTierausunddruckeRtn!");
1182KeyboardInput.tasteDrucken();
1183startKnoten.fragen();
1184System.out.println("Mochtestdunochmal?");
1185}while(KeyboardInput.ja());
1186}
1187}
1188interfaceFrage{
1189booleanstellen();
1190}
1191publicclassKnoten{
1192Fragefrage;
1193Knotenja;
1194Knotenenen;
1195publicKnoten(Fragefrage){
1196this.frage=frage;
1197nein=null;
1198ja=null;
1199}
1200publicvoidfragen(){
1201booleanantwort=frage.stellen();
1202if(antwort){//Antwortpositiv
1203if(ja!=null)//weitereFragenvorhanden:
1204ja.fragen();//mitJa-Knotenweitermachen
1205else//keineweiterenFragenvorhanden:
1206System.out.println("Fertig.");
1207}
1208else{//Antwortnegativ
1209if(nein!=null)//weitereFragenvorhanden:
1210nein.fragen();//mitNein-Knotenweitermachen
1211else{//keineweiterenFragenvorhanden:
1212Stringname=KeyboardInput.antwort("Wiehei&tesdann?");
1213TierneuesTier=newTier(name);
1214Stringmermalsfrage=
1215KeyboardInput.antwort("NennemireeFrage,diefur"
1216+neuesTier.name()+"mitJaundfur"
1217+((Tier)frage).name()
1218+"mitNeinbeantwortetwernden muss!");
1219MerkmalneuesMerkmal=newMerkmal(merkmalsfrage);
1220ja=newKnoten(neuesTier);nein = new Knoten(frage); // frage wandert nach unten!
1222 frage = neuesMerkmal;
1223 System.out.println("Gut!");
1224
1225
1226
1227
1228public class Tier implements Frage {
1229 private String name;
1230 public Tier(String name) {
1231 this.name = name;
1232 }
1233 public String name() {
1234 return name;
1235 }
1236 public boolean stellen() {
1237 System.out.println("Heist es " + name + "?");
1238 return KeyboardInput.ja();
1239 }
1240
1241public class Merkmal implements Frage {
1242 String frage;
1243 public Merkmal(String frage) {
1244 this.frage = frage;
1245 }
1246 public boolean stellen() {
1247 System.out.println(frage);
1248 return KeyboardInput.ja();
1249 }
1250

Die Klassen Tier und Merkmal sind beide recht klein und unterscheiden sich nur wenig. Beide speichern pro Instanz einen String, einmal in der Instanzvariable name, einmal in der Instanzvariable frage. Diese Strings werden jeweils bei der Erzeugung der Objekte per Konstruktoraufruf übergeben (so z. B. in Zeile 1179) und in der Folge nicht mehr geandert (die Instanzvariablen sind private deklariert und es gibt aufger dem Konstruktor keine Methoden der Klassen, die Schreibend darauf zugeifen, also die Instanzvariable auf der linken Seite einer Zuweisung stehen haben). Beim Stellen der Frage fugt Tier noch etwas Text zu dem Inhalt von name hinzu, so dass sich eine vollstandige Frage ergibt; für Merkmale muss die Frage so einggegeben werden, wie sie hinterher gestellt wird.

Das Gros der Anwendungslogik steckt in der Klasse Knoten. Ihre Instanzen stellen die Knoten eines binaren Baums, von denen der eine Nachfolger den Ja-, der andere den Nein-Zweig beinhaltet. Zudem muss jeder Knoten eine Frage haben; dass die entsprechende Instanzvariable frage heisst und vom Typ Frage ist, druckt aus, dass mit jedem Knoten entweder eine Tier- oder eine Merkmalsfrage verbunden ist. Dass nur die Blatter einesBaums Tierfragen beinhalten durfen, wird durch die Variablendeklarationen nicht ausgedruckt; das steckt in der nachfolgenden Programmlogik, der Implementierung der Methode fragen().

Die Methode fragen() enthalt eine Unterscheidung von vier Fallen, die sich aus der Beanntwortung der zu dem Knoten gehorenden Frage (ja oder nein) und dem Umstand, ob es sich um einen Blattknoten handelt (was man daran sehen kann, dass ja bzw. nein den Wert null haben) ergeben. Die Schachtelung der insgesamt drei If-else-Anweisungen ist Standard und hat mit Objektorientierung nichts zu tun. Objektorientiert ist dagegen die Fallunterscheidung, die sich hinter dem Aufruft frage.stellen() (Zeile 1201) verbirgt: Da frage eine Instanz der Klasse Tier oder Merkmal benennen kann, die beiden Klassen die Methode stellen() aber jede für sich implementieren, wird hier eine Fallunterscheidung per dynamischem Binden getroffen. Man beachte, dass die Unterscheidung, ob ein Knoten Blattknoten ist, ebenfalls per dynamisches Binden getroffen werden konnte; ihre Programmierin hat sich aber im Rahmen ihrer kreativen Freiheit dagegen entschieden.

Vielleicht ist lhnen aufgefallen, dass auf der Konstruktoren keine der Methoden einen Parameter hat. Es ist dies ein Zeichen für eingelungenes objektorientiertes Design. für Programmierierinnen, die aus der imperativen Programmierung kommen, ist dies gewohnungsbedurftig -- intuitiv denkt man zunächst, dass die Methoden stattlessen wohl auf globale Variablen zugereifen werden, weswegen man spontan die Nase rumpfen mochte. Das ist aber nicht der Fall: Alle Methoden greifen ausschliesslich auf Instanzvariablen zu. Diese gibt es aber in der imperativen Programmierung nicht.

## 49 Losungen zu den Selbsttestaufgaben

Es gibt keines. Man weiss nur, dass die Elemente von liste Number oder einem Subtyp davon als obere Schranke haben. Sobald es nicht mehr **Number** ist, können keine Instanzen vom Typ **Number** mehr zugewiesen werden, und je tiefer man den Subtyp wahlt, desto weniger Typ können zugewiesen werden. Solange es keinen gemeinsamen tiefsten Subtyp aller Subtypen von **Number** gibt, können auch dessen Instanzen nicht als gultige Zuweisungen angenommen werden. Einzige Anwahme: null.

Aber: Wenn **Number** final deklariert ware (so dass es keine Subttypen von **Number** gabe), dann konnte man auch **Number** als Elementtyp annehmen -- dann ware jedoch auch der ganze Umstand mit dem Typ-Wildcard nicht erforderlich.

* [1251] ArrayList<Object> o = new ArrayList<Object>();
* [1252] ArrayList<String> s = new ArrayList<String>();
* [1253] Und jetzt noch prufen, ob s.getClass() == o.getClass() zu true auswertet, wenn man bloss wusste, wie das in JAVA geht... (s. Funnote 3).

* [1254] Selbsttestaufgabe 43.2 (Seite 233)
* [1255] Sie gibt immer eine Lite zuruck, deren Elemente den deklarierten Typ Object haben. Wenn man die Elemente anders verwenden will, muss man einen _Down cast_ durchfuhren, der fehlschlagen (zu einem dynamischen Typfehler fuhren) kann.

[MISSING_PAGE_EMPTY:269]

Kurseinheit 5: Andere objektorientierte Programmiersprachen

A language that doesn't affect the way you think about programming, is not worth knowing.

Alan Perlis

Wahrend der obige Leitspruch aus akademischer Sicht sicher richtig ist, können sich Praktikerinnen (und solche, die es werden wollen) diese Einstellung nicht leisten. Stattdessen muss man die Sprachen kennen, für die es einen Markt gibt. Und so zeichnen sich die in dieser Kurseinheit behandelten Sprachen mit Ausnahme von Eiffel weniger durch revolutionare Konzepte oder neuartige Sichtweisen aus, sondern vielmehr dadurch, dass sie in der Prais weite Verwendung finden. Gleichwoohl mag die eine oder andere Eigenheit der einen oder anderen Sprache der Leserin Anlass geben, ihre bisherigen Denkweisen zu überprufen.

Ziel dieser Kurseinheit ist es ubrigens nicht, Sie zu Programmierrinnen in einer der (oder gar allen) in dieser Kurseinheit behandelten Sprachen C#, C++ und Eiffel zu machen. Ziel ist vielmehr, lhnen eine erste Ubbersicht und ein Verstandnis dieser Sprachen zu vermitteln. Sie sollen einen Eindruck davon bekommen, auf was Sie sich einlassen, wenn Sie sich eindscheiden, in einer der genannten Sprachen Software zu entwicken. Dazu gehort nicht, jedes Konstrukt jeder dieser Sprachen zu kennen oder auch nur einmal gesehen zu haben, sondern vielmehr eine Vorstellung davon, was jeweils deren charakteristische Eigenschaften, was die Starken und was die Schwachen jeder einzelnen Sprache sind. Je nachdem, wie sich die einzelnen Sprachen von bereits besprochenen unterscheiden, fallt die folgende Darstellung kurzer oder langer aus.

## 50 C#

C# ist Microsoftts Antwort auf Java. Oberflachlich betrachtet Java recht ahnlich, enthalt C# doch einige zusatzliche Merkmale von C++, aber auch solche von Microsoftts Haussprache Visual Basic. Dabei ist die Entwicklung von C# wohl weniger der Versuch, mit der Microsoft eigenen Marktmatht einen proprietaren Standard durchzudrucken (was bei Programmiersprachen meines Wissens bislang auch noch nie gelungen ware), sondern vielmehr dem Umstand geschuldet, dass Java keine volle Kontrolle über Rechner und Betriebssystem biett und somit nicht für jede kommerzielle Softwareentwicklung geignet ist. Zwar war auchSun benntht, bekannte Schwachen zu beheben, aber man gibt sich dabei doch recht schwerfallig. Und so war, bei dem nicht zu übershenden Erfolg Javas in der Softwareentwickierinnnengemeinde, die Abspaltung einer eigenen, Java-artigen, aber eben doch in wichtigen Punkten verschiedenen Sprache eigentlich nur folgerichtig.

### Das Programmiermodell von C#

Das Programmiermodell von C# unterscheidet sich zunächst nicht wesentlich von dem Javas: Auch in C# ist der Code auf Klassen verteilt, die einzeln übersetzt werden können. Klassen werden in Dateien gespeichert, jedoch ist das Verhaltnis von Klasse zu Datei lockerer als in Java (u. a. können Klassen anders heissen als ihre Dateien und sogar auf mehrere Dateien aufgeteilt werden). Allerdings sind der Bytecode und die dazu passende virtuelle Maschine nicht speziell für C# entworfen, sondem für alle sog..NET-Sprachen. So heißt denn auch die Sprache des Bytecode _Common Intermediate Language_ (CLI); sie gilt als (grade noch) menschenlesbar.

Anders als bei Java waren bei C# Flexibilitat und Performanz von Anbe-ginn kritische Gesichtspunkte des Sprachentwarfs. für C# war daher von

Anfang an und ausschliesslich die sog. Just-in-time-(JIT-)Kompilierung vorgesehen, die den CIL-Code unmittelbar vor der Ausfuhrung (und nur, wenn er überhaupt ausgefuhrt wird) in Maschinencode der Maschine, auf der er gerade lauft, übersetzt. Die Einheiten der JIT-Kompilierung gehen dabei hinunter bis zu einzelnen Methoden. Eine vollstandige Kompilierung von CIL- in nativen Maschinencode vor der Ausfuhrung ist ebenfalls moglich.

Eine andere Eigenschaft Javas, mit der die Programmiererinnen Micro-

softs offenbar nicht unter allen Umstanden leben konnten, ist die

_Garbage collection_. In C# hat man daher die Moglichkeit, den Speicherplatz für Objekte, die mit **new** erzeugt wurden, selbst wieder freizugeben. Doch wehe der, die das vergisst: Speicherlecks sind die unmittelbare Folge. Noch schlimmer sind aber Speicherfreigaben von Objekten, auf die noch Referenzen existieren: Die zeigen dann ins Leere oder, wenn der Speicher wieder belegt wird, auf oder mitten hinein in ein anderes Objekt. Eine Katastrophe.

Aber damit nicht genug: Das mit Smalltalk und Java abgeschaffte Han-

**explizite Pointer**

tieren mit Pointern wurde in C# auch wiedereingefuhrt, wohl weil man in der systemnahen Programmierung (und bei Aufrufen in das hauseigene Betriebssystem) nicht darauf verzichten konnte. Allerdings sind beide Ruckschritte -- explizite Speicherverwaltung und das Hantieren mit Pointern -- in sog. _unsichere Bereiche_ verbannt. Dazu gibt es in C# einen Modifizierer unsafe, der solche Bereiche einleitet:

```
1253publicstaticunsafevoidSwap(int*x,int*y){
1254inttemp=*x;
1255*x=*y;
1256*y=temp;
1257Dabei bedeuttet der Stern hinter einem Typ, dass es sich um einen Zeiger-auf-Typ handelt; vor einer Variable bedeutet er, dass die Variable dereferenziert wird, also nicht auf den Pointer, sondern auf die Speicherstelle, auf die der Pointer zeigt, zugegriffen wird. Nebenbei bedeuttet der Stern aber auch noch die Multiplikation und all das, worfur er sonst noch überladen wurde.

Neben Methoden können auch Klassen, Blocke und Variablen unsicher sein.

### Gemeinsamkeiten mit und kleinere Unterschiede zu JAVA

C# unterscheidet sich, was Objekte, Variablen und Ausdrucke, Anweisungen, Blocke und Kontrollstrukturen angeht, nicht grossartig von JAVA. Es ist in C# allerdings moglich, Operatoren (also z. B. +, -, == etc., aber nicht new, ( ), ||, &&, =) zu überladen. C# besitzt dafur das Schlusselwort operator, das in einer Operatordefinition (die ansonsten so aussieht wie eine Methodendefinition) vorangestellt wird:

1258static Matrix operator +(Matrix m1, Matrix m2) {-}

Außerdem ist es in C# Konvention, Methodennamen mit einem Gross- || **Call by reference** buchstaben beginnen zu lassen, aber das ist wie gesagt nur Konvention. Wichtiger (und für viele Programmierprobleme von unschatzbarern Wert) ist da schon die Moglichkeit von C#, _Call by reference_ nach dem Vorbild Pascals (also ohne explizite Pointer; s. o.) zu erlauben und damit Funktionen wie das Vertauschen von Variableninhalten (die Methode swap) sicher zu programmieren:

1259publicstaticvoidSwap(refintx,refinty){1260inttemp=x;1261x=y;1262y=temp;1263}

Allerdings muss ref -- anders als in Pascal var -- auch an der Aufruftstelle verwendet werden. Formale Parameter können auch mit out modifiziert werden (wobei für die Aufruftstelle dasselbe gilt wie für ref):

1264publicstaticvoidAenderbar(outStrings){1265s="auchdertatsachlicheParameteristgeandert!"1266}

Der Unterschied ist der, dass bei Verwendung von ref die Variable, die den tatsachlichen Parameter liefert, vor dem Aufruf initialisiert worden sein (einen Wert zugewiesen bekommen haben) muss, wahrend dies bei out nicht der Fall ist. Daft muss bei out der formale Parameter in der Methode einen Wert zugewiesen bekommen. Dass ref und out in C# anders als var in Pascal an der Aufruftstelle wiederholt werden mussen, hat den Vorteil, dass die Programmiererin weiss, dass ihre die tatsachlichen Parameter liefernden Variablen nach dem Aufruf andere Werte haben können. Sie drucken also das Vorhandensein einer Zuweisung in beide Richtungen (hin und zuruck) aus.

Oberlegen Sie, welche Konsequenzen sich aus der Verwendung von **ref** bzw. **out** im Kontext des Subtyping ergeben.

Sowohl **ref** als auch **out** ermoglichen, dass eine Methode mehr als einen Ruckgabewert hat. Da diese Moglichkeit in Java und Smalltalk fehlt, findet man in diesen Sprachen haufig Klassen vor, die einzig dem Zweck dienen, mehrere Ruckgabewerte in einem Objekt zu verpacken. Da sie an der Auftristelle aber wieder ausgepackt werden mussen, ist das eine ziemlich umstandliche Losung. Eine elegantere Alternative sind die Tupel Effells (s. Abschnitt 52.7).

Nun verdient C# im Kontext von Methodenauftrufen nicht nur lobende Erwahnung. Die wohl bedeutendste Unterlassung ist, dass es in C# keine Throws-Klauslen in Methodedeklarationen gibt -- die aus Java bekanntte Unterscheidung von _Checked exceptions_ und _Unchecked exceptions_ (Abschnitt 47.2 in Kurseinheit 4) entfallt also und es gibt nur Unchecked exceptions. Das bedeutet, dass die Auftruferin einer Methode nicht gezwungen wird, darüber nachzudenken, was zu tun ist, wenn die Methode nicht korrekt ausgefuhrt werden kann; ja sie weiss nicht einmal bei Betrachten der Schnittstelle, dass die Methode auch abgebrochen werden kann. Das ist naturlich debattierbar, soll aber dem Umstand Rechnung tragen, dass bei einer stark geschichteten Architektur (beispielsweise beim Einsatz von Middleware) das Wissen um Exceptions auf der ganzen Wegstrecke von der Exception-Quelle bis zum Exception handler vorhanden sein muss, obwohl die mittleren Schichten naturgemas an Art und Auftreten von Ausnahmen keinerlei Interesse haben. Das mit Java Version 1.4 eingefuhrte sog. _Exception chaining_ erlaubt, eine Checked exception in einer Unchecked exception zu verpacken und spater, z. B. nach Durchlaufen der Middleware, wieder auszupacken (erneut zu werfen). Das sog. _Exception tunneling_ bietet ebenfalls Abhilfe.

Ein weiterer, für die Programmierpravis nicht weniger bedeutsamer Unterschied bei Methoden ergibt sich im Zusammenhang mit dem Oberschreiben: Wahrend in Java alle Methoden im Prinzip überschrieben werden können (es sei denn, ihre Definition tragt den Zusatz final), so dass der Compiler zunächst von einer dynamischen Bindung der Auftrufe ausgehen muss, sind in C#, der Tradition von C++ folgend, dynamisch zu bindende Methoden unbedingt als solche zu deklarieren, und zwar mit dem Schlusselwort virtual. Entsprechend muss eine überschreibende Methode mit dem Schlusselwort override deklariert werden. Soll hingegen eine Methode gleicher Signatur in einer Subklasse neu eingefuhrt (und nicht anstelle der, die sie überschreibt, dynamisch gebunden) werden, dann ist dies durch Verwendung des Schlusselworts new bekanntzugeben. Anders als landlaufig angenommen hat dies nicht nur Performanzgrunde (es vermindert die Zahl der dynamischen Bindungen in einem Programm), sondern auch gewichtige programmiertechnische: Man markiert alle Stellen im Programm, an denen das sog. _Fragile-base-class-Problem_ (Thema von Kapitel 55 in Kurseinheit 6) auftreten kann.

Einige Sprachkonstrukte verwenden in C# andere Schlusselworter als

**Unterschiede bei den**

Java, so **lock** anstatt synchronized sowie **foreach** anstatt for fur**

**Anweisungen**

die zweite Form von For-Schleifen (s. Kapitel 38 in Kurseinheit 4). Andere weichen in ihrer Bedeutung leicht von denen Javas ab: So sind auch Strings als Basis einer Switch-Anweisung zugelassen (in Java erst seit Version 71) und jeder Zweig (case), der mindestens eine Anweisung enthalt, muss mit einer expliziten Kontrollfussanweisung (**break**, **goto**, **return** oder **throw**) abgeschlossen werden. Außerdem hat C# eine Goto-Anweisung, mit der man jedoch nicht in Blocke hinein springen kann. All dies hat allerdings nichts mit Objektorientie- rung zu tun.

### Zusatzliche Ingredienzien von Klassendefinitionen in C#

Fur die Programmierpraxis recht nutzlich sind die in C# vorgesehenen zusatzlichen Elemente

einer Klassendefinition. Es sind dies Properties, Indexer und Events.

#### Properties

**Properties** sind gewissermangen die Umkehrung von Zugriffsmethoden (_Setterm_ und _Getterm_; s. Abschnitt 4.3.4 in Kurseinheit 1): Anstatt auf ein Feld eines Objektes über Methoden (lesend und Schreibend) zuzugreifen, ruff man Methoden über das auf, was syntaktisch wie ein Feldzugriff aussieht. Dies erlaubt einer, (lesende und schreibende) Feldzugriffe mit Nebeneffekten zu versehen (wie z. B. einer dynamischen Typprufung bei schreibendem Zugriff, wenn man kovariante Redefinition imitieren will). Konkret: Anstatt des (auch in Java ublichen)

```
1267classPunkt{
1268privatefloatx,y;
1269voidSetXY(floatx,floaty){
1270this.x=x;
1271this.y=y;
1272}
1273floatGetX(){
1274returnx;
1275}
1276floatGetY(){
1277returny;
1278}
1279voidSetRadiusWinkel(floatr,floatw){
1280x=Math.Cos(w)*r;
1281y=Math.Sin(w)*r;
1282}
1283floatGetRadius(){
1284returnMath.Sqrt(x*x+y*y);
1285}

* [1286] floatGetWinkel() {
* [1287] returnMath.Acos(x/r);
* [1288] }
* [1289] }

kann man in C# alternativ

* [1290] classPunkt {
* [1291] privatefloatx,y;
* [1292] floatX{
* [1293] get(returnx;)
* [1294] set{x=value;}
* [1295] }
* [1296] floatY{
* [1297] get(returny;)
* [1298] set{y=value;}
* [1299] }

* [1300] floatRadius{
* [1301] get(returnMath.Sqrt(X*X+Y*Y);)
* [1302] set{
* [1303] floatw=Winkel;
* [1304] x=Math.Cos(w)*value;
* [1305] y=Math.Sin(w)*value;
* [1306] }
* [1307] }

* [1308] floatWinkel{
* [1309] get(returnMath.Acos(X/Radius);)
* [1310] set{
* [1311] floatr=Radius;
* [1312] x=Math.Cos(value)*r;
* [1313] y=Math.Sin(value)*r;
* [1314] }
* [1315] }
* [1316] }

schreiben. Dabei sind get und set Schlusseworter von C# und **value** ist eine spezielle Variable (vergleichbar mit this), die den Eingabewert eines Setters halt. Um einem Punkt seine Koordinaten zuzuweisen bzw. darauf zuzugereifen, kann man dann die Properties X, Y, Winkel und Radius wie Felder verwenden:

* [1317] **Punkt p=newPunkt();**
* [1318] p.X=1;**
* [1319] p.Y=1;**
* [1320] **if(p.Radius==Math.Sqrt(2)&&p.Winkel==Math.PI/4)**

Keine grosse Sache, aber es macht den Code auf Aufruferinnenseite knapper und besser lesbar. Den Getter oder den Setter kann man wahlweise auch weglassen; auf diese Weise lassen sich Felder mit Nur-lese- bzw. Nur-schreib-Zugriff simulieren.

#### Indexer

**Indexer** übertragen gewissermangen das Konzept der indizierten Instanzvariablen von SMALLTAK auf C#: Jede Instanz einer Klasse, für die ein Indexer definiert ist, hat eine Menge von (scheinbar unbenannten) Instanzvariablen, die über einen Index zugegriffen werden können. Allerdings muss die indizierte Instanzvariable klassenintern durch eine normale, benannte Instanzvariable (Feld) reprasentiert werden; Indexer ahneln Properties insofern, als der Zugriff über einen Index mittels entsprechender Get- und Set-Abbildungen auf einen Zugriff auf eine benannte Instanzvariable übersetzt wird. Das folgende Beispiel illustriert den Vorgang:

```
1321class HatScheinbarEineIndizierteInstanzvariable{
1322private Object[]iivar;
1323HatScheinbarEineIndizierteInstanzvariable(intanzahl){
1324iivar=newObject[anzahl];
1325}
1326Objectthis[intindex]{
1327get{returniivar[index];}
1328set{iivar[index]=value;}
1329}
1330}
```

Dabei wird this als Schlussewort missbraucht, um anzudeuten, dass bei Zugriffen auf die indizierte Instanzvariable kein Name einer Instanzvariable (eines Feldes), sondern lediglich der Name des Objekts, zu dem sie gehort, steht:

```
1331HatScheinbarEineIndizierteInstanzvariablee einObject=new
1332einObject[0]=einObject[1];
```

Nun darf der Indexer in C# überladen werden, so dass ein Objekt mehrere indizierte Instanzvariablen haben kann, wobei der Zugriff (aufgund des fehlenden Namens) einzig über den Typ des Indexes differenziert erfolgen kann. Durch das überladen ist es wiederum moglich, nicht eine, sondern mehrere indizierte Instanzvariablen zu simulieren, was jedoch der Beschrankung unterliegt, dass der Elementtyp (der Ruckgabetyp beim überladen) gleich bleiben muss. Und schliesslich muss ein Indexer auf keine interne (benannte) Instanzvariable zugerefen -- alle Inhalte können, genau wie bei Properties, auch berechnet werden.

#### 50.3.3 Ereignisse (Events)

Viele Applikationen, insbesondere solche mit GUI, benotigen neben der direkten Kommunikation zwischen Objekten, die sich kennen (die ja durch Nachrichtenaustausch bzw., je nach Diktion, durch Methodenaufrufe bewerkstelligt wird), auch eine Kommunikation mit unbekannten. Die Problematik hatten wir im Kontext von SMALLTAK bereits besprochen (Abschnitt 14.3 in Kurseinheit 1).

Nun kommt dieses Problem so haufug vor, dass man sich bei MICROSoft

dafur entschieden hat, es zumindest teilweise von der Ebene der Programmerung (wo es in Form eines sog. _Patterns_ abgehandelt wird; mehr dazu in Kurs 01853) auf die Ebene der Programmiersprache zu heben (in SMALLtalk, wo diese Unterscheidung nicht so ausgepragt ist, war das Problem ja mittels einer Implementierung der benotigen Mechanismen in der Klasse Object, von der alle anderen erben, gelost worden). Es wurde zu diesem Zweck das Konstrukt des **Events** (Ereignisses) eingefuhrt, über das sog. _Event handler_ aktiviert werden können. Dabei sind die Event handler in Abschnitt 50.4.1 skizzierte sog. _Deleggates_. Leider ist die mit Deklaration und Registrierung von Event handlern sowie der Verbreitung von Ereignissen verbundene Syntax von C# nach Ansicht des Autors dieses Textes komplett uneserlich geraten, so dass hier auf eine weitergehende Befassung mit dem Thema verzichtet wird.

### Das Typsystem von C#

Auch wenn es in grossen Teilen recht ahnlich ausfallt, so weicht das Typsystem von C# von dem JAVAS gleich in mehreren wesentlichen Punkten ab:

* der Art der Unterscheidung von Wert- und Referenztypen,
* den angebotenen Typkonstruktoren für Wert- und Referenztypen und
* dem Umgang mit Interfaces als Typen.

Darüber hinaus hat C# noch eine ganze Reihe weiterer Verbesserungen, die man mit dem Typsystem in Verbindung bringen kann; auf sie wird hier aber nur am Rande eingegangen.

#### Die Typhierarchie von C#

In C# sind genau wie in JAVA alle Variablen typisiert. Anders als in JAVA wird dabei jedoch zunächst nicht zwischen Wert- (primitiven) und Referenztypen unterschieden: Alle Typen, auch die primitiven, gelten als von Object (genauer: System.Object) abgeleitet. Da lohnt es sich, auf die Typhierarchie etwas genauer einzugehen.

Genaugenommen ist die Typhierarchie von C# gar nicht die Typhierarchie

von C#, sondern die von.NET: Sie ist namlich für alle.NET-Sprachen dieselbe. Das liegt daran, dass.NET für alle seine Sprachen ein gemeinsames Typsystem vorsieht, namlich das Common Type System (CTS). Das CTS sorgt dafur, dass Typen, die in einer Sprache definiert wurden, auch in einer anderen Sprache verwendet werden können, und zwar ganz so, als seien sie in der anderen Sprache selbst definiert worden. Wie man sich leicht vorstellen kann, sind dafur einige Konventionen notwendig.

Das erste Merkmal des CTS ist, dass alle Typen in einer Hierarchie untergebracht sind. Die aus JAVA bekannte Ausgrenzung der primitiven Typen

Werttypen gibt es also nicht. Tatsachlich sind die primitiven Typen als eine von mehreren Arten vonWerttypen in der Hierarchie angesiedelt. Eine weitere wichtige Form von Werttypen sind die (aus Pascal bekannten und inzwischen auch in Java, dort aber als Referenztypen angekommenen) Aufzahlungstypen, deren Elemente (Werte) von der Programmiererin selbst angegeben werden können (im Gegensatz zu denen der primitiven Typen, deren Werte mit der Sprachdefinition vorgegeben sind):

1333enum Colour { Red, Blue, Green }

Aus Werttypen können, genau wie in Pascal oder C, mittels des Typkonstruktors struct (dem C-Aquivalent von Pascals record) neue Werttypen erzeugt werden, die sogar Methoden und Konstruktoren haben können, die aber keine Klassen sind (und insbesondere keine _Typenweiterung_ und somit auch keine _Verebung_ erlauben):

1334struct Point {

1335intx,y;

1336voidmove(intx,inty) {_}

1337

Man ergpart sich durch das Weglassen der Typenweiterung die Projektion bei Zuweisungen, also das Fallenlassen von Feldern, die ein erweiterter Typ hinzugefugt hat und für die im für die Zielvariable reservierten Speicher kein Platz ist (vgl. Kapitel 23 in Kurseinheit 2, insbesondere Fussnote 50). Der Typkonstruktor,,Array von" ([]) fuhrt in C# jedoch, genau wie in Java, zu einem Referenztypen.

Bei den Referenztypen wird dann das zweite wichtige Unterscheidungsmerkmal sichtbar: Neben Klassen, Interfaces und Arrays gibt es auch noch sog. **Delegates**, das sind im wesentlichen (Zeiger auf) an ein Objekt gbundene, einzelne Methoden. Delegates ersetzen die aus anderen Sprachen bekannten Funktionspointer; sie konnten in Java bis Version 8 nur recht umstandlich über Interfaces und anonyme innere Klassen emuliert werden, an deren Stelle heute freilich die Lambda-Ausdrucke Javas treten können (s. Kapitel 37 in Kurseinheit 4). Delegates sind für verschiedene Problemstellungen (z. B. Listener-Mechanismen) sehr nutzlich.

Zuletzt gibt es in C# auch noch sog. Attribut-Typen (**Attributes**); sie ent-

**Attributes** sprechen im wesentlichen den _Annotationen_, die es seit der Version 5 auch in Java gibt. Annotationen haben aber mit objektorientierter Programmierung nicht unmittelbar etwas zu tun und sind daher nicht Gegenstand dieses Kurses (s. a. Abschnitt 47.4 in Kurseinheit 4). Es sei nur soviel erwahnt, dass in C# ein Attribut namens Serializable das gleichnamige _Marker-Interface_ Javas ersetzt (vgl. Kapitel 45 in Kurseinheit 4).

Es ergibt sich die folgende grobe Einteilung der Typen von C#:

**Einteilung der Typen von C#**Wohlgemerkt, dies ist keine Klassenhierarchie, sondern lediglich eine Ein-

**Klassenhierarchie** teilung der verschiedenen Arten von Typen in C#. Die Klassenhierarchie ist wesentlich komplexer und vereinheitlicht zudem, wie ja bereits gesagt, das Typsystem von C# (wie auch das CTS), indem alle Typen von System.Object ableiten. Die Klassenhierarchie im Name-space **System** fangt dann auch ungefahr so an (Subklassen sind eingertuckt):

Object

Array

Attribute

Delegate

MulticastDelegate

AsyncCallback

EventHandler

Exception

ValueType

Boolean

Enum

DayOfWeek

Guid

TimeSpan

TypedReference

Void

Wie lhnen sicher aufgefallen ist, sind einige der Arten von Typen aus der obigen Liste jeweils durch eine spezielle Klasse (**Array**, **Delegate**, **Attribute**) vertreten. Man kann dies als Hinweis darauf verstehen, dass tatsachlich alle Arten von Typen integriert sind und es keine grundsatzlichen Barrieren zwischen ihnen gibt. In C# haben ubrigens alle Klassen auf **System.Object** ganz wie in Java _genau eine_ Superklasse; sie können aber (auch wie in Java) beliebig viele Interfaces implementieren. Die Tatsache, dass Werttypen als Subtypen eines Referenztypen (namlich Object) deklariert sind, verrat auSerdem, dass C# über _Auto boxing_ und _unboxing_ verfugt.

#### 50.4.2 Interfacetypen in C#

Zwar hat C# das Interface-als-Typ-Konzept von Java übernommen, doch hat man hier seine Rolle deutlich gestarkt. So ist es in C# moglich, dass von verschiedenen Interfaces,,geerbte", gleiche Methodendeklarationen in einer Klasse getrennt voneinander implementiert werden können. Dies geschieht mit sog. **expliziten Interfaceimplementierungen**, wie imfolgenden Beispiel dargestellt (man beachte, dass in C# der Doppelpunkt die Schlusselworter **extends** und implements ersetzt75):

Footnote 75: Der (berechtigten) Kritik, dass dies eine wichtige Unterscheidung verwischt und man so bei Betrachtung einer Klasse manchmal nicht sagen kann, welcher der aufgelisteten Supertypen Interface und welcher Superklasse ist, wird eine Namenskonvention entgegengehalten: Im Common Type System von.NET sollten alle Interfacenamen mit einem _]" beginnen. Das steht in der Tradition der bei MICRsoft weithin gebrauchten und nach dem früheren Mitarbeiter CHARLES SMOONI so genannten _ungarischen Notation_.

1338Interface Angestellte {

1339Telefonnummer gibTelefonnummer();

1340

1341interface Privatperson {

1342Telefonnummer gibTelefonnummer();

1343

1344class Person : Angestellte, Privatperson {

1345Private Telefonnummer privat, buro;

1346TelefonnummerAngestellte.gibTelefonnummer() {

1347return buro;

1348}

1349Telefonnummer Privatperson.gibTelefonnummer() {

1350return privat;

1351}

1352

Der Nutzen der expliziten Interfacemplementierung in den Zeilen 1346-

1351ist der, dass ein Objekt der Klasse Person auf die gleiche Nachricht

gibTelefonnummer() unterschiedlich reagiert, und zwar abhangig davon, über welches

Interface es angesprochen wird. Der Typ der Variable (oder des Ausdrucks), die als Empfanger fungiert, gibt also gewissermassen die Rolle (hier: **Angestellte bzw. Privatperson**) vor, in der das Objekt angesprochen wird. Es ist weder vorgesehen noch moglich, dass man an der Aufruftstelle etwas wie **x.**Angestellte.gibTelefonnummer() schreibt (wobei **x** das Objekt bezeichne); vielmehr steht dort einfach nur **x.gibTelefonnummer(). Falls ubrigens die Methodendekaration Telefonnummer gibTelefonnummer() von einem gemeinsamen Superinterface von **Angestellte** und Privatperson, z. B. Erreichbar, gerebt wurde, ware das Programm ungultitig; es muss namlich immer der tatsachlich deklarierende Typ als Qualifizierer angegeben werden.

Wenn im obigen Beispiel für die beiden expliziten Interfacemplementierungen von **gibTelefonnummer()** nicht wie in Java verlangt der Zugriffsmodifikator **public** angegeben wurde, dann geschah das nicht ohne Grund: Es ist in C# namlich moglich, Methoden nicht **public** zu deklarieren und trotzdem, per Interfacemplementierung, von aussen zugereifbar zu haben. Allerdings ist dies an die explizite Interfacemplementierung gebunden. Die sog. **implizite Interfacemplementierung**, also 

[MISSING_PAGE_FAIL:281]

eines Typs wie in Java vor, sondem eine Annotation der _Definition_ des Typs76: Dem ko- bzw. kontravarianten Typparameter wird dazu das Schlusselwort **out** bzw. in vorangestellt. Die Beschrankungen (nur lesen bzw. nur schreiben) sind dann bei allen Verwendungen des Typs die gleichen. Ubrigens: für Arrays in C# gilt dasselbe wie in Java: Sie sind kovariant, das Schreiben in ein Array kann aber zu einem Laufzeittypfehler fuhren, der in C#,,ArrayType-MismatchException" hei8t.

#### Die dynamische Komponente

C# soll genau wie Java und anders als C++ eine typsichere Sprache sein, also eine strikte Typprufung durchfuhren. Da aber (ebenfalls genau wie in Java) nicht alles zur Obersetzungszeit geschehen kann, hat auch das Typsystem von C# eine Laufzeitkomponente.

Um einen Ausdruck einer Typumwandlung zu unterziehen, bietet C# geman wie Java und C++ Casts an. Auch die Syntax unterscheidet sich nicht:

1354 (T) a bewirkt, dass der Ausdruck **a** den Typ T aufgedruckt bekommt. Ist dies nicht moglich, weil der tatsachliche Typ des Objektes, auf das a verweist, kein Subtyp von T ist oder weil keine entsprechende Typumwandlung definiert ist (einschl. Boxing/Unboxing), wird dies mit einem Laufzeitfehler quittiert. Casts sind also typsicher (in dem Sinne, dass keiner Variable ein Wert zugewiesen wird, den sie nicht haben darl), aber nicht sicher (sie können zu Ausnahmesituationen und, im Falle einer Nichtbehandlung, zu Programmabbruchen fuhren).

Um Casts sicher zu machen, bietet C# den Operator is an. Er entspricht **Typumwandlung** im wesentlichen dem **instanceof** von Java und gibt für einen Ausdruck **Typumwandlung** der Art

1355 **a is T**

wobei **a** für einen beliebigen Ausdruck und T für einen Typ steht, zuruck, ob das Ergebnis der Auswertung von **a** mit einer Variable vom Typ T zuweisungskompatibel ist. Dabei wird sowohl das Subtyping als auch das implizite (Auto-)Boxing berucksichtigt. Programmfragmente der Art

1356 **T x**;

1357 **if (ais T) {**

1358 **x = (T) a**;

1359 **

sind also sicher. Parallel zum Operator is gibt es noch einen weiteren **as**, der die typsichere Zuweisung erlaubt:wobei **a** wieder für einen beliebigen Ausdruck und T für einen Typ steht, verursacht nie einen Laufzeitfehler, weil bei mangelnder Zuweisungskompatibilitat einfach null (das mit allen Variablen zuweisungskompatibel ist) eingesetzt wird. Das obige Programmfragment (Zeilen 1356-1359) ist demnach mit dem folgenden fast aquivalent:

1361 T x;

1362 x = a as T;

1363 if (x!= null) {

1364

### 50.5 Ausblick

C# ist nicht nur Nachahmer Javas, sondern war auch Pionier für Sprach- **C# als Vorreiter** erweiterungen, die es inzwischen auch in Java gibt: So gab es in C# von Anfang an sog. Attributes, die in Java in der Version 5 als Annotationen (was in jedem Fall der bessere Name ist) Einzug gehalten haben. C# hatte auch schon ab der Version 3.0 _Lambda-Ausdruckke_ (ein Element _funktionaler Programmiersprachen_, in Smalltalk -- in Form von _Blocken_ -- schon immer vorhanden und ein Grundelement der Sprache); Java ist erst mit Version 8 nachgezogen. Die Gefahr ist jedoch, dass ich die beiden Sprachen gegenseitig totrusten -- irgendwann wird jemand auf die Idee kommen, aus den besten Eigenschaften beider eine neue Sprache zu destillieren (Kotun mag hier ein erstes Beispiel sein). Vielleicht wird bei der Gelegenheit ja auch endlich mit dem C-Erbe aufgeramt und die furchterliche Syntax entsorgt.

## 51 C++

With syntax so chaotic that even compilers have to guess at it, _C++_ code had better be reusable, because no one will ever want to reverse-engineer it. The programming language's "feature" -- being a superset of \(C\) -- is a fundamental bug. With numerous large projects being written in already obsolete dialects, _C++_ is arguably an "instant legacy" language.

über C++ ist viel geschrieben worden, nicht alles davon positiv im Tenor. Dabei wird jedoch haufig vergessen, dass eine der harten Nebenbedingungen des Entwurfs von C++, die volstandige Ruckwartskompatibilitat mit C, ein derart schweres Handicap darstellt, dass nahezu jede Kritik an C++ als unfair gelten muss.77 Naturlich kann man in C++ komplett unlesbare Programme schreiben, aber das gilt schon deswegen, weil man in C komplett unlesbare Programme schreiben kann. Man kann aber auch C++ mit einer neuen Syntax versehen (mittels seines P raprozessors, der ubrigens Turing-aquivalent ist, also die Ausdrucksstarke einer vollwertigen Programmiersprache besitzt) und dann darin komplett lesbare Programme schreiben. Wenn man denn will.

Footnote 77: Sie kennen vielleicht auch den Witz, nach dem C von Amerikanern mit dem Ziel entwickelt wurde, es den Rusen zuzuspielen, um deren Informatik um Jahrzehnte zurückznuerfen, und dass die Entwicklung der Sprache erst als abgeschlossen erachtet wurde, nachdem sich for(;P("\n"), R--;P("|")) for(e=C;e--;P("_"+(*u++/8)%2)) P("|"+(*u/4)%2); übersetzen liess.

### Das Programmiermodell von C++

Das Programmiermodell von C++ ist ein klassisches: Programme werden als Menge von Quellcode-Dateien geschrieben, die in auf einer Zielmaschine direkt ausfuhrbaren Maschinencode übersetzt werden. Getrennte übersetzung von Programmteilen ist dank sog. Header files, die die Schnittstellen der Teile enthalten, moglich. Getrenntt übersetzte Programmteile mussen vor der Ausfuhrung gebunden werden; dynamisches (Nach-)Laden von Funktionen ist moglich, muss aber explizit (programmgesteuert) erfolgen.

C++ ist als objektorientierter Nachfolger von C komzipiert und sol sol einen stufenlosen übergang von der prozeduralen zur objektorientierten Programmierung ermoglichen. Dies wird insbesondere für die Migration von Altsystemen hin zur Objektorientierung als nutzlich erachtet. Entsprechend ziekt C++ auf die gleiche Klasse von Anwendungen wie C ab: macshinennahe Programmierung wie die von Betriebs- oder eingebettetten Systemen. Extreme Speicher- und Recheneffizienz sind dabei haufig oberste Kriterien.

### Klassen

C++ ist insofern objektorientiert, als es neben den aus C übernommen Strukturen (structs) auch Klassen anbietet. Diese beinhalten, genau wie in Smalltalk und Java, neben Feldern (Instanzvariablen) auch Methoden. Klassenfelder und -methoden werden (wie in Java; s. Abschnitt 36.1 in Kurseinheit 4) mit dem Schlusselwort static in einer Klasse eingefuhrt. _Metaklassen_ gibt es in C++ nicht; gleichwohl kann der Name einer Klasse als Wert verwendet werden.

Dass man in C++ wie in Java das Schlusselwort class verwendet, heisst nicht automatisch, dass man darint Klassen im Sinne Javas oder Small

[MISSING_PAGE_FAIL:285]

Will man nun davon abweichend ein _Call by reference_ haben, dann gibt es zum einen die Moglichkeit, an der Aufruftstelle den Zeigeroperator & zu verwenden, der anstelle einer Koperie des Inhalts der Variable einen Zeiger auf die Speicherstelle der Variable erzeugt und diesen übergibt:

```
1368A*a,b;
1369swap(sa,&b);
```

Dafur mussen dann aber die formalen Parameter so deklariert werden, dass sie Zeiger auf Zeiger aufnehmen können, also etwa wie in

```
1370voidswap(A**a,A**b){
1371A*tmp=*a;
1372*a=*b;
1373*b=tmp;
1374 }
```

Alternativ gibt es in C++ aber die Moglichkeit, wie in Pascal zu verfahren und einfach

```
1375voidswap(A*&a,A*&b){
1376A*tmp=a;
1377a=b;
1378b=tmp;
1379 }
```

zu schreiben, wobei dann die Aufruftstelle unverändert bleiben kann (also ohne & auskommt). Vgl. dazu aber die Bemerkungen in Abschnitt 50.2 zur Praxis in C#.

### Friends

Ein interessantes Konzept von C++, das einen direkten Bezug zur objektorientierten Programmierung hat, ist das Friends-Konzept. In der Praxis kommt es haufig vor, dass ein bestimmtes Teilproblem nicht von einer Klasse allein, sondern nur durch das Zusammenspiel mehrerer Klassen gelost werden kann. Wahrend diese Klassen untereinander eng kooperieren mussen und deswegen (relativ) intime Kenntnis voneinander benotigen (will sagen, auf Elemente zugreifen können mussen, die anderen Klassen verborgen bleiben sollten), gilt das für andere Klassen nicht unbedingt. Die Schnittstelle solcher kooperierenden Klassen sollte also nicht absolut, sondern relativ zu anderen Klassen definierbar sein.

In Java hatte man dazu bis zur Version 8 nur die Moglichkeit, die besag- **ledizierter Export**ten Klassen in ein Paket zu verfrachten und die fraglichen Elemente mit paketweitem Zugriff (also ohne Zugriffsmodifizierer) zu deklarieren (Abschnitt 39.1 in Kurseinheit 4). Das hat jedoch den Nachteil, dass alle Klassen desselben Pakets dieselbe Schnittstelle jeder einzelnen enthaltenen Klasse haben; wenn es eine Klasse gibt, die eine ansonsten unsichtbare Eigenschaft x einer Klasse A sehen und eine andere, die eine Eigenschaft y derselben Klasse sehen soll, dann gibt es keine Aufteilung der Klassen auf Pakete, die genau dieses gestattet. Was man stattdessen gern hatte, ist ein dedizierter Export von Elementen einer Klasse, also ein

[MISSING_PAGE_FAIL:287]

aufzusplitten und nur die zu beerben, deren Eigenschaften man braucht, um sich von unnotigem Ballast freizuhalten.

Mehrfachvererbung ist etwas, das sich Programmiererinnen geme wunschen. Sie bringt jedoch einige praktische Probleme mit sich, unter anderem die Frage, was zu tun ist, wenn eine Klasse von mehreren anderen Klassen verschiedene Definitionen desselben Elements (Feld oder Methode) erbt. Da die Klasse sich dann für eine der beiden Definitionen entscheiden muss, geht die der anderen verloren. Dies kann, insbesondere im Zusammenhang mit _dynamischem Binden_ und _offener Rekursion_, zu unerwartetem Verhalten fuhren. Darüber hinaus fuhrt die Mehrfachvererbung noch zu zahlreichen weiteren Problemen, die hier nicht weiter ausgefuhrt werden sollen.

### Das Typsystem von C++

Das Typsystem von C++ stellt den Versuch dar, objektorientierte Programmierung mit starker Typischerheit unter Beibehaltung der vollen Freiheit der Programmiererin mit moglichst wenig Laufzeit-Overhead zu erzielen. Dazu gibt es eigentlich nur einen Kommentar:

#### Statische Komponente

Wie bereits eingangs enwahnt, wurde bei der Definition von C++ als objektorientierte Erweiterung der Sprache C stark auf Ruckwartskompatibilitat geachtet. Und so findet sich auch das Typsystem Cs vollstandig in C++ wieder. Es gibt also primitive Datentypen wie int, bool etc. und auch die Typkonstruktoren struct (entsprechend dem record Pascals) und union (entsprechend dem varianten Record). Alle diese Typen sind, genau wie die durch Klassen definierten, Typen mit Wertsematik. Es lassen sich aber auch, genau wie in C, Zeigertypen darauf definieren.

Wie in Abschnitt 51.4 diskutiert, erlaubt C++ anders als alle zuvor disku-

\begin{tabular}{c c c c}
1385 & class \textless{Derived} & \textless{Basel}\textgreater{} & \textless{Base2} & \textgreater{} & \textless{} \\ \hline \end{tabular}

Die Mehrfachvererbung wirkt sich naturlich auch auf das Typsysteme aus: Ein von einer Klasse abgeleiteter Typ kann beliebig viele direkte Supertypen haben (namlich einen pro direkte Superklasse). C++ kennt dafur keine Interfaces wie Java oder C#; sie mussen durch rein _abstrakte Klassen_ emuliert werden. Ein Problem ergibt sich dann, wenn verschiedene Supertypen eines Typs dieselbe Eigenschaft ands spezifizieren -- der Subtyp hat dann einen Konflikt, da er nicht den Spezifikationen beider Supertypen dienen kann.

Obwohl die Zuweisungskompatibilitat in C++ wie in Java über die Typ- **dynamisches Binden** konformitat an die Typerveiterung gebunden ist und somit einer Variable eines Typs auch Objekte seiner Subtypen zugewiesen werden können, werden in C++ (wie auch in C#) Methoden zunächst einmal statisch gebunden. Das bedeutet im Klartext, dass auf einem Objekt immer die Methode aufgerufen wird, die in der Klasse definiert ist, deren Typ die Variable (und nicht das Objekt, auf das sie verweist) hat. Der tatsachliche Typ eines Objekts wird also ignoriert, es sei denn, die betreffende Methode wurde mit **virtual79** deklariert.

Bei virtuellen Methoden wird hingegen wie in Java zur Laufzeit gepruft, welchen Typs das Objekt ist, und dann zur entsprechenden Methodenimplementerung verzweigt. Zu diesem Zweck halt das Laufzeitsystem eine sog. _Virtual function table_, in der die zum Objekt passende Implementierung nachgeschlagen werden kann. Diese Indirektion gilt jedoch als teuer (sie bedeutet einen Performanzverlust, den man schon an SMALLtalk immer bennangelt hatte) und soll daher nur wenn unbedingt notwendig durchgefuhrt werden. Folge ist, dass virtual (vor allem von Smalltalk- und Java-Programmiererinnen) gelegentlich vergessen wird und Programme dann nicht wie enwartet funktionieren, oder dass die nachtragliche Erweiterung einer Klasse, auf die eine Programmiererin selbst keinen Einfluss hat, um Subklassen dazu fuhrt, dass die Methoden der Subklasse auf Variablen der alten Klasse nicht aufgerufen werden können. In Java hat man deswegen bewusst davon Abstand genommen (und überlasst die Performanzsteigerung einem optimierenden Compiler); in C# hat man diese Entscheidung nicht nachvollzogen (s. Abschnitt 50.2).

In C++ wird Generizitat mit Hilfe sog. **Templates** erreicht. Wie der Name **Generizitat** schon nahelegt, ist ein Template ein Muster, anhand dessen neue, parameterfose Klassen erzeugt werden können. Im Gegensatz zu Java (und genau wie z. B. in ADA) werden aus Templates tatsachlich neue Klassen erzeugt: Man sagt, dass in C++ Typparameter _expandiert_ werden. Das bedeutet, dass für jede Instanz eines generischen Typs (einer Template) ein neuer Typ tatsachlich erzeugt und kompiliert wird. Man kann sich den Mechanismus wie eine Textverarbeitung vorstellen, die das Template kopiert, alle Vorkommen der Typparameter darin durch tatsachliche Typen ersetzt, das ganze dann mit einem neuen Namen versieht und kompiliert. Tatsachlich wird die Generizitat in C++ als ein Makro-Mechanismus angesehen; ihn umzusetzen ist die Aufgabe des P raprozessors.

Das Typsystem von C++ ist zwar rein statisch, aber nicht strikt: Es erlaubt

**Typumwandlungen** namlich _Typumwandlungen_ (_Type casts_; s. Kapitel 27). Ausdrucke der Form

1386 (<Typ>) <Asdruck>

überzeugen den Compiler davon, dass das Objekt, für das <Ausdruck> steht, vom Typ <Typ> ist und entsprechend verwendet werden kann. Dabei wird nur leider vollkommen ignoriert, welchen Typs das Objekt tatsachlich ist, und ob dieser Typ zuwiesungskompatibel mit <Typ> ist. Anders als in Java oder C# wird die Zulasigkeit dieser Typumwandlung auch nicht zur Laufzeit überpruft, ja sie kann zum Teil nicht einmal überpruft werden (s. Abschnitt 51.5.2) -- wenn sie falsch war, dann hat man halt nicht richtig programmiert. So steht denn auch zu lesen:

_Explicit type conversion is best avoided. Using a cast suppresses the type checking provided by the compiler and will therefore lead to surprises unless the programmer was right._

Margaret A. Ellis und Bjarne Stroustrup

Man spurt die Distanz der Autoren zu dem, was sie da beschreiben. Und so darf es als eine der grossen Errungenschaften Javas gefeiert werden, dass es Type casts wenigstens zur Laufzeit auf Zulasigkeit pruft und damit ein Loch in der Typsicherheit schliebst. Das fuhrt uns zur dynamischen Seite des Typsystems von C++.

#### Dynamische Komponente

Die Beschreibung der dynamischen Typprufung in C++ fallt knapp aus: Es gibt keine.

Nun wissen aber manche Objekte in C++ zumindest im Prinzip, von welcher Klasse sie Instanz sind, und zwar ganz einfach deswegen, weil sie einen Zeiger in die Sprungtabelle ihrer virtuellen Methoden besitzen. Da diese virtuelle Funktionstabelle für alle Objekte einer Klasse dieselbe ist, steht sie gewissermassen für die Klasse. Und so wurde schlieslich C++ doch noch eine Bibliotheksfunktion spendiert, die es erlaubt, für Objekte mit dynamisch gebundenen Methoden herauszufinden, Instanzen welcher Klassen sie sind.80 Diese Information ist unter dem Namen _Runtime Type Information_ (RTTI) bekannt.

Konkret kann die RTTI folgendermassen ausgenutzt werden. Es gibt zu-

**Runtime Type** nachst eine Funktion **typeid**, die man auf einer Referenz aufrufen kann.

**Da die Funktion auf Klassenamen überladen ist und zudem eine Struktur zuruckliefert, auf der == als Gleichheitstest definiert ist, lasst sich der Typ eines Objekts z. B. durch* 1387**typedef(x) == typeid(T) prufen (wobei **x** für eine Variable und **T** für eine Klasse stehen soll). Eine andere nutzliche Funktion, die die RTTI ausnutzt, ist dynamic_cast<T>(x); sie nimmt zwei Parameter, einen Typ (T) und ein Objekt (x), und liefert das Objekt mit dem Typ zuruck, wenn die RTTI dies als typkorrekt erkennt, oder **0** sonst. In Java übersetzt hiesse das:
* 1388**(x instanceof T)? (T) x : null** wobei der Ausdruck <A>? <B> : <C> je nachdem, ob <A> zu wahr oder falsch auswertet, entweder das Ergebnis der Auswertung von <B> oder von <C> zuruckliefert (s. Kapitel 37 in Kurseinheit 4). dynamic_cast<T>(x)entspricht im wesentlichen **x** as T in C# (Abschnitt 50.4.4).

**Selbsttestaufgabe 51.1**

Schlagen Sie ein Verfahren vor, wie man mit Bordmitteln von C++ für Instanzen aller Klassen (und ohne Verwendung von **typeid**) herausfinden kann, Instanzen welcher Klasse sie sind.

### Der ganze Rest

C++ ist eine sehr komplexe Sprache. Sie zu lernen dauert Jahre, selbst bei taglichem Umgang mit ihr; sie zu lehren erscheint fast aussichtslos. Selbst wenn man die zahlreichen Konstrukte der Sprache der Reihe nach durchginge, so ergibt sich die eigentliche Komplexitat erst aus deren kombinierter Verwendung, und die Zahl der Moglichkeiten ist den Gesetzen der Kombinatorik folgend hoch. Entsprechend gro\(\ss\) ist auch die Zahl der Idiome (Wendungen), die es für C++ gibt. Auch wenn langst nicht alle Beitrage zur Komplexitat von C++ in Zusammenhang mit der Objektorientierung stehen, so ist es doch schwierig, sie davon zu trennen. Deshalb soll es an dieser Stelle auch genug damit sein.

## 52 Eiffel

Eiffel nimmt unter den hier behandelten Sprachen eine Sonderstellung ein. Es soll namlich mehrere Dinge auf einmal sein:

* eine Sprache für objektorientierte Analyse und Design,
* eine Sprache für kommerzielle Programmierung und
* eine akademische Lehrsprache.

Das herausragende Merkmal, das Eiffel zu dieser Multifunktion qualifiziert, ist die Integration von Zusicherungen (die Formulierung von Vorbedingungen, Nachbedingungen und Klasseninvarianten), die, als Vertrage zwischendienstanbietenden und dienstnehmenden Klassen interpretiert, erlauben, das Was einer Software zumindest teilweise unabhangig vom Wie zu spezifizieren. Die Typsysteme, die Sie in den vorangegangenen Kapiteln kennengelernt haben und von denen auch Eiffel eines besitzt, erlauben zwar auch schon, Zusicherungen auszudrucken, aber die sind jeweils auf die moglichen Werte einer Variable bezogen und bleiben dabei sowohl voneinander als auch von der Zeit unabhangig. Eiffel erlaubt darüber hinaus, nahezu beliebige Bedingungen für Variablen- und Ruckgabewerte von Methoden auszudrucken, die sowohl auf andere Werte als auch auf den zeitlichen Verlauf (vorher/nachner) Bezug nehmen können.

Eiffel tritt in vielerlei Hinsicht in die Fussstapfen von Pascal: Es ist nicht **akademische** nur syntaktisch ahnlich, sondern ist auch um Sparsamkeit, Klarheit und **Lehrsprache** Orthogonalitat der Konzepte bemuht. Viele Dinge sind in Eiffel ein klein bisschen anders als in anderen Sprachen, weswegen man meinen konnte, es sei aus Prinzip anders; die meisten Abweichungen sind aber wohlbegründet und vermitteln mitunter eine angenehm andere Perspektive auf vertraute Dinge. So ist es eigentlich nur folgerichtig, dass der Erschaffer von Eiffel, Bertrand Meyer, Nachfolger von Niklaus Wirth auf dessen Lehrstuhl an der ETH Zurich wurde.

Es ist mir nicht ganz klar, warum Eiffel kein groBerer Erfolg beschieden ist -- es mag zum einen an der über Jahre absolut unzureichenden Implementierung der Werkzeuge liegen (insbesondere des Compilers -- es wurde anfangs noch nach C übersetzt; man male sich aus, welche Freude man als Programmiererin beim Debuggen hatte) und zum anderen an der Natur Bertrand Meyers, der sich mit seiner Kompromisslosigkeit nicht nur Freundinnen gemacht hat. Eine Rolle spielt sicher auch das unmogliche, aber trotzdem angestrebte Spagat zwischen kommerzieller Einsetzbarkeit und akademischer Eignung -- viele Programmerweisen, die in der Praxis ublich sind und auf die kaum eine Entwicklerin verzichten will, sind akademisch verpont. Das Typsystem Eiffels schliesslich tragt, wie Sie sich in Abschnitt 52.5 selbst vergewissern können, auch nicht unbedingt zur Akzeptanz bei. Auf der anderen Seite hat Eiffel neben Smalltalk noch am ehesten das Format, die Art, wie man über das Programmieren denkt, zu beeinflussen.

### Das Programmiermodell Effells

Eiffel ist, wie alle anderen hier behandelten Sprachen mit Ausnahme von C++, eine rein objektorientierte Programmiersprache in dem Sinne, dass der gesamte Code innerhalb von Klassen angesiedelt ist. Klassen können (mit der in Abschnitt 52.5 gemachten Einschrankung) getrennt übersetzt werden. Dabei basiert die Ausfuhrung von Eiffel nicht auf einer virtuellen Maschine, sondern erfolgt direkt auf der Zielmaschine; allerdings gibt es inzwischen auch ein Eiffel fur.NET, das, wie alle.NET-Sprachen, zunächst in Cll und dann in Maschinencode übersetzt wird. Die Sprache sieht aufgrund ihrer Schlichtheit keine spezielen Konstrukte vor, die der Programmiererin erlauben, zwischen performanten und weniger performanten Implementierungen auszuwahlen -- mogliche Performzgewinne werden ganz einem optimierenden Compiler überlassen. Eiffel verwendet _Garbage collection_ zur Speicherfreigabe.

### 5.2 Klassen als Module

Klassen sind in Eiffel vor allem ein Mittel zur _Datenkapselung (_,Information hiding"_); alle Instanzvariablen oder Felder, in Eiffel Attribute (engl. attributes) genannt, sind privat (weswegen man für sie auch keine Zugriftsmodifikatoren angeben kann). Um dennoch von au-Ben darauf zugerefen zu können, benotigt man in Eiffel (wie in Smalltalk) zwingend Zurgriffsmethoden, die allerdings (wie die Properties in C#) an der Aufruftelle syntaktisch die Form von Variablen annehmen:

1389

rutt also eine Funktion (einen _Setter_) mit dem Parameter **y** auf,

1390

ruft eine auf, die einen (mit y zuweisungskompatiblen) Wert liefert (einen _Getter_). Funktion der Zugriftsmethoden ist es ublicenweise, eine entsprechende Instanzvariable zu setzen bzw. zu lesen; sie können aber auch etwas ganz anderes tun (vgl. dazu auch das Beispiel in Abschnitt 50.3.1). Insbesondere wird es dadurch moglich, den Zugriff auf Instanzvariablen mit Vor- und Nachbedingungen (s. Abschnitt 52.6) zu versehen. Auch bleibt der Programmiererin so die Freiheit, etwas, das wie eine Instanzvariable aussieht, nach aussen anzubieten, ohne sich (dauerhaft) darauf festzulegen, dass es sich dabei auch tatsachlich um eine Instanzvariable handelt (die sog. _Repräsentationsunabhangigkeit_). Aber das hatten wir ja schon bei C# gesehen. Indexer gibt es in Eiffel ubrigens auch.

Die Methoden einer Klasse heissen in Eiffel **Routinen** (routines) und werden logisch in zwei Gruppen unterteilt: **Abfragen** (queries) und **Befehle** (commands). Abfragen geben über den Zustand von Objekten Auskunft, Befehle verändern ihn. Es ist in Eiffel schlechter Stil (aber wird durch die Sprachdefinition nicht verhindert), dass eine Abfrage Seiteneffekte hat, also den Zustand des abgefragten Objekts (des Empfangers) oder eines anderen verändert.

Attribute (Instanzvariablen) und Routinen (Methoden) heissen in Eiffel zusammen Features (entsprechend den Members in von C++ abgeleiteten Sprachen); sie sind in Eiffel die einzigen Elemente einer Klassendefinition. Insbesondere ist es in Eiffel nicht moglich, Klassende-finitionen zu schhateln (es gibt also keine inneren Klassen).

In Eiffel gibt es keine Zugriftsmodifikatoren wie in Java/C#/C++: Wenn **Zugeifbarkeitsregeln** nichts weiter vermerkt wird, ist jedes Feature offentlich zuganglich. Da Attribute jedoch nur über Zugriffsmethoden zuganglich sind, ist der Zustand (im Sinne der Belegung von Instanzvariablen; s. Kurseinheit 1, Kapitel 3) eines Objekts automatisch gekapselt: Man braucht ja schliesslich keine Zugriffsmethoden zu spezifizieren und wenn man es doch tut, dann doch sicher nur, weil die entsprechenden Abfragen und Befehle Teil der Schnittstelle und kein Geheimnis sind.

Nun ware die Definition einer Schnittstelle (der Export von Features) in Eiffel so aber reichlich unspezifisch -- alle Klienten einer Klasse hatten (ubrigens genau wie in Smalltalk) das gleiche Bild von ihr. Das ist für grossere Projekte kaum sinnvoll. Anstatt aber Zugefibarkeit an Pakete zu binden (wie in Java und C#) oder an Freunde (_Friends_, wie in C++), biete Eiffel die Moglichkeit, einzelne Features _dediziert zu veroffentlichen_ (zu exportieren), also unter Nennung der Klassen, die sie sehen können sollen. (Dies schliesst die Nennung der leeren Menge ein, was dann bedeutet, dass keine andere Klasse diese Features sehen kann, also private in anderen Sprachen entspricht). Diese Klassen mussen dann umgekehrt die Features, die ihnen angeboten werden, nicht explizit importieren -- das Wissen ob und der explizite Ausdruck der Abhangigkeit ist also in Eiffel genau invers zu dem der anderen Sprachen. Dabei entspricht der dedizierte Export Eiffels in etwa dem qualifizierten Export Javas, wir er dort allerdings nur für Module und nicht für Klassen definiert ist.

### Anweisungen

Anweisungen sind in Eiffel die Zluweisung, der Methodenaufruf, der Konstruktoraufruf (der Umgang mit Konstruktoren in Eiffel unterscheidet sich erheblich von dem in Smalltalk und auch von dem in Java/C#/C++; es wird hier jedoch nicht weiter darauf eingegangen) sowie die ublichen Kontrollstrukturen zur Verzweigung und der Wiedenholung. Eiffel halt sich dabei strikt an die Regeln der strukturierten Programmierung -- jede Kontrollstruktur hat also genau einen Eingang und einen Ausgang. Das ist in der Praxis naturlich richtig lastig, fuhrt zu argerlich langen Programmen und durfte mit ein Grund für die mangelnde Akzeptanz Eiffels unter professionellen Programmiererinnen sein. Davon unbeschadet bietet Eiffel ein _Exception handling_, das sich angenehm von dem in Java/C#/C++ unterscheidet (es erlaubt insbesondere ein Retry, also ein Wiederholen eines fehlgeschlagenen Versuchs, das in anderen Sprachen durch Codiemuster realisiert werden muss); auf Details von Eiffels Exception handling wird hier jedoch nicht eingegangen, da es nur bedingt etwas mit Objektorientierung zu tun hat.

In Eiffel ist, genau wie in Pascal, das Semikolon Trennzeichen und nicht Teil einer Anweisung; darüber hinaus kann es am Ende einer Zeile auch weggelassen werden. Kleine Eiffel-Programme wirken daher, und aufgrund des Verzichts auf Blocke aüberhalb von Kontrollstrukturen -- es gibt weder {_} noch begin _ end --, optisch aufgeraumt; grosse Programme wirken jedoch schnell aufgelhalt.

### Verebung und überladen

Eiffel erlaubt Mehrfachverebung. Es gestattet zudem sowohl das _überschreiben_ (in Eiffel _Redefinition_ genannt) als auch das Loschen von Methoden. Auf der Haben-Seite steht dabei, dass zu Beginn einer Klassendefinition deklariert werden muss, welche Methoden in der Klasse überschrieben (welche,,Features redefiniert") werden. Naturlich gibt es in Eiffel auch _abstrakte Klassen_; das dazugehorige Schlusselwort heißt jedoch **deferred** anstattabstract, ansonsten ist aber alles wie in Java (richtiger: in Java ist alles wie in Eiffel -- Eiffel ist ca. zehn Jahre alter als Java).

Bertrand Meyer ist ein bekennender Gegner des überladens. Es ist in Eiffel daher nicht erlaubt, dass eine Klasse zwei Methoden besitzt, die gleichnamige heissen. Gleichwohl ist es erlaubt, dass verschiedene Klassen gleichnamige Methoden besitzen -- nur dann durfen diese Klassen nicht in Verebrungsbeziehung zueinander stehen, es sei denn, die Methoden besitzen gleiche oder kovariant redefinierte Parameterstypen, denn dann sind die Methoden nicht überladen, sondern werden überschrieben (was dann allerdings durch eine Redefine-Deklaration anzueigen ist). Nun kann man aber nicht erzwingen, dass zwei Klassen, von denen man erben mochte, keine gleichnamigen Methoden verwenden. Anstatt auf das Erben zu verzichten, ist es in Eiffel deswegen moglich, geerbte Features umzubenennen. Es gibt zu diesem Zweck eine Rename-Klausel, die es erlaubt, zwei geerbte Features gleichen Namens mit unterschiedlichen Benennungen nebeneinander stehen zu lassen. Man beachte, dass das dynamische Binden davon unberuhrt bleibt: über den Typ der Klasse, von der ein umbenanntes Feature geerbt wurde, angesprochen hort das Feature weiterhin auf seinen ursprunglichen Namen.

### Das Typsystem Eiffels

Eiffel besitzt ein einheitliches Typsystem (keine separaten Referenz- und Werttypen) und unterscheidet auch nicht (wie Java) zwischen eingebauten Operatoren und programmiere-rinnendefinierten Methoden: Die Operation + auf Integern beispielsweise ist (wie in Smalltalk) nichts weiter als eine syntaktische Variante einer Methode plus definiert in einer Klasse **INTEGER** mit gleichem Parametertyp (Eiffel verwendet per Konvention für Klassen und Typen vollstandige Grossscheibeung; allerdings ist Eiffel -- wie PASCAL -- nicht case sensitive). Die Einheitlichkeit des Typsystems von Eiffel geht dabei über die von C# insofern hinaus, als es keine an bestimmte Typkonstruktoren gebundene Unterscheidung von Wertund Referenztypen gibt; gleichzeitig unterscheidet es sich aber von dem Smalltalks (das sich ja zumindest dem Anschein nach vollstandig auf Referenztypen festgelegt hat) insofern, als es auch Werttypen zulasst. Mehr dazu gleich.

Zu den prominentesten Eigenschaften des Typsystems von Eiffel Zahlen **wichtige Eigenschaften**

* Mehrfachvererbung,
* Generizitat (genauer: beschrankter parametrischer Polymorphismus; s. Abschnitt 29.4 in Kurseinheit 3),
* das Unterdrucken von Instanzvariablen und Methoden in Subklassen (Loschen von Methoden; s. dazu auch Abschnitt 11.3 in Kurseinheit 1) sowie
* kovariante Redefinition, unterstutzt durch sog. verankerte Typen (engl. anchored types; so gut wie ein Alleinstellungsmerkmal EffELS).

In gewisser Weise kann man das Unterdrucken von Methoden eines Typs in seinen Subtypen in Eiffel als ein Spezialfall der kovarianten Redefinition ansehen, namlich einen, in dem die Menge der moglichen Parameterobjekte auf die leere Menge eingeschrankt wird, so dass es keinen gultigen Aufruf gibt (vgl. Kapitel in Kurseinheit 3). Auch sind die Probleme, die kovariante Redefinition und Unterdruckung verursachen, ahnlich. Deshalb beschranken wir uns bei der Motivation (der Erklarung, warum Eiffel ber diese Eigenschaften verfugt), auf ein Beispiel für kovariante Redefinition.

#### Ein motivierendes Beispiel

Meyers klassisches Beispiel für die Motivation kovarianter Redefinition und verankerter Typen a la Eiffel soll lhnen hier nicht vorenthalten werden -- es wird immer wieder zitiert und ist, abgesehen davon, dass es zu Bemerkungen abseits der Informatik einhaldt, intuitiy gut verstandlich. Das Beispiel beginnt wie folgt:

```
1391class SKTER feature
1392roommate: SKIER;
1393--This skier's roommate
1394share(other: SKIER) is
1395--Choose other as roommate.
1396-
1397do
1398roommate:=other
1399 end
1400--class SKIER
1401end--class SKIER
```

Die Idee ist, dass jugendliche Skifahrerinnen sich zu zweit ein Zimmer teilen. Wie Sie vielleicht schon selbst bemerkt haben, ist der durch die Klasse Skier definierte Typ rekursiv: Seine Instanzvariable roommate ist selbst vom Typ Skier. Somit wird z. B. der folgende Aufruf von share moglich (typkorrekt):

```
1402s1,s2:SKIER
```

Nun ist das Beispiel so noch unvollstandig. Es ergibt sich namlich aus der Sache, dass die jungen Skifahrerinnen nach Geschlechtern getrennt untergebracht werden sollen. Dazu kann man in Eiffel (dank erlaubter kovarianter Redefinition) einfach schreiben:

```
1404class GIRL inherit
1405SKIER
```
1406redefine roommate, share end
1407feature ```
```
1408roommate:GIRL;
14109share(other:GIRL)is -
14111do
1412roommate:=other
1413end
```

[MISSING_PAGE_FAIL:297]

#### 52.5.2 Statische Komponente

Wie auch in Java definiert in Eiffel jede unparametrisierte Klasse einen Typ und jede parametrisierte Klasse eine (generiche) Menge von Typen. Alle Variablen (inkl. Methoden81 und deren Parameter) mussen einen Typ haben. _Zuweisungskompatibilitat_ ist an nominale _Typkonformitat_ gebunden, die wiederum mit der _Typenweiterung_ (in Eiffel einfach _Vererbung_ genannt) einhergeht -- ganz wie in Java. Anders als in Java ist es jedoch zulassig, Instanzuraiablen und Funktionsparameter wie im obigen Beispiel kovariant zu redefinieren -- von kontravarianter Redefinition will Meyer nichts wissen (eine Begrundung sollten Sie mittlerweile selbst zur Verfugung haben). Das bedeutet allerdings mangelnde _Substituierbarkeit_ und bereitet Eiffel erwartungsgemass einige nichttriviale Probleme.

zunächst einmal wollen wir uns das Typsystem Eiffels noch etwas genauer ansehen. Es basiert, wie in der objektorientierten Programmierung **Bedingungen der Typkonformitat** oblich, auf dem Begriff der Typkonformitat (Kapitel 23 in Kurseinheit 3). In Eiffel ist ein Typ U typkonform zu einem Typ T

* wenn U und T gleich sind,
* wenn U eine direkte Erweiterung von T ist (direkt von T erbt) und wenn zusatzlich, im Falle von parametrischer Erzeugung von U und T, jeder tatsachliche Typparameter von U konform ist zum entsprechenden tatsachlichen Typparameter von T oder
* wenn es einen Typ V gibt, so dass U typkonform mit V und V typkonform mit T ist (U ist eine indirekte Erweiterung von T).

Außerdem gibt es in Eiffel noch einen Typkonstruktor like <ein Ausdruck> (s. u.), dessen erzeugter Typ typkonform zum Typ von <ein Ausdruck> ist. Dieser spielt bei der kovarianten Redefinition eine wichtige Rolle. Zu einem so erzeugten Typ ist jedoch nur der Basistyp konform, keiner seiner Subtypen.

Dazu zunächst ein paar Beispiele. Bei

1429class B inheritA=

1430a: A

1431b: B

1432a:= b

OK,

1433b:=a* [1434]**class GSub[B] inherit class GSuper[B]**
* [1435]**x**: : GSub[integer]
* [1436]**y**: : GSuper[integer]

ist wieder

* [1437]**y**:= x

zuweisungskompatibel, die umgekehrte Zuweisung jedoch nicht. Beschrankter parametrischer Polymorphismus wird in Eiffel ubrigens wie folgt notiert:

* [1438]**class SortedList[G -> Comparable]**

Eiffel benutzt also eckige Klammem und -> anstelle von spitzen Klammern und **extends** in JAVA.

In Eiffel wird ubrigens anders als in C# nicht pro Typkonstruktor zwischen Wert- und Referenztyp unterschieden -- zu jedem kann es (ahnlich wie

**Referenz- und** in C++) beide Formen geben. Dazu gibt es in Eiffel die Moglichkeit, bei

einer Deklaration anzugeben, dass Variablen eines Typs Wertsemantik, also ein Objekt anstelle einer Referenz auf ein Objekt zum Inhalt haben sollen (s. Kurseinheit 1, Abschnitt 1.5). Dies ist manchmal für alle Variablen eines Typs sinnvoll (z. B. bei Zahlen und Wahrheitswerten), manchmal aber auch nur für manche. Und so gibt es in Eiffel einen Typkonstruktor

**expanded**, der, in Variablendeklaration wie in

* [1439]**x**: : expanded C**

eingesetzt, einer einzelnen Variable eine Wertsemantik gibt, und der in Klassendefinitionen

* [1440]**expanded class C _**

verwendet allen Variablen des entsprechenden Typs (der entsprechenden Typen im Falle einer generischen Typdefinition) automatisch Wertsemantik gibt. Eiffels Typkonstruktor

**expanded**entspricht also gewissermanessen einer Umkehrung des in Pascal-artigen Sprachen

verwendeten Typkonstruktors \({}^{\mathbf{\Lambda}}\) (Zeiger auf): Wenn **expanded**_nicht_ verwendet wird, handelt es sich um einen Zeigertypen.

Die Unterscheidung von Wert- und Referenztypen einer Klasse hat in Erfell einen starken konzeptuellen Hintergrund: Sie unterstutzt die bereits in Abschnitt 2.3 diskutierte Komposition und ihre Abgrenzung als eine besondere Beziehung zwischen Objekten, namlich der, die das Enthaltensein von Objekten in anderen ausdruckt (vgl. dazu auch Kapitel 59 in Kurseinheit 6). Nun ist es in der Realtat so, dass nicht alle Instanzen einer Klasse immerentweder Komponenten (also in anderen Objekten enthalten) oder freie Objekte (also nirgends enthalten) sind. Eiffel wird dem gerecht, indem es erlaubt, von einer Klasse fallweise Komponentenobjekte (über **expanded** Variablen) und freie Objekte (über normale Variablen) zu haben. Dieses Feature ist nicht in C# (zumindest nicht im Safe mode) zu haben, denn dort definieren Strucks ausschlieflich Werttypen und Klassen ausschlieflich Referenztypen, und schon gar nicht in Smalltalk oder Java -- in C++ (und im Unsafe mode von C#) kann man es simulieren, zahlt dafur aber den Preis, mit expliziten Pointer hantieren zu mussen, was nach landlaufiger Auffassung ein ziemlich hoher ist.

Nun stand bereits in Kurseinheit 1, Abschnitt 1.6 zu lesen, dass bei der Zuweisung zwischen zwseichen zwei Variablen mit Wertsemantik der Wert der einen

Variable in die andere Variable kopiert wird, wahrend bei der Zuweisung

zwischen zwei Variablen mit Referenzsemantik lediglich der Zeiger kopiert wird. Dies ist auch in Eiffel so. Bei der Zuweisung einer Variable mit Referenzsemantik an eine Variable mit Wertsemantik reicht es jedoch nicht, einen Zeiger zu kopieren, denn die Zielvariable hat keinen Platz für einen Zeiger, sondern für die Attributwerte -- stattdessen wird hier das Objekt, auf das der Zeiger verweist, kopiert (genauer: es werden die Attribute des Objekt s in den für die Attribute des Werts reservierten Speicher der Variable kopiert). Im umgekehrten Fall, also wenn eine Variable mit Wertsemantik an eine Variable mit Referenzsemantik zugewiesen wird, konnte man annehmen, dass ein Zeiger auf den Wert erzeugt und zugewiesen wird; dies wurde aber bedeuten, dass dadurch ein _Alias_ auf einen Wert entstunde, was nicht der Semantik der Komposition (_Aggregation_; s. Abschnitt 2.3 in Kurseinheit 1) entsprache. Was stattessen passiert, ist, dass ein Klon des Objekts erzeugt wird und eine Referenz auf diesen Klon übergeben wird. Dies ist eine aüberst sinnvolle Festlegung.

**Verankerte Typdeklarationen** haben in Eiffel die Form

**verankerte Typen**

1441 x : like y

wobei **y** ein bereits typisiertes Programmelement (also z. B. eine Instanzvariable) ist. Eine solche Verankerung bewirkt, dass sich der Typ von **x** automatisch mit dem von **y** verändert. Dies hat zunächst noch nichts mitt Kovarianz zu tun, wie das folgende Beispiel zeigt.

Anstatt in Eiffel

1442 class A

1443 feature

1444 f : X

1445 setF(v : X)

1446 getF() : X

1447 end

1448 --

1449 end

1450 class B

1451 inherit A

1452 redefine f * 1453 feature f : Y
* 1455 setF(v : Y)
* 1456 getF() : Y
* 1457 end
* 1458 --
* 1459end ```
zu schreiben, d. h., bei Veränderung des Typs der Instanzvariable **f** von **X** zu Y alle Parametertypen, die davon beruhrt sind, mit zu verändern, reicht es aus,
```
1460class A
1461feature f : X
1463setF(v : like f)
1464getF() : like f
1465 end
1466 --
1467end ```
```
1468class B
1469inherit A
1470redefine f
1471feature f : Y
1473end --
1474 --
1475end
```

zu schreiben. Da die Typen der Parameter von **setF** und **getF** alle per Deklaration dieselben sind wie der Typ von **f**, muss in der Definition von **B** textuell nichts anderes stehen. Da nun aber in Eiffel die Redefinition von Instanzvariablen per Definition immer kovariant sein muss, muss Y ein Subtyp von **X** sein. Der Ruckgabetyp von **getF** und der Parametertyp von **setF** andern sich damit automatisch ebenfalls kovariant.

Ein besonderer Fall von verankerten Typen ergibt sich bei rekursiven Typen, also Typen, deren Definition den definierten Typ selbst referenziert:

In diesem Fall schreibt man in Eiffel anstelle der Typreferenz bei der Deklaration einer Variable vom zu definierenden Typ **like** Current. Bei einem entsprechend deklarierten Feld andert sich der Typ bei der Verebrung also immer automatisch zum erbenden Typ hin ab, also immer mit dem Typ und damit kovariant. für das Beispiel der zu trennenden Skifahrerinen (Zeilen 1391-1425) ergibt sich damit

```
1476class SKTER feature
1477roommate: like Current;
1478share(other: like Current) is
1479 --
1480do
1481roommate:=other
1482end --
1483 --
1484end -- class SKTERDie beiden erbenden Klassen GIRL und BOY mussen dann nichts mehr redefinieren.

Wir können nun zur Losung des Problems der Kovarianz in Eiffel kommen. Die obige Konstruktion

\begin{tabular}{c c}
1485 & **s1 : SKTER; b1 : BOY; g1 : GIRL** \\
1486 & **s1 := b1;** \\
1487 & **s1. share(g1)** \\ \end{tabular} (hier unverändert wiederholt) wird dann vom Type checker zur übersetzungszeit zuruckgewiesen, da g1 nicht vom Typ like s1 ist, was aber laut Typkonformitatsregeln von Eiffel notwendig ware. Leider ist das nur ein Teilerfolg.

Es ist namlich andersherum like s1 mit dem Typ von s1 konform. Und so wird es moglich, dass bei zusatzlicher Deklaration von

\begin{tabular}{c c}
1488 & **g2 : like s1** \\ \end{tabular} (wobei der Typ von s1 ja SKTER ist)

\begin{tabular}{c c}
1489 & **s1 := g1; g2 := s1** \\ \end{tabular} (s1)

und anschließend

\begin{tabular}{c c}
1491 & **s1 := b1** \\ \end{tabular}

\begin{tabular}{c c}
1491 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1485 & **s1 : SKTER; b1 : BOY; g1 : GIRL** \\
1486 & **s1 := b1;** \\
1487 & **s1. share(g1)** \\ \end{tabular} (hier unverändert wiederholt) wird dann vom Type checker zur übersetzungszeit zuruckgewiesen, da g1 nicht vom Typ like s1 ist, was aber laut Typkonformitatsregeln von Eiffel notwendig ware. Leider ist das nur ein Teilerfolg.

Es ist namlich andersherum like s1 mit dem Typ von s1 konform. Und so wird es moglich, dass bei zusatzlicher Deklaration von

\begin{tabular}{c c}
1488 & **g2 : like s1** \\ \end{tabular} (wobei der Typ von s1 ja SKTER ist)

\begin{tabular}{c c}
1489 & **s1 := g1; g2 := s1** \\ \end{tabular} (s1)

und anschließend

\begin{tabular}{c c}
1498 & **s1 := b1** \\ \end{tabular}

\begin{tabular}{c c}
1491 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1492 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1493 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1491 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1492 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1493 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1494 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1495 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1496 & **s1 : share(g1)** \\ \end{tabular}

\begin{tabular}{c c}
1497 & **s1 : share(g1)** \\ \end{tabular}

\begin{tabular}{c c}
1498 & **s1 := g1; g2 := s1** \\ \end{tabular}

\begin{tabular}{c c}
14998 & **s1 := g1; g2 := s1** \\ \end{tabular}

\begin{tabular}{c c}
14998 & **s1 := b1** \\ \end{tabular}

\begin{tabular}{c c}
1491 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1491 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1492 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1493 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1491 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1491 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1492 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1493 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1491 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1493 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1494 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1495 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1496 & **s1 : share(g1)** \\ \end{tabular}

\begin{tabular}{c c}
1497 & **s1 : share(g1)** \\ \end{tabular}

\begin{tabular}{c c}
1498 & **s1 : share(g1)** \\ \end{tabular}

\begin{tabular}{c c}
14998 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1491 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1491 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1492 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1493 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1491 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1491 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1492 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1493 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1494 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1495 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1496 & **s1 : share(g1)** \\ \end{tabular}

\begin{tabular}{c c}
1497 & **s1 : share(g1)** \\ \end{tabular}

\begin{tabular}{c c}
1498 & **s1 : share(g1)** \\ \end{tabular}

\begin{tabular}{c c}
14998 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
14991 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1491 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1491 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1492 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1493 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1491 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1493 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1494 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1495 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1496 & **s1 : share(g1)** \\ \end{tabular}

\begin{tabular}{c c}
1497 & **s1 : share(g1)** \\ \end{tabular}

\begin{tabular}{c c}
1498 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1498 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
14998 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
14998 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1491 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1491 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1491 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1492 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1493 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1493 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1491 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1493 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1495 & **s1 : share(g2)** \\ \end{tabular}

\begin{tabular}{c c}
1496 & **s1 : share(g2)** \\ \Die zweite Moglichkeit ware, eine Typinferenz für das gesamte Programm durchzufuhren, um die moglichen Zuweisungen an Variablen zu sammeln. Dazu sind insbesondere alle Methodenaufrufe anzusehen (Zuweisungen an Instanzvariablen sind in Eiffel nur innerhalb einer Klasse erlaubt) und diese können je nach Konfiguration des endgultigen Systems sehr unterschiedlich ausfallen. Eine solche Typinferenz ist aber in den meisten Fallen unrealistisch.

Die dritte Moglichkeit ist die, alle dynamisch gebundenen Aufrufe von Methoden, deren Verfugbarkeit oder Parametertypen sich in überschriebenen Versionen (,,Redefinitionen") andern (die von Meyer so genannten CAT-Calls, wobei CAT fur,,Change Availability or Type" steht), zu verbieten. Ein Aufruf von **share** auf **s1** wie oben ist damit verbboten, weil **share** in BOY und **GIRL** kovariant redefiniert wird. Auf einer Variable vom Typ GIRL oder **BOY** ware er hingegen zulassig, solange sichergestellt ist, dass diese Variable keinen Wert von einem Subtyp von **GIRL** bzw. **BOY** zugewiesen bekommen kann. Das ist moglich, wenn kein solcher Subtyp existiert oder wenn keine Zuweisung an die Variable existiert, bei der die rechte Seite ein Subtyp der Variable ist. Das erste ist lokal nicht nachzuweisen, das zweite hingegen schon, jedoch nur \(k\) _explizite Zuweisungen_ (inkl. der Instanzierung, die in Eiffel auf einer Variable durchgefuhrt wird und ihr automatisch einen Wert gibt). für die Zuweisung an formale Parameter kann dies jedoch nicht lokal nachgewiesen werden, weil im Gegensatz zu expliziten Zuweisungen an Variablen die Methodenaufrufe von überall her erfolgen können.

Wie Sie sehen, sind die Bedingungen ziemlich restriktiv, und man kommt nicht unhin, das Typsystem von Eiffel als etwas eigenartig zu empfinden. Wie es sich in der Pravis auswirkt, ist mir leider nicht bekannt; Meyer behauptet, dass die Probleme praktisch keine Rolle spielen. Ich mochte hinzufugen, dass falls doch, die durchschnittliche Programmiererin kaum verstehen wird, was denn nun genau das Problem ist und was sie tun kann, es zu umgehen.

#### Die dynamische Komponente

Bei allen Bemuhungen, für Eiffel ein moglichst,,wasserdichtes" Typsystem vorzulegen und dabei so viel wie moglich zur Obersetzungszeit zu erledigen, bleibt es naturlich auch in Eiffel-Programmen nicht aus, dass man in einen Container (eine Variable oder eine Collection) Elemente ungleichen Typs hineinpackt und hinterher wissen will, welchen genauen Typs ein Element ist, um es seinem Typ entsprechend verwenden zu können. Nicht immer wird man die dazu notwendige _Fallunterscheidung_ dem dynamischen Binden (einem dynamisch gebundenen Methodenaufruft) überlassen wollen; manchmal ist es einfach einfach einfacher (und besser nachvollziehbar), wenn man den Typ explizit pruft und innerhalb einer Methode entsprechend verzweigt.

Solche Typtests werden in Eiffel von einem sog. _Zuweisungsversuch_ (engl.

\begin{tabular}{c c}  & **Typtests und** \\  & **Typumwandlungen** \\  & **Typumwandlungen** \\  & **Pergibt nie einen Typfehler, sondern fuhrt hochstens dazu, dass a void zugewiesen wird. Es bleibt dann die Aufgabe der Programmiererin, a nach der Zuweisung zu kontrollieren. Es entspricht dies direkt dem as aus C#, dem dynamic_cast<T>(x) aus C++ sowie dem Java-Konstrukt

1493if(binstanceofA)a=(A)b;elsea=null;oder auch kryptischer

1494a=(binstanceofA)?(A)b:null;wobeiAderTypvonasei(manbeachtedasargerliche, aber in C-artigen Sprachen notwendige SemikolonvordemElse). Explizite Type casts gibt es in Eiffel nicht; sie können also auch keine Laufzeitfehler verursachen. Der Zuweisungsversuch erfullt aber weitgehend die Funktion einer Typumwandlung, denn er ist nur erfolgreich, wenn die rechte Seite zuweisungskompatibel mit der linken ist, was per Definition nur dann der Fall ist, wenn die rechte Seite ein Objekt eines Subtypes (einschlie@lich Gleichheit) der linken Seite hat. Es wird hier allerdings die Typumwandlung immer mit einer Zuweisung verbunden; man braucht also u. U. eine temporare Variable, die man sich sonst hatte sparen können. Dass der Zuweisungsversuch in Eiffel anders als der Down cast in Java keinen Laufzeitfehler verursachen kann, ist wenig trostlich, denn der Wert **void** in einer Variable kann es naturlich schon; in Wirklichkeit wird hier lediglich ein Type cast error gegen eine Null pointer exception getauscht.

Die Typumwandlung wird in Eiffel aber auch noch für etwas anderes gbraucht, namlich für das Binden von Aufrufen kovariant redefinierter Methoden. Da Eiffel ja, wie oben beschrieben, polymorphe CAT-Calls verbieten muss, diese aber gleichwohl notwendig sein können, hat man nur die Moglichkeit, die dynamische Bindung programmatisch zumulieren. Und dafur braucht man Zuweisungsversuche, wie folgendes Beispiel zeigt:

14959:GTRL;b:BOY

14969?=s1;1497if9/=Voidthen

1498g.share(_

1499endelse

1500b?=s1;1501ifb/=Voidthen

1502b.share(_

1503end

1504end

Nun ja.

### Zusicherungen in Eiffel: Vorbedingungen, Nachbedingungen und Klasseninvarianten

Praktisch ein Alleinstellungsmerkmal Effels ist die Integration von Zusicherungen in Form von Vor- und Nachbedingungen bei Methodenaufrufen. Bei der Behandlung JAVas war uns ja schon die Assert-Anweisung begegnet, die es erlaubte, Zusicherungen zur Laufzeit auszuwerten und das Programm ggf., bei einer Verletzung, abzubrechen. Da es sich aber um eine Anweisung handelte, gab es keine von der Sprachdefinition vorgesehenen Orte, an denen solche Zusicherungen auftreten sollten -- sie an passenden Stellen einzustreuen war ganz der Programmiererin überlassen. In Eiffel ist das anders.

Eiffels Syntax zur Definition einer Methode sieht zwei Schlusselworter, require und ensure, vor, von denen das erste vor der Definition der Implementierung der Methode (dem Methoderumpft), das zweite dannach auftreten kann. Beiden Schlusselwortern folgen können Boolesche Ausdrucke, die allesamt zu,,wahr" auswerten mussen. Die Idee hinter einer Require-Klausel ist, dass, damit die betreffende Methode richtig funktionieren kann, die darin ausgedruckten Bedingungen erfullt sein mussen. So ist es beispielsweise sinnvoll, für die Methode pop der Klasse STACK zu verlangen, dass der betreffende Stack, auf dem die Methode aufgerufen wird, nicht leer ist. Die Idee hinter einer Ensure-Klausel ist, dass eine Methode, deren Require-Klausel erfullt war, im Gegenzug garantieren muss, dass sie die in der Ensure-Klausel ausgedruckten Bedingungen erfullt. Im Beispiel des Stacks ware das beispielsweise, dass nach einem push das übergebene Element auch tatsachlich oben auf dem Stapel liegt, die Methode top also beispielsweise das soeben auf den Stapel gelegte Element liefert. Um ihre Bedingungen zu formulieren, durfen die Ausdrucke in beiden Klauseln auf Abfragen (queries) der Klasse zuruckgreifen. Diese sollten dazu aber tunlichst nebeneffektfrei sein, zum einen, weil die Ensure-Klausel sonst nicht garantieren kann, dass eine geprutfe Bedingung auch nach ihrer vollstandigen Abarbeitung immer noch wahr ist (man bedenke nur, was ware, wenn die Ensure-Klausel zu push die Methode pop aufrufen wurdel), zum anderen aber auch, weil auch in Eiffel (wie in JAVA) die überprufung der Zusicherungen zur Laufzeit abgestellt werden kann (weswegen dann das Programm mit überprufung der Zusicherungen eine andere Semantik hatte als ohne; vgl. die Anmerkungen zu JAVas Assert-Anweisung in Kurseinheit 4, Kapitel 38).

Neben der Moglichkeit, Vor- und Nachbedingungen zu formulieren, gibt **Klasseninvarianten**es in Eiffel noch die Moglichkeit, sog. Klasseninvarianten (Schlusselwort **invariant**) zu deklarieren. Klasseninvarianten mussen jederzeit zwischen zwei Methodenaufrufen gelten; man kann sich vorstellen, dass sie jeder Vor- und Nachbedingung per Konjunktion hinzugefugt werden. Auf die etwas subtilen Probleme, die das Aliasing in Zusammenhang mit Zusicherungen schafft, wollen wir an dieser Stelle nicht eingehen; Kurs 01853 befasst sich ausführlicher damit.

Zusicherungen werden in Eiffel von Klassen auf ihre Subklassen vererbt. **Zusicherungen und**Wenn dabei eine Methode redefiniert wird, dann durfen auch Vor- und

[MISSING_PAGE_FAIL:306]

Losungen zu den Selbsttestaufgaben

Die Regel für die Zuweisungskompatibilitat an der Aufrufstelle, also die Zuweisung des tatsachlichen an den formalen Parameter, muss auf Typaquivalenz eingeschrankt werden, da sonst (im Rumpf der aufgerufenen Methode) dem tatsachlichen Parameter ein Wert eines Supertps des Typs des tatsachlichen Parameters zugeweisen werden kann. Praktisch heißt das für C#, dass der tatsachliche und der formale Parameter vom gleichen Typ sein mussen.

**Selbsttestaufgabe 51.1 (Seite 276)**

Man deklariert eine virtuelle Methode getClass() in einer abstrakten Klasse (nennen wir sie Object), lasst jede Klasse, die die Funktionalitat haben soll, von dieser Klasse ableiten und oberschreibt getClass() in diesen Klassen mit der Ruckgabe der jeweiligen Klasse bzw. eines Reprasentanten der Klasse.

**Selbsttestaufgabe 52.1 (Seite 291)**

Die Konjunktion (logische Und-Verknopfung) einer Bedingung mit einer beliebigen anderen entspricht einer Verscharfung der Bedingung (sie ist in weniger Fallen wahr), die Disjunktion (logische Oder-Verknopfung) einer Aufweichung (sie ist in mehr Fallen wahr).

Typinvarianten sind spezielle, Variablenwerte betreffende Zusicherungen. Typinvarianten auf Einga-beparametem entsprechen Vorbedingungen, solche auf Ausgabeparameterem (dazu zahlt der Ruckgabeparameter) entsprechen Nachbedingungen. Die Aufweichung der Vorbedingungen in Subklassen entspricht der Kontravarianz von Eingabeparameter, die Verscharfung der Nachbedingungen der Kovarianz der Ergebnistypen.

Bemerkenswerterweise verlangt Eiffel bei den Vorbedingungen Kontravarianz, bei den Eingabeparametern jedoch Kovarianz.

Kurseinheit 6: Probleme der objektorientierten Programmierung

In den vorangegangenen Kurseinheiten wurde bereits an verschiedenen Stellen auf Probleme der objektorientierten Programmierung hingewiesen. Diese sollen nun in dieser Kurseinheit zusammengefasst dargestellt werden.

## 54 Das Problem der Substituierbarkeit

In Kapitel 26 sind wir ja schon ausführlicher auf den Begriff des _Subtyping_ eingegangen. Das Subtyping sollte _Zuwesiungskompatibilitat_ zwischen verschiedenen Typen gestatten, also erlauben, dass Objekte eines Typs Variablen eines anderen Typs, namlich eines Supertps, zugewiesen werden. Das fuhrt nun zu dem Problem, dass man -- aufgrund des _dynamischen Bindens_ von Methodenaufrufen -- bei Vorliegen des Programmfragments

```
15071e<T>
1508e:=<ein Ausdruck>.
1509e mselbst bei Kenntnis des Typs T nicht sagen kann, welchen Effekt der Aufruf von Methode m in Zeile 1509 hat.82 Nach den Regeln gangiger objektorientierer Programmiersprachen zur Zuweisungskompatibilitat weiss man lediglich, dass es sich beim Typ des Empfangerobjekts e um einen Subtyp von T handen muss83 -- man weiss aber nicht, um welchen. Bei statischer, lokaler Betrachtung84, also bei mangelnder Kenntnis des Typs des von e bezeichneten Objekts sowie aller infrage kommenden Subtypen von T, tappt man hier vollkommen im Dunkeln. Da die Erweiterung um Subklassen bzw. Subtypen aber gerade eine der Errunenschaften der objektorientierten Programmierung ist, hat man es dabei mit einem echten Problem zu tun.
```

Das Problem lasst sich als ein Problem der formalen Programmverifikation ausdrucken: Wie lasst sichalso dass bei Vorliegen der Bedingung \(P\) vor Ausfuhrung des Methodenaufrufs **e** **m** nach dessen Ausfuhrung die Bedingung \(Q\) eingehalten wird, beweisen? Ein solcher Beweis verlangt immerhin genaue Kenntnis davon, was der Methodenaufruft tut, oder vielmehr, welchen Effekt dieses Tun hat. Dazu muss man aber die Implementierung der Methode kennen.

Umgekehrt ist es für die Pflege und Weiterentwicklung eines Programms wichtig zu wissen, welchen Bedingungen die Methoden einer in ein Programm neu eingefuhrten Klasse genugen mussen, damit das Programm auch hinterher noch funktioniert. Wenn die neue Implementierung sich in den Kanon der bereits bestehenden einordnet, ohne ein unwartetes Verhalten einzubringen, wenn sie also für alle Aufrufe gemachte Zusicherungen der Form von (54.1) einhalt, dann ist das Funktionieren nicht gefahrdet -- andernfalls hingegen schon. Nur um das zu garantieren, mussen die Bedingungen bekannt sein.

Es stellt sich also die Frage, wie man den Effekt aller Implementierungen von **m** für Subtypen von **T** (einschlie@lich T selbst) fassen kann. Eine naive Beantwortung der Frage wurde vorschlagen, dass man sich alle diese Implementierungen anseint und auf dieser Basis eine _Fallunterscheidung_ prasentiert: Wenn das Objekt **e** vom **T** ist, dann hat **m** den und den Effekt usw. Die Zusammenfassung dieser Fallunterscheidungen wurde dann alle Effekte mit logisch Oder verknupfen. Diese Moglichkeit hat jedoch neben ihrer unnotigen Sperrigkeit den Nachteil, dass dabei noch gar nicht vorhandene Implementierungen unberuckschtigt bleiben mussen. Was man stattessen mochte, ist die Gewissheit, dass eine lokale,,,modulare" Betrachtung ausreich und man nicht jedes Mal eine Analyse des gesamten Programms durchfuhren muss, um zu entschlusseln, was ein Methodenaufruf bewirken konnte. Genau dies soll der Begriff der Substituierbarkeit bringen.

### Der Begriff der Substituierbarkeit

Zuweisungskompatibilitat zwischen verschiedenen Typen bedeutet, dass Objekte eines Typs da auftreten durfen, wo Objekte eines anderen Typs erwartet werden. Wenn das gutgeht, also wenn durch eine entsprechende Zuweisungskompatibilitat keine Fehler entstehen, spricht man von der **Substituierbarkeit** der Objekte des Typen auf der linken Seite der Zuweisung durch die des Typen auf der rechten.

Nun ist die Frage, ob eine Zuweisung gutgeht, eine, die man gern automatisch, am besten durch den Compiler, beantwortet hatte. Der Begriff der Substituierbarkeit ist daher in der Programmierung zu einem eigenstandigen geworden, der zunächst unabhangig von der (an _Typkonformitat_ gebundenen) Zuweisungskompatibilitat betrachtet werden kann. Der Begriff der Substituierbarkeit soll daher zunächst einmal genauer untersucht werden.

In der strengsten Auslegung des Begriffs der Substtuierbarkeit kann ein Objekt ein anderes nur dann substituieren, wenn sich das auf den Programmablauf in keiner Weise auswirkt. Dazu musste das ersetzende Objekt aber nicht nur gleich implementiert sein wie das ersetzte (also Instanz derselben Klasse85 sein), sondern sich auch noch (zum Zeitpunkt der Substituerung) im selben Zustand wie das substituierte befinden. Wenn namlich beispielsweise eine Instanz der Klasse Stack gerade leer ist, ist sie nicht grundsatzlich gegen eine, die gerade nicht leer ist, austauschbar: Eine Operation **pop**, die das oberste Element des Stacks liefern soll, wurde im einen Fall scheitem, im anderen Fall nicht. Da sich Objekte aber nicht abnutzen (so dass sie aus Wartungsfunden substituiert werden mussten), gibt es wohl kaum einen Grund für eine Substituerung sich identisch verhaltender Objekte und damit auch nicht für einen entsprechend eing gefassten Substituierbarkeitsbegriff.

Der Substituierbarkeitsbegriff muss also zumindest vom konkreten Zustand der Objekte unabhangig sein. Das hat den Vorteil, dass man die Betrachtung von Substituierbarkeit von der Laufzeit auf die übersetzungs- (oder Entwurfs-)Zeit verlagern kann. Auf dieser Ebene ist aber zumindest das Verhalten aller Objekte einer Klasse gleich (namlich durch dieselbe Klassendefinition) spezifiziert, so dass eine gegenseitige Substituierbarkeit von Objekten derselben Klasse automatisch gegeben ist.

Interessant wird die Frage der Substituierbarkeit erst, wenn die Objekte nicht derselben Klasse angehoren und wenn man eine gewisse Abweichung im Verhalten von zu substituierenden Objekten zulasst. So konnte man sich beispielsweise vorstellen, dass ein substituierendes Objekt funktional aquivalentt ist (also das Gleiche tut), aber auf eine andere Art. Es konnte z. B. seinen Dienst schneller verrichten als das substituierte oder mit weniger Speicheranforderungen. Diese sog. _nichtfunktionalen Anforderungen_, die normalerweise von den _funktionalen_ getrennt dargestellt werden, sind aber in Wirlichkeit gar nicht immer hundertprozentig davon zu trennen und es ist durchaus vorstellbar, dass ein Programm, das von einem funktionien-renden nur in nicht-funktionalen Eigenschaften abweicht, nicht funktioniert (beispielsweise weil bestimmte angenommene Echtzeitbedingungen nicht eingehalten werden und dies zu Abbruchen durch Time outs o. a. fuhrt).

Ein klassisches Beispiel für die gegenseitige Austauschbarkeit funktional aquivalenter, aber verschiedener Typen ist die plattformunabhangige

**Programmierung** GUI-Programmierung. So basiert beispielsweise die GUI-Programmierung von und mit E-CLIPSE auf einer Reihe von Typen, deren Objekte für die Elemente eines GUI stehen, also Fenster, Buttons etc. Nun hat jedes Betriebssystem seine eigenen, den jeweiligen Eigenheiten angepassten Implementierungen dieser GUI-Elemente. Es ist also sinnvoll, für jeden Typvon GUI-Element eine Reihe von Subtyppen, einen pro Betriebssystem, anzubieten, die die Elemente auf die jeweiligen Implementierungen des Betriebssystems abilden. Objekte dieser Typen sind innerhalb derselben Gruppe (also als Objekte von Subtypen desselben Typs) funktional aquivalent, können sich aber in Aussehen und ggf. auch Detailverhalten (gegenüber dem Bediener) unterscheiden. Diese Unterschiede sind jedoch gewollt und die Substituierbarkeit bleibt davon unberuhrt.

Aber auch damit ist noch nicht Schluss mit der Auslegung des Begriffs von der Substituierbarkeit. Es ist z. B. denkbar, dass unterschiedliches Verhalten nicht nur toleriert, sondern sogar gewunscht wird. Denken Sie beispielsweise an einen Editor, der eine Funktion _,ruckgangig machen" hat, die es erlaubt, den Effekt der letzten Aktion, die Sie ausgefuhrt haben, zuruckzunehmen, und zwar unabhangig davon, welche Aktion dies war. Die Aktionen, die moglich sind, sind in der Regel hochst unterschiedlich, so dass es keinen einheitlichen Mechanismus gibt, der erlauben wurde, jeden Effekt auf die gleiche Weise ruckgangig zu machen. Es ist also sinnvoll, Aktionen als Objekte zu reprasentieren, die neben einer Funktion _,ausfuhren" auch noch eine _,Ruckgangigmachen" haben, die, für jeden Typ von Aktion verschieden, das jeweils Notwendige verrichtet. Objekte all dieser Aktionstypen waren dann, was den Tatbestand der Ausfuhr- und Ruckgangigmachbarkeit angeth, gegeneinander austauschbar und die Aktionstypen waren alle Subtypen eines allgemeinen (abstrakten) Typen **Aktion**, obwohl ihr konkretes Verhalten, also das, was jeweils mit _,ausfuhren" und _,ruckgangig machen" verbunden ist, jeweils hochst unterschiedlich ausfallt. Die Anforderungen an die Substituierbarkeit sind in diesem Fall also eher gering.

Im allgemeinen als nicht gegeneinander austauschbar angesehen wird jedoch Verhalten, bei dem eine Funktion, die in dem auszutauschenden Typ schlicht fehlt. So ware beispielsweise eine Aktion, für die _,ruckgangig machen" nicht definiert ist (z. B. **Speichern**), kein Subtyp von **Aktion**, da Objekte dieses Typs nicht überall da auftauchen können, wo allgemein Aktionenen ewartet werden. Es ist diskutierbar, ob es ausreicht, die Funktion _,ruckgangig machen" in **Speichern** leer zu implementieren, also beispielsweise nichts passieren zu lassen oder eine Meldung _,ruckgangig Machen leider nicht moglich" auszugeben; die Benutzerin ist vermutlich zerknittert, aber das Programm wurde immerhin weiterlaufen. Die formale Spezifikation, namlich die Aktion (das Speichern) ruckgangig zu machen, wurde freilich nicht erfullt; Objekte vom Typ **Speichern** sind damit strenggenommen nicht gegen andere Objekte vom Typ **Aktion** austauschbar.

### Subtyping und das Prinzip der Substituierbarkeit

Das Beispiel von **Aktion** und **Speichern** legte bereits nahe, dass die Substituierbarkeit immer dann fraglich ist, wenn keine Typerweiterung vorliegt, wenn man es sogar insbesondere mit einer Typeinschrankung zu tun hat. Dies soll nun etwas genauer beleuchtet werden.

In Java ist die Klasse Stack als Subklasse der Klasse Vector (die keinen

**Stack als Subklasse Vektor im mathematischen Sinne, sondem eher ein dynamisches, also in**

**von Vector?**

seiner Grosse wachsen könnendes Array reprasentiert) definiert. Das fuhrt jedoch dazu, dass an Stellen im Programm, an denen eine indizierte Sammlung von Objekten mit wahlfreiem Zugriff (eben ein Objekt vom Typ Vector) erwartet wird, ein Objekt vom Typ Stack auftauchen kann, dessen interne Repräsentation zwar auf einem dynamischen Array a la Vector aufbauen mag (und der deswegen davon erbt), der aber an seiner offentlich zugangigen Schnittstelle die Funktionen für den wahlfreien Zugriff unterdrucken muss (was in Java allerdings nicht geht). Solte namlich das Programm, in Erwartung einer indizierten Sammlung, auf ein Element darin zugefrein wollen und anstelle dieser einen Stack vorfinden, kann das Programm nicht fortgesetzt werden, es sei denn, es findet vor dem Zugriff eine entsprechende Prufung (und ggf. eine Verzweigung zu alternativen Verfahrensweisen) statt. Eine solche Prufung muss jedoch zur Laufzeit stattfinden; wird sie vergessen (nicht implementiert) und es taucht an dieser Stelle ein Stack auf, dann hat man es mit einem waschechten Programmierfehler zu tun. Immerhin lassen sich solche Fehler einfach vermeiden, indem man abgeleiteten Typen verbietetet, Eigenschaften zu unterdrucken.

Eine schwachere Variante, die aber ahnlich katastrophale Folgen haben

**nichtkonforme kann und deren Vorliegen nur schwer festzustellen ist, stellt der Fall dar,**

**Verhaltensanderung**

dass eine Funktion in einem Subtyp so abgeandert wird, dass sie dem (vom Supertypen) erwarteten Verhalten widerspricht. Dies ist beispielsweise bei den beiden Typen **Set** (Menge) und **Bag** (Multimenge) der Fall. Wenn man namlich **Set** als Subtyp von Bag annummt, so konnte man das durchaus als eine Typeinschrankung begreifen, und zwar eine, in der die Anzahl der Vorkommen jedes einzelnen Elements auf die Werte 0 und 1 (den Wertebereich {0, 1}) beschrankt ist. Die Funktionen _Hinzufugen eines Elements", _Entfernen eines Elements" sowie die Angabe der Grosse und der Test auf Enthaltensein eines Elements werden von **Set** genau wie von Bag unterstutzt; der einzige Unterschied scheint zu sein, dass das Hinzufugen eines Elements, das in der Menge schon enthalten ist, diese nicht verändert.

Bei genauerem Hinsehen ergibt sich aber das Problem, dass **Set** durch seine Eigenheit mehrere charakteristische Eigenschaften von Multimengen verletzt. So gilt für Sets beispielsweise nicht wie für Bags, dass jedes Hinzufugen eines Elements die Grosse um 1 anwachsen lasst. Auch gilt nicht, dass genauso viele Elemente entnommen werden können, wie hinzugefugt wurden; alle doppelten Einfugungen werden von **Set** einfach unterschlagen. Ein Programm, das auf die Eigenschaften von Bags setzt und stattlessen mit einem Set arbeiten muss, funktioniert mit hoher Wahrscheinlichkeit nicht mehr korrekt.

Umgekehrt wurde, wenn man Bag als Subtyp von **Set** annehmen wurde, die für **Set** charakteristische Eigenschaft, namlich dass nach dem Entfernen eines Elements diese nicht mehr darin enthalten ist, verletzt. Programme, die darauf bauen, dass diese Eigenschaft garantiert wird und die anstelle einer Menge eine Multimenge bekommen, funktionieren nicht mehr korrekt. Je nach eingenommenem Standpunkt stellt dies einen Typfehler dar.

Wenn man versucht, der Ursache des Fehlers auf den Grund zu gehen, kommt man schnell zu der Einsicht, dass die charakteristischen Eigenschaften keiner der beiden Typen die des jeweils anderen implizieren, dass sie genauer im Widerspruch zueinander stehen. Deswegen lassen sich keine korrekten Satze wie,fur alle Objekte vom Typ X gilt,..." bilden, wobei die Objekte vom Typ X (**Bag** oder **Set**) immer auch die vom jeweils anderen Typ Y, der Subtyp von X sein soll, einschliessen soll. Dies entspricht jedoch genau der Definition des Subtypings aus Kurseinheit 3, Abschnitt 26.1; tatsachlich ist es mehr oder weniger eine Frage der Auslegung, ob für den Tatbestand des Subtypings die in Kapitel 26 genannten syntaktischen Bedingungen, insbesondere die Ko- und Kontravarianz, ausreichen oder ob strengere Bedingungen der Substituierbarkeit eingehalten werden mussen.

In der Pravis wird die Prufung der Substituierbarkeit durch Type-checking-Verfahren in Form der Prufung der Typkonformitat immer nur angena-hert; tatsachlich kann nicht einmal eine Substituierbarkeit ausgeschlossen werden, wenn mangelnde Typkonformitat vorlieget.86 Gleichwohl werden

entsprechende Zuweisungen nicht zugelassen. Umgekehrt bedeutet aber Typkonformitat nicht automatisch auch Substituierbarkeit -- dazu ist auch eine Betrachtung des Verhaltens notwendig.

Footnote 86: Die Substituierbarkeit kann deswegen nicht vollstandig ausgeschlossen werden, weil diese immer auch vom Verwendungskontext abhangig ist — wenn beispielsweise mit einem Objekt gar nichts gemacht wird, kann es auch durch ein anderes erstzt werden, selbst wenn die entsprechenden Typ nicht konform sind. Mehr dazu in Abschnitt 54.5.

### Verhaltensbasiertes Subtyping

Die Regeln des Subtyping aus Kapitel 26 und die damit verbundene Regelung der Zuweisungskompatibilitat bezogen sich ja lediglich auf die Elemente einer Typdeklaration und damit auf rein statische Information. Um nun auch das Verhalten der Objekte eines Typs einzufangen, greift man auf eine Idee der formalen Programmverifikation zuruck: der der Oberfuhrung der Vorbedingungen in Nachbedingungen nach der Art von (54.1). Ins Objektorientierte übertragen heilst das, dass ein Typ dann korrekt (implementiert) ist, wenn für jede Methode gezeigt werden kann, dass aus der Vorbedingung der Methode die Nachbedingung folgt (und dass die Invarianten des Typs hochstens temporar, wahrend der Methodenausfuhrung verletzt werden). Wir schreiben dazu für eine Methode m und einen Typ T

\[\boldsymbol{pre}_{m}^{T}(\boldsymbol{self}\boldsymbol{:}\boldsymbol{T}) \boldsymbol{\Rightarrow}\boldsymbol{post}_{m}^{T}(\boldsymbol{self}\boldsymbol{:} \boldsymbol{T}) \tag{54.2}\]

und meinen damit, dass für eine Implementierung von m in der zu T gehorenden Klasse, die auf einem Empfangerobjekt vom Typ T (einer Instanz der entsprechenden Klasse) aufgerufen wird, die Nachbedingung aus der Vorbedingung folgt. Diesen Beweis mussen wir aber zum Gluck nicht fuhren -- wir sind hier nicht an der Korrektheit von Implementierungen an sich interessiert, sondern vielmehr daran, ob sich eine (korrekte) Implementierung durch eine andere (ebenfalls korrekte, aber eben andere, auch in Bezug auf ihre Spezifikation)ersetzen lasst. Konkret: Wir sind an einer verhaltensbasierten Subtypenrelation interessiert, also an den Bedingungen, die potentielle Subtypen einhalten mussen, damit sie die Spezifikation des Supertyps erfullen, so dass man sie als verhaltenskonform betrachten kann und eine Subtypenbeziehung wie in Kapitel 26 beschrieben gegeben ist. Das ist immer dann der Fall, wenn obige Implikation auch für Objekte des potentiellen Subtypen S gilt, also wenn

\[pre_{m}^{T}(self\colon\mathbb{S})\Rightarrow post_{m}^{T}(self\colon\mathbb{S}) \tag{54.3}\]

Man spricht dann von einem **Behavioural subtyping**, das zu deutsch am besten als **verhaltensbasiertes Subtyping87** wiedergegeben wird.

Es gilt also, (6.3) sicherzustellen. Bei der Spezifikation der Methoden des (potentiellen Sub-) Typs S wird man aber zunächst nicht auf die Vor- und Nachbedingungen von T zuruckgreifen, sondern eigene angeben, so dass für alle Methoden m von S

Footnote 87: Nun ist das immer noch halb englisch —,,das Subtypen” klingt aber wirklich doof.

\[pre_{m}^{S}(self\colon\mathbb{S})\Rightarrow post_{m}^{S}(self\colon\mathbb{S}) \tag{54.4}\]

als Ausdruck der Korrektheit gilt. (54.3) folgt daraus unmittelbar, wenn

\[pre_{m}^{S}\equiv pre_{m}^{T}\;\;\text{und}\;\;post_{m}^{S}\equiv post_{m}^{T}\]

fur alle m in T ist, aber das wird ja wie gesagt im allgemeinen nicht der Fall sein. Die Frage ist vielmehr: Wie mussen \(pre_{m}^{S}\), \(pre_{m}^{T}\), \(post_{m}^{S}\) und \(post_{m}^{T}\) miteinander im Verhaltnis stehen, damit Objekte vom Typ S die Anorderungen für Objekte vom Typ T erfullen? Formal: Was mussen wir voraussetzen, damit aus (54.4), dem Verhalten von m in S, (54.3), das Verhalten von m in T angewandt auf Objekte aus S, folgt?

Leider ist es mit der Beantwortung dieser Frage aber noch nicht genug. Aufgrund des in der objektorientierten Programmierung weit verbreiteten Aliasing kann ein Objekt vom Typ S, das von einem Klienten wie ein Objekt vom Typ T betrachtet wird, von einem weiteren Klienten wie ein Objekt vom Typ S (oder wie von einem anderen Supertypen als T) betrachtet werden. Dadurch können dann auch Methoden auf dem Objekt aufgerufen werden, die Zustandsanderungen des Objekts verursachen, die nicht durch die mit T verbundenen Methodenspezifikationen (deren Vorund Nachbedingungen) abgedeckt sind, ja die ein Verhalten bewirken, das mit dem von T nicht kompatibel und das für Benutzerinnen des Objekts, die es als ein T ansehen, nicht akzeptabel ist. Eine methodenweise Betrachtung von Bedingungen für die Substituierbarkeit reicht also nicht aus. Man ahnt bereits, dass die Angelegenheit komplex wird.

### Das Liskov-Substitutionsprinzip

In Sachen verhaltensbasiertes Subtyping am meisten Bekanntheit erlangt haben die Arbeiten von Barbara Liskov und Jeannette Wing. Tatsachlich ist das sog. **Liskov-Substitutionsprinzip** (Liskov substitution principle, LSP) eines der am haufigsten zum Thema Subtyping angefuhrten, weswegen es auch hier behandelt werden soll. Ohne den Beitrag der beiden schmalem zu wollen, ist dies durch die Sache jedoch nicht gerechtfertigt -- anderen, fruheren Arbeiten gebuhrt mindestens gleicher Ruhm und auserdem ist, wie Sie noch sehen werden, das LSP zu streng gefasst, weswegen es nutzliche, für die Prais relevante Falle des verhaltensbasierten Subtyping ausschlieBt.

Historischer Hintergrund des Liskov-Substitutionsprinzips war die Suche **Motivation** nach einer hinreichenden Bedingung für die Subtypenrelation zwischen zwei Typen. Wir hatten ja in Kapitel 26 (Kurseinheit 3) festgestelt, dass es bei den meisten Programmiersprachen ausreicht, dass ein Typ B deklariert, Subtyp eines Typs A zu sein, damit Zuweisungskompatibilitat von B nach A festgestelt werden kann.88 Dazu war es allerdings notwendig, dass die Eigenschaften von A auf B übertragen (vererbt) und dass dabei die Regeln von den ko- bzw. kontravarianten Redefinitionen von Parametertypen eingehalten werden. Dies wird im allgemeinen durch die Sprachdefinition und durch den Compiler sichergestellt.

Footnote 88: Man beachte den Zirkel in der Definition: für das Subtyping reicht aus, dass Zuweisungskompatibilität besteht; der Compiler leitet die Zuweisungskompatibilität aus dem Bestehen einer Subtypenbeziehung (z. B. **extends** oder implements in Java) ab.

Das _verhaltensbezogene Subtyping_ geht nun über die auf die Kontrolle der Parametertypen beschrankte, syntaktische Subtypenbeziehung hin- **Subtyping** aus, indem es -- nach Liskov und Wing -- fordert, dass sich Objekte eines Subtyps und seines Supertyps gleich verhalten sollen, und zwar insoweit irgend jemand oder irgendein Programm dies feststellen kann. Diese Forderung kulminiert in der Regel

\begin{tabular}{l|l} \hline \hline \multicolumn{2}{l}{Subtype Requirement: Let \(\phi(\mathbf{x})\) be a property provable about objects \(\mathbf{x}\) of type T. Then \(\phi\) (\(\mathbf{y}\)) should be true for objects \(\mathbf{y}\) of type S where S is a subtype of T.} \\ \hline \hline \multicolumn{2}{l}{Eine deutsche Paraphrase dessen fanden Sie bereits in Abschnitt 26.1.} & **kritische Betrachtung** \\ \hline \multicolumn{2}{l}{Diese Definition ist gleich in mehrfacher Hinsicht problematisch.} \\ \hline
1. Da sie die Subtypenbeziehung definiert, ist davon auszugehen, dass \(\mathbf{x}\) exakt vom Typ T ist und \(\mathbf{y}\) exakt vom Typ S. Es sind also insbesondere \(\mathbf{x}\) und \(\mathbf{y}\) keine Objekte von Subtypen von T bzw. S. Damit ist die Definition nicht auf abstrake Typen und Interfaces ausdehnbar. 2. Damit zusammenhangend ist die Aussage lospelost von jedem konkreten Gebrauch der Objekte. Wie in Abschnitt 54.5 noch genauer dargestelt werden wird, kann

[MISSING_PAGE_FAIL:316]

Aus den obigen Regeln der Subtyprelation und aus der Korrektheit der überschreibenden Methode in **S** folgt die gewunschte Substituierbarkeit.

Es bleibt jedoch noch das eingangs beschriebene, mit dem Aliasing und **das Aliasing-Problem** der damit verbundenen Moglichkeit des zusatzlichen Methodenaufrufs assoziierte Problem bestehen. Dafur identifizieren Liskov und Wing zwei Losungen:

Die erste sagt aus, dass das Verhalten eines Subtyps immer dann mit dem **Verhaltensimulation** des Supertyps konform ist, wenn alles zusatzliche Verhalten des Subtyps durch Verhalten des Supertyps simuliert werden kann, wenn es also für jede zusatzliche Methode eine Kombination von Methodenaufrufen des Supertyps (bzw. deren überschriebenen, verhaltenskonformen Varianten) gibt, die den Effekt der zusatzlichen Methode hat und die der Klient des Objekts auch selbst (oder ein anderer Klient, der aber das Objekt durch denselben Typ sieht) durchfuhren konnte. Diese Bedingung ist jedoch ziemlich hart, da sie im Grunde aussagt, dass ein Subtyp lediglich Makros hinzufugen darf. Auf der anderen Seite ist ihre Einhaltung, wenn auch nicht automatisch, so jedoch zumindest anschaulich relativ einfach nachzuweisen (was für die Praxis eminent wichtig ist).

Die zweite Losung ist denn auch weniger einschrankend, dafur aber in **Zustandswechselin-**der Praxis kaum nachzuweisen: Sie verlangt von jedem Typ zusatzlich zur **varianten** Verhaltensspezifikation der Methoden (über die ublichen Vor- und Nachbedingungen) die Einhaltung von Verlaufseigenschaften, die die moglichen Zustandswechsel der Objekte des Typs betreffen und die wir deswegen **Zustandswechselinvarianten** nennen. Dazu ware eine Art endlicher Automatenspezifikation, also eine Spezifikation der Menge der moglichen Zustande und Zustandsübergange, notwendig. Das Problem dabei ist jedoch, dass die Zustande eines Objekts nicht abstrakt (z. B. in Form einer Aufzahlung von Zustandsnamen) existieren, sondern sich in der Belegung von Instanzvariablen manifestetieren, so dass sich der Zustandsraum kombinatorisch (abzuglich der funktionalen Abhangigkeiten der Attribute) ergibt. Um dem aus dem Weg zu gehen, werden bei den historischen Zustandswechseln lediglich zwei beliebige, zeitlich nicht notwendig unmittelbar aufeinander folgende Zustande betrachtet und für diese eine Bedingung formuliert, die eingehalten werden muss. Man beachte, dass die Einhaltung der ersten Bedingung die zweite impliziert: Wenn alle Methoden des Supertyps die historischen Invarianten einhalten und wenn eine Methodedes Subtps sich als Kombination von Methoden des Supertyps darstellen lasst, dann halt auch diese die historischen Invarianten ein.

So gut das Liskov-Substitutionsprinzip auch begründet sein mag, es er- **LSP ist zu restriktiv** weist sich für die Praxis als zu streng. So konnte man beispielsweise in einem Typ T eine Methode **echo: i <Integer> "Integer definieren, die den Eingabeparameter gleich wieder ausgibt (die sog. Identitat oder Identitatsfunktion). In einem Subtyp S konnte man dann die Methode so überschreiben, dass sie beliebige Objekte entgegennimmt und gleich wieder zuruckgibt: **echo: i <Object> " Object**. Die Methode ist damit zwar in ihrem Eingabeparameter kontravariant, aber in ihrem Ausgabeparameter nicht kovariant, und erfullt somit die Bedingung des LSP nicht. Gleichwohl kann **echo:** auf einem Objekt vom Typ S überall da aufgerufen werden, wo es auch auf einem Objekt von Typ T aufgerufen werden kann, denn es kommt so niemals dazu, dass die Regel der Kovarianz des Ausgabeparameters verletzt wird. Wir haben es beim LSP also mit einer Typprifung zu tun, die gultige Programme zuruckweist. Dafur, dass die Einhaltung des LSP für den allgemeinen Fall gar nicht automatisch überpruft werden kann, ein ziemlich hoher Preis.

### Relativitat der Substituierbarkeit

Nun kann man argumentieren, dass Substituierbarkeit im Einzelfall von der jeweiligen Verwendung der Typen abhangt (vgl. FuBnote 86). So kann man im Beispiel von **Set** und **Bag** gar nicht sagen, dass grundsatzlich das eine nicht das andere substituieren kann, denn es kann durchaus Verwendungen des einen oder anderen Typen geben, in denen der jeweils andere durchaus als Erstz infrage kommt. Das Vorliegen einer echten Substituierbarkeit ist also nicht auf Basis der beteiligten Typen alleinentscheidbar, sondern hangt auch von deren Verwendung ab. Das wiederum bedeuttet (auch vor dem Hintergrund des oben gesagten zur funktionalen Aquivalenz), dass es so etwas wie eine absolute (d. h., von jeder moglichen Verwendung losgeloste) Substituierbarkeit eigentlich nicht gibt.

Wie kann man diesem Umstand abheflen? Nun, indem man neben der **Perspektivwechsel** Sicht der Programmiererin, die die Typen liefert und die sich um deren Substituierbarkeit (und die davon abhangige Subtypenbeziehung) sorgt, auch noch die Sicht der Programmierrein, die die Typen zu einem konkreten Zweck einsetzen will, einbezieht. Nur diese Programmiererin weiss namlich, was sie sich genau von einem Typen (genauer: von den Objekten eines Typs) enwartet, und nur diese kann beurteilen, welche Typen zu ihrem Zweck ggeneinander austauschbar sind.

Wie aber druckt die Programmiererin ihre Erwartung aus? Die Antwort ist **Typen als Rollen** verbluffend einfach: Indem sie selbst einen Typ definiert, dessen Definition die -- und eben nur die -- Eigenschaften umfasst, die sie verlangt. Ein Typ, der genau diese Erwartung und nicht mehr ausdruckt, spezifiziert gewissermanen eine Rolle, die die Objekte im Kontext der Verwendung zu spielen haben. In der Regel wird dieser Typ nur einen Teil der Eigenschaften umfassen, die allgemeine Typen wie **Set** oder **Bag** spezifizieren; im Gegenzug ist damit aber auch die Auswahl der Typen, deren Objekte für ihre Zwecke infrage kommen, groser.

Die einzige Vorausetzung dafur, dass Objekte die ihnen durch ihren Typ aus Klientinnensicht zugewiesene Rolle auch spielen können, ist, dass sie dazu typkonform sind.

Diese zweiseitige Sicht auf Typen, namlich die der Nutzerin und die der Anbieterin, beginnt sich erst langsam durchzusetzen. Die Programmiersprache Java und in der Folge auch C# bieten immerhin ein _Interface-als-Typ-Konzept_ (s. Kapitel 40 in Kurseinheit 4und Abschnitt 50.4.2 in Kurseinheit 5) an, mit dem es moglich ist, in einem Programm partielle Sichten auf Typen zu spezifizieren. Allerdings wird in der Programmierpraxis die Moglichkeit dieser beiden Sprachen kaum dazu genutzt, Bentuzerinnen ihre eigenen Anforderungen als Typen definieren zu lassen. Vielleicht handhaben Sie es ja zukunftig anders.

## 55 Das Fragile-base-class-Problem

Unter dem **Fragile-base-class-Problem** versteht man eine ganze Familie von Problemen, die in unmittlebarem Zusammenhang mit der Verebung stehen. Dabei ist der Name insofern etwas irrefuhrend, als nicht unbedingt die _Basisklassen_, also die Superklassen (vgl. Abschnitt 11.1), die,,anfalligen" oder,,zerbrechlichen" sind, sondern eher die Klassen, die von ihnen erben. Ein einfaches Beispiel soll erlautern, worum es geht.

Wir nehmen an, wir hatten eine Klasse TapeArchive geschrieben, die Videobander archiviert. Da es sich nicht um eine Mickey-Maus-Anwendung auf dem heimischen Desktop handelt, sondern um ein kommerzielles System, erfolgt die Datenhaltung in einer Datenbank. Die folgende Smalltalk-Klassendefinition gibt einen kleinen Ausschnitt des Systems wieder.

\begin{tabular}{l l} \hline \hline Klasse & TapeArchive \\ \hline \hline \multicolumn{2}{l}{benanite Instanvariablen} & database \\ \hline \hline \multicolumn{2}{l}{Klassemmethoden} & \\ \hline \hline
**1510** & new \\ \hline \hline
**1511** & **a super new initialize** \\ \hline \hline
**1512** & initialize \\ \hline \hline
**1513** & database := Database new: 'tape archive' \\ \hline
**1514** & addTape: aTape \\ \hline \hline
**1515** & database beginTransaction. \\ \hline \hline
**1516** & database add: aTape. \\ \hline
**1517** & database endTransaction \\ \hline
**1518** & addAllTapes: aCollection \\ \hline
**1519** & aCollection do: [ :aTape | self addTape: aTape ] \\ \hline \hline \end{tabular}

Nun ist es in der objektorientierten Programmierung ublich, dass man solche Klassen wiederverwendet, indem man davon neue Klassen ableitet. Wenn beispielsweise eine Kundinenanforderung kommt, nach der mit jeder Archivierung eine Nachricht verschickt werdenmuss, die das anzeigt, und wenn diese neue Anforderung nicht für alle Kundinnen der Software gleichermassen interessant ist, dann schreibt man eine Subklasse, die das geanderte Verhalten bereitstellt:

\begin{tabular}{l l} \hline \hline Rasse & NotifyingTapeArchive \\ benannte Instanzurialien & listener \\ Superflasse & TapeArchive \\ Rassemethodoen & \\ \hline
1520 new: alistener & \\
1521 & super new initialize: alistener \\ Instanzmethodoen & \\ \hline
1522 initialize: aListener & \\
1523 listener := alistener & \\
1524 addTape: aTape & \\
1525 super addTape: aTape. & \\
1526 listener notify: aTape & \\ \hline \end{tabular}

Das Schone an der Objektorientierung ist dabei, dass man nur die Unterschiede (Differentia) spezifizieren muss -- der Rest wird einfach gewelt.

So genugt es im gegebenen Fall, die Initialisierung (nicht so interessant) und die Methode **addTape:** anzupassen. Das Verhalten von **addAllTapes:** kann unverändert bleiben, da dies die (dynamisch gebundene) Methode **addTape:** aufruit und somit auch das von **NotifyingTapeArchive** geforderte Verhalten, namlich die Notification aller archivierten Bander, garantiert. Ein ganz ahnliches Beispiel (anhand der Klasse **Collection**) war Ihnen in Kurseinheit 2, Abschnitt 10.3 schon einmal begegnet; es handelt sich auch hier um einen Fall von _offener Rekursion_, die erst durch _dynamisches Binden_ (Kapitel 12) aufgelost wird. Aufrufe dieser Art sind das Herz vieler objektorientierter (Anwendungs-)Frameworks und auch diverser Entwurfsmuster.

Oder auch nicht. Das Problem ist namlich, dass man der Klasse **Vorsicht Falle**TapeArchive** weder ansieht, was sie garantiert, noch, wovon die Korrektheit ihrer Subklassen abhangt. Wenn in der Folge z. B. eine anderere Kundin norgelt, das Hinzufugen von grossen Mengen von Bandern dauere zu lange, wenn man das wiederholte Aufrufen von **addTape:** aus addAllTapes:** und die dadurch bedingte wiederholte Ausfuhrung von **beginTransaction** und **endTransaction** als Ursache ausmatht und wenn man dann in Erwagung zieht, nicht nur die norgelnde Kundin in ihrer Version, sondern alle Kundinnen mit der optimierten Implementierung

\begin{tabular}{l l} \hline Rasse & TapeArchive \\ nistanzmethodoen & \\ \hline
1527 & \\
1528 addAllTapes: aCollection & \\ \hline \end{tabular}

* 1529databasebeginTransaction.
* 1530aCollectiondo:[::aTape|databaseadd:aTape|.
* 1531databaseendTransaction

zu beglucken, was sprache dagegen?

**Selbsttestaufgabe 55.1**

Bevor Sie weiterlesen, antworten Sie: Was sprache dagegen?

Vermutlich nur die Wenigsten unter Ihnen werden sofort sagen können, was dagegen spricht, denn in der Klasse TapeArchive scheint nach wie vor alles in bester Ordnung zu sein. Was man namlich nicht sehen kann, ist, dass die Korrektheit der Methode addAllTapes: davon abhangt, dass sie addTape: aufruft -- zwar nicht für die Klasse TapeArchive selbst, dafur aber für ihre Subklasse NotifyingTapeArchive. Hier werden jetzt namlich nur noch für einzeln archivierte Bander Benachrichtigungen verschickt.

Hand aufs Herz: Hatten Sie den Fehler vorhergesagt? Wenn nicht, dann liegt das vermutlich daran, dass Sie der Tauschung erlegen sind, addAllTapes: in TapeArchive wurde die benachbarte Methode addTape: aufruft, und wenn man nur den Beitrag von addTape: in addAllTapes: verlagert und dafur addTape: nicht mehr aufruft, dann ware das eine semantikerhaltene Umstrukturierung (ein sog. _Refactoring_; s. Kurs 01853). Tatsachlich benraubt aber genau dies die Subklassen der Moglichkeit, eigenes Verhalten an genau dieser Stelle -- dem Aufruft von addTape: -- einzubringen, und wenn eine solche Beraubung im Nachhinein erfolgt, kann sie eben den Code,,zerbrechen".

Das Schlimme an diesem Problem ist, dass man noch nicht einmal genau **Schuldfrage** weiss, wem man die Schuld geben soll -- TapeArchive, weil es einen Vertrag bricht, den es gar nicht paraphiert hat (oder weil es keine Rucksicht auf Subklassen nimmt, die es gar nicht kennt), oder NotifyingTapeArchive, weil es sich grundlos darauf verlasst, dass die geerbten Methoden dauerhaft die eigenen (in diesem Fall das geerbte addAllTapes: das eigene addTape:) aufruften? Wenn noch nicht einmal die Schuld feststeht -- wie kann man das Problem verhindern?

Es gibt zahlreiche Varianten des Fragile-base-class-Problems, die hier nicht alle aufgefuhrt werden sollen. Zugrunde liegt ihnen immer dasselbe: Zwischen einer Klasse und ihren Subklassen bestehen durch die Vererbung von Eigenschaften starke Abhangigkeiten, die -- wenn überhaupt -- nur unvollstandig dokumentiert sind. Zwar konnte man annehmen, dass von allem, was wererbt wird, eine Abhangigkeit ausgeht, die man bei Anderungen pauschal berucksichtigen muss, aber dies wurde die Moglichkeiten, in Superklassen etwas zu andern, so stark einschranken, dass das ganze Konzept ad absurdum gefuhrt wurde. Es bleibt also nicht viel mehr, als beim Einsatz von Vererbung grose Vorsicht walten zu lassen oder sie ganz zu verbieten.

Das folgende, im Kontext des Component Object Models (COM) getatige Zitat aus dem Hause Microsoft fast es schon zusammen:

Implementation inheritance--the ability of one component to "subclass" or inherit some of its functionality from another component--is a very useful technology for building applications. Implementation inheritance, however, can create many problems in a distributed, evolving object system.

The problem with implementation inheritance is that the "contract" or relationship between components in an implementation hierarchy is not clearly defined; it is implicit and ambiguous. When the parent or child component changes its behavior unexpectedly, the behavior of related components may become undefined. This is not a problem when the implementation hierarchy is under the control of a defined group of programmers who can make updates to all components simultaneously. But it is precisely this ability to control and change a set of related components simultaneously that differentiates an application, even a complex application, from a true distributed object system. So while implementation inheritance can be a very good thing for building applications, it is not appropriate for a system object model that defines an architecture for component software.

In a system built of components provided by a variety of vendors, it is critical that a given component provider be able to revise, update, and distribute (or redistribute) his product without breaking existing code in the field that is using the previous revision or revisions of his component. **In order to achieve this, it is necessary that the actual interface on the component used by such clients be crystal clear to both parties.** Otherwise, how can the component provider be sure to maintain that interface and thus not break the existing clients?

Auf die objektorientierte Programmierung übertragen ist das Problem also, dass der Vertrag zwischen den Klassen einer Verebungshierachie nicht klar definiert ist. Wenn die Superoder Subklasse ihr Verhalten unenwartet verändert, kann daraus undefiniertes Verhalten verwandter Klassen resultieren. Tatsachlich war die Verebung von Implementierung aus der Spezifikation von Microsofts _Component Object Model_ (COM) verbannt; stattdessen setztze man voll auf die Verebung von Interfaces (was wir als Subtyping bezeichnen wurden). Inzwischen (mit dem.NET-Framework) ist diese harte Haltung wieder aufgegeben worden, was wohl auch daran liegt, dass hier Komponenten Klassen sind; es bleiben jedoch die in Kapitel 50 (im Kontext von C#) enwahnten Vorbehalte gegenüber dem dynamischen Binden.

Nun liegt ja zunächst nahe, bei der Verebung das zu tun, was man bei **Verebungsinterface** Abhangigkeiten immer macht: Schnittstellen einzufuhren. Im Gegensatz zu der Schnittstelle, die einem Klient einer Klasse angeboten wird (der diese Schnittstelle nutzt, indem er seine Variablen mit dem zur Klasse gehorenden Typ deklariert und somit auf Instanzen der Klasse zugerefen kann), handelt es sich bei der Schnittstelle zwischen einer Klasse und ihren Subklassen jedoch um eine etwas anders geartete: Hier gibt es lediglich zwei Variablen **self** (bzw. **this**) und **super**, die allerdings keine Abhangigkeit von anderen Objekten ausdru-cken und die zudem nicht explizit typisiert sind. Die damit verbundene Schnittstelle, also die Menge der Eigenschaften, auf die man über diese Variable zugerefen kann, und wo man diese Eigenschaften dann findet (also wo sie definiert sind), muss man sich selbst zusammensuchen. Mit _Information hiding_ und dem Verbergen von _Implementationsgeheimissen_ hat das freilich nichts zu tun. Was man vielmehr brauchte, ware ein explizites **Veerbungs-interface**.

Einige erste, zarte Ansatze zur Einfuhrung von expliziten Vererbungsin-terfaces hatten Sie bereits gesehen: Die Verwendung des Zugriffsmodifi-zierers **protected** in Java, C# und C++ sowie die explizite Deklaration von **überschreibung mittels virtual** und **override** in C# (und C++). Im obigen Beispiel wurde die Deklaration von **addTape:** als nicht überschreibbar (und somit als nicht dynamisch, sondern statisch gebunden) verhindern, dass **NotifyingTapeArchive** diese Methode abandert _und sich zugleich_ darauf verlast, dass die gerbte Methode **addAllTapes:** die überschreibende Version von **addTape:** aufruft (sie konnte sie aber immerhin noch neu einfuhren, aber diese neue Version wurde beim Binden in **addAllTapes:** nicht berucksichtigt). **NotifyingTapeArchive** musste dann wohl oder **ubel beide Methoden neu implementieren und konnte bei der Gelegenheit selbst dafur Sorge tragen, dass **addAllTapes:** den Fehler nicht macht. Allerdings wurde dadurch auch bei einem direkten Aufruf von **addTape:** von **auserhalb auf einer Variable vom Typ **TapeArchive**, die eine Instanz vom Typ **NotifyingTapeArchive** halt, die überschreibende Impleentierung unberucksichtigt bleiben (da ja keine dynamische Bindung mehr stattfindet). Im Gegensatz dazu wurde die Verwendung von **virtual** bei **addTape:** in **TapeArchive** der Programmiererin einen Hinweis darauf geben, dass die Methode in Subklassen für diese relevante Modifikationen enthalten kann, so dass man Aufrufe dieser Methode nicht einfach, wie im obigen Beispiel geschehen, kurzen kann.

Wenn es um die Sicht- und Zugereifbarkeit von Elementen geht, scheint **Bidirektionalitat des** der Zugriffsmodifizierer **protected** zunächst auf gleicher Ebene mit **protected-Interfaces: public** und **friend** zwischen zwei (nicht über Vererbung in Beziehung stehenden) Klassen zu stehen: die **protected** deklarieteren Elemente einer Klasse sind wie bei einem _dedizierten Export_ (s. Abschnitt 52.2) auch in ihren Subklassen sicht- und verwendbar. Was allerdings nicht so klar ist, ist, dass **überschreibende**, als **protected** deklarierte Methode auch für den Code der Superklasse zugereifbar sind: eine **protected** Methode einer Subklasse kann -- über das dynamische Binden auf self bzw. this -- aus der Superklasse heraus aufge-rufen werden, ohne dass die Subklasse irgendeinen Hinweis darauf enthalt. Anders als bei der Zugereifbarmachung mit **public** oder **friend** bei nicht über Vererbung in Beziehung stehenden Klassen kann die Zugereifbarkeit also in beide Richtungen gehen, und zwar abhangig davon, ob die Methode **überschrieben** wird oder nicht: Wird sie **überschrieben, kann die **überschreibende** (in der Subklasse) von der Superklasse aus aufgerufen werden und die ubberschriebene (in der Superklasse) von der Subklasse (über **super**) -- wird sie nicht überschrieben, kann die Methode der Superklasse aus der Subklasse heraus aufgerufen werden.

Es bleibt also ein hochst verworrener Eindruck. Dies ist um so bedauerlicher, als Bjarne Stroustrup selbst kommentierte:

_One of my concerns about protected is exactly that it makes it too easy to use a common base the way one might sloppily have used global data.... In retrospect, I think that protected is a case where "good arguments" and fashion overcame my better judgement and my rules of thumb for accepting new features._

Bei der Definition von Java fand das offenbar kein Gehor. Und so bleiben die Schlusselworter protected, virtual und override nicht viel mehr als Zeichen des Bewussteins, dass es das Fragile-base-class-Problem gibt.

## 56 Das Problem der schlechten Tracebarkeit

Spatestens mit der Verfugbarkeit sog. Hochsprachen und den gleichzeitig immer grosser werdenden Programmen kam die Frage auf, was,,gute Programmierung" ausmacht. Eines der Hauptprobleme schlechter Programmierung war schnell identifiziert: die grosse Diskrepanz zwischen statischem, linearem Programmtext und dynamischem, stark verzweigendem und sich wiederholendem Programmablauf. Eine gute Programmiereerin hatte ihre Programme so zu schreiben, dass Programmtext und Programmablauf einander moglichst ahnlich waren, dass genauer die (statische) Struktur des Programms moglichst viele Ruckschlusse über seinen (dynamischen) Ablauf erlaubte. Man wolte also von den Programmierreinnen Klartext.

Ebenso schnell wie das Problem wurde seine Hauptverursacherin ausge-

**Goto-Anweisung vs.**

**Lokalitatsprinzip**

**Lokalitatsprinzip**

**Leis Programms an beliebige andere Stellen des Programms und durchbricht dabei auf brutale Art und Weise das ungemein nutzliche **Lokalitatsprinzip** von Programmen: Dinge, die zusammengehoren, stehen im Programmtext beieinander. So, und nur so, ist bei Inspektion des Programmtextes unmittelbar klar, wie man an eine Stelle im Programm gelangt ist und, mindestens ebenso wichtig, wie eine Variable ihren Wert bekommen hat.**

**Zur Veranschaulichung soll die nachfolgende Abbildung dienen, die einen**

**Anweisungsfolgen**

**Programmtext als eine Folge von Anweisungen stilisiert. Anweisungen**

**ohne Goto**

**sind durch Kreise dargestellt, die (textuelle) Folge der Anweisungen im Programmtext durch die kleinen Pfeile. Ohne besondere, den Kontrolfluss beeinflussende Anweisungen ent-

**spricht die (dynamische) Reihenfolge der Ausfuhrung der (statischen) Folge der Anweisungen im Programmtext. Bei**

**Betrachtung des starkerunrmandeten, mittleren Kreises (der entsprechenden Anweisung), z. B. wahrend einer Debug-Sitzung, ist daher aus dem unmittlebaren Kontext heraus (der Ellipse; Lokalitatsprinzipl) klar, welche Anweisung davor ausgefuhrt wurde und welche als nachstes drankommt. Alles ist in bester Ordnung.

Handelt es sich nun bei einer der Anweisungen um ein Goto, dann ist die **Probleme des Goto** Sachlage langst nicht mehr so klar. Man hat vielmehr die folgenden Falle zu unterscheiden:

1. Die betrachtete Anweisung ist selbst ein Goto:

In diesem Fall ist zwar klar, woher der Programmfluss kommt, und auch, wohin er geth, letztere s aber nur mit einer gewissen Einschrankung -- das Ziel ist nicht der Nachbar im Programmtext, sondern befindet sich ausserhalb des gewahlten Kontextes. Nun kann man den Kontext naturlich so wahlen, dass er das Ziel enthalt, und kurze Sprunge sind vielleicht auch so innerhalb des betrachteten Kontextes; allgemein gilt aber, dass jede gewahlte Lokalitat durch einen Sprung verletzt werden kann. Immerhin lasst sich aber das Ziel des Sprungs aus dem Kontext erkennen und der Kontext entsprechend wechseln.
2. Die betrachtete Anweisung ist Ziel eines Gotos:

Hier ist das Sachverhalt schon schwieriger. Der Programmfluss scheint bei Betrachtung des Kontextes genau wie im ersten Beispiel zu verlaufen. Wenn man den Kontext allerdings vergrossert, lernt man, dass die dynamische Vorgangerin der betrachteten Anweisung auch ein anderer sein kann. Der Kontext selbst gibt aber keinen Hinweis darauf; zwar kann das Vorhandensein eines Sprunglabels einen Hinweis darauf geben, dass die so markierte Anweisung Ziel eines Gotos sein kann, sie muss es aber nicht; in Sprachen wie Basic beispielsweise (damals noch weit verbreitet), in denen Zeilennummern gultige Sprungzielle sind, muss jede Anweisung als mit einem Label versehen betrachtet werden und kann somit Sprungziel von irgendwoher sein.

AulSerdem kann eine Anweisung von verschiedenen Gotos angesprungen werden, so dass unklar bleibt, welches die (zeitliche) Vorgangeranweisung war.89

Footnote 89: So gesehen gibt es den eingangs geschilderten Fall, bei dem alles klar ist, bei Programmen mit Gotos eigentlich gar nicht.
3. Die betrachtete Anweisung ist unmittelbare Nachfolgerin eines Gotos:

Hier ist zwar aus dem Kontext erischtlich, dass die statische Vorgangerin nicht die dynamische sein kann, ansonsten kann man aber nur mutmassen, dass es sich vielleicht um toten Code handeln konnte (also um Code, der niemals ausgefuhrt wird). Es kann namlich die Anweisung Sprungziel von Gotos außerhalb des Kontexts (wie in allen anderen Fallen auch) sein.

Fazit: Die Verwendung von Goto-Anweisungen verursacht ein hohes Mass an Nichtwissen bei der Interpretation von Quelltext. Speziell beim Debugging von Programmen ist der Blick in den Quelltext des Programms so nur sehr bedingt von Nutzen. Von daher, so der allgemeine Konsens, ist die Benutzung von Gotos zu vermeiden.

Wenn man also kein Goto benutzen darf, wie steuert man dann den Ablauf von Programmen? Die sog. **strukturierte Programmierung** sieht dafur neben der Sequenz von Anweisungen (ausgedruckt durch die unmittelbare Nachbarschaft im Programmtext) die Verzweigung, die Wiederholung und den Unterprogrammaufruf vor. Von diesen behalten die ersten beiden das Lokalitatsprinzip bei, solange man den Kontext auf den Umfang der _Fallunterscheidung_ bzw. Schleife, die damit ausgedruckt wird, ausdehnt. für den Unterprogrammaufruf gilt das jedoch nicht mehr: Schon weil ein Unterprogramm in der Regel von mehreren Stellen eines Programms aus aufgerufen werden kann und weil diese Stellen nicht automatisch denselben Kontext haben, wird hier das Lokalitatsprinzip durchbrochen. Dies ist aber unvermeidlich und man trostet sich damit, dass ein Unterprogramm, genauer eine Prozedur oder eine Funktion, immer genau an die Stelle zuruckkehrt, von der es aufgerufen wurde. Es ergibt sich also anschaulich die folgende Situation:Bei Betrachtung des textuell unmittlebaren Vorgangers der betrachteten Anweisung sieht man sofort, dass es sich beim dynamischen Vorganger

um die Return-Anweisung des aufgerufenen Unterprogramms handeln

 muss. Dies ist zwar nicht lokal, aber wenn man sich sicher sein kann, dass das Unterprogramm nur die Variablen manipuliert, die bei seinem Aufruf als tatsachliche Parameter übergeben wurden, und wenn zudem das Unterprogramm bekannte Vor- und Nachbedingungen einhalt, dann ist das kein Problem. Selbst wenn man nicht weiss, wie die Variablen manipuliert wurden, so ist die Unwissenheit, die durch einen Unterprogrammaufruf verursacht wird, im Vergleich zu der beim Goto gering. Ihr steht auf der anderen Seite ein grosser Nutzen gegenüber:

1. Man vermeidet die Duplizierung von Code, die notig ware, wenn man die Anweisungen des Unterprogramms im Aufrufkontext halten wollte und es mehrere solche Aufrufkontexte gibt (das sog. _Inlining_, das manche Compiler aus Optimierungsfrunden durchfuhren).

Man erlaubt der Programmiererin, ihre Programme in Abschnitte zu unterteilen, die sie detrennt untersuchen und verstehen kann.

Besonders der zweite Punkt ist wichtig: Aus Sicht der Programmiererin sollte es namlich reichen, zu wissen, was ein Unterprogramm tut, um es korrekt benutzen zu können. Sie muss also insbesondere nicht in das Unterprogramm hineinschauen, also seine Anweisungen inspizieren, wenn ihr eigentliches Interesse dem Kontext der Aufruftstelle gilt. Umgekehrt muss sie, wenn sie das Unterprogramm interessiert, nicht wissen, von wo es überall aufgerufen wird -- es reicht dann, zu wissen, mit welchen Parametern es versorgt wird, und die sind ihr per formale Parameterdeklaration bekannt. (Voraussetzung dieser Argumentation ist jedoch, dass es keine globalen Variablen gibt, die eine gegenseitige Beeinflussung von Aufruftstelle und Unterprogramm an den tatsachlichen und formalen Parametern vorbei erlauben. Diese globalen Variablen sind jedoch mindestens so sehr verpont wie das Goto.)

Bei der objektorientierten Programmierung hat man es zunächst mit einer leicht veränderten Situation zu tun. Hier sind namlich nicht allein das Vermeiden von doppeltem Code sowie die stufenweise Verfeinerung Kriterien für die Aufteilung in Unterprogramme, sondern auch die Disziplin, jede Teilfunktion der Klasse zuzuordnen, deren Daten sie manipuliert. Typische objektorientierte Programme teilen daher die Implementierung groserer Funktionen nicht nur in kleinere auf, sondern verteilen diese auch noch über viele Klassen. Auch wenn es sich dabeisets nur um Unterprogrammaufrufte handelt, die allen obgengenannten Anforderungen gennugen, so erfolgen die zum Programmwerstehen notwendigen Kontextwechsel doch in so kurzer Folge, dass man schnell den überblick darüber verliert.90

Footnote 90: Jede, die einmal ein größeres objektorientiertes Programm debugt hat, weiss, wovon ich spreche: Im Single-step-Modus der IDE springt der Programmzähler wild zwischen den verschiedenen Methoden und deren Klassen hin und her und haufig ist es schon nach kurzer Zeit kaum mehr moglich, zu rekonstrueren, wie sie ja für die gekommen ist, an der man sich gerade befindet. Viele Programmireineren ertappen sich dann dabei, dass sie, wie in der Steinzeit der Programmierung, Print-Anweisungen in ihre Programme einbauer, die den Programmablauf in nicht-flüchtiger Form festhalten. Zahlreiche Frameworks bieten darüber hinaus Tracing- oder Logging-Funktionen, mit denen es mit vergleichsweise wenig Aufwand möglich ist, den Programmablauf aufuzeichnen und zu rekonstrueren. Aus der Betrachtung des Programmtexts ist dies namlich meistens umnglich.

Nun ergibt sich aber mit der Einfuhrung von dynamisch gebundenen Unterprogrammaufrufen, wie sie ja für die objektorientierte Programmie- rung pragend sind, das Problem, dass aus dem Programmtext nicht unmittelbar ersichtlich ist, wohin der Sprung geht: Wie bereits in Kurseinheit 1, Abschnitt 4.3.2 bemerkt, verbindet das dynamische Binden den Unterprogrammaufruf mit der Verzweigung. Anschaulich betrachtet findet man im Quelltext die folgende Situation vor:

Es ist an der Stelle der betrachteten Anweisung nicht klar, von woher der in der Anweisung zuvor angestossene Unterprogrammaufruf zuruckkehrt -- es konnte von jeder Implementierung der im Gosub genannten Methode sein. Um das Sprungziel und damit die Return-Anweisung, die unmittelbarer Vorganger war, zu identifizieren, muss man die Klasse des Empfangerobjekts kennen, also die Klasse des Werts der Variable, auf der die Methode aufgerufen wurde. Die ist aber in der Regel nur auf Basis einer vollstandigen Programmanalyse bestimmbar, die sich nicht lokal durchfuhren lasst. Das Lokalitatsprinzip wird also durch das dynamische Binden weiter aufgewicht als durch den Unterprogrammaufruf allein.

Dieser Umstand hat dazu getfuhrt, dass das dynamische Binden von Skeptikerinnen und Gegnerinnen der objektorientierten Programmierung schon als eine Art Goto der 90er Jahre betrachtet wurde. Dieser Vergleich ist jedoch nicht ganz fair, weil, genau wie beim statisch gebundenen Unterprogrammaufruf, die Aufruferin ja gar nicht wissen muss, welche genauen Anweisungen als Antwort darauf

[MISSING_PAGE_FAIL:329]

Insbesondere bei grosseren Programmen kann leicht das Verlangen aufkommen, ein Programm nach mehreren Kriterien gleichzeitig zu strukturieren. Dies kann beispielsweise verschiedene Vererbungshierarchien betreffen -- so, wie man in der Biologie eine Taxonomie der Arten nach Herkunft (Genetik) und nach Merkmalen erstellen kann und, da beide ihren Nutzen haben, man weder auf die eine noch auf die andere ohne Not verzichten mochte, so kann man ein Programm beispielsweise unter dem Gesichtspunkt der Vererbung von Funktionalitat und von Daten alternativ strukturieren wollen. Voraussetzung hierfur ist allerdings, dass die verschieden Darstellungen getrennt von-einander gepflegt werden und dass durch sie weder Inkonsistenzen im Code noch ungewollte Interferenzen entstehen können.

Ein Nachteil der objektorientierten Programmierung (wie auch aller anderen heute bekannten Programmierparadigmen) ist sicherlich, dass die **(noch) keine Losung** sog. **Trennung der Belange**, besser bekannt als die **Separation of concerns**, nur unzueichehend unterstutzt wird. Ansatze wie das Subject- oder Aspect-oriented programming wurden zwar hoch gehandelt, sind aber dennoch nicht im Mainstream angekommen. Die Gründe dafur mogen vielfältig sein aber letztlich ist es wohl immer illusorisch, zu versprechen, man konne die essentielle Komplexitat, die einem Problem innerwohnt, durch programmiersprachliche Mittel besitigen. Insbesondere die getrennte Spezifikation eines Systems aus verschiedenen Sichten verlagert die Komplexitat nur in das Zusammenfuhren der Sichten: Wie so off muss das Ganze mehr sein als die Summe seiner Teile, um seinen Zweck zu erfullen. Unsere heutigen Softwaresysteme sind die kompliziertesten technischen Artefakte, die die Menschheit jemals hervorgebracht hat, und wer hier Einfachheit verspricht, soll sich schamen.

Everything should be made as simple as possible -- but no simpler.

## 58 Das Problem der mangelnden Kapselung

Als man mit der objektorientierten Programmierung begann, war man glucklich, weil man glaubte, mit dem Klassenbegriff eine naturliche Art der **Kapselung** (engl. encapsulation) gefunden zu haben, die zudem noch mit der hochangeeshenen Theorie der abstrakten Datentypen in Einklang steht (zumindest einigermassen): Klassen ergeben sich auf naturliche Weise aus der Anwendungsdomane (als Reprasentanen von _Allgemeinbegriffen_; s. Kurseinheit 1, Kapitel 7) und Daten sowie Implementierungsdetails lassen sich hinter der _Klassenschmittstelle_ (dem Protokoll der Objekte) verbergen.

Die erste grosse Enttauschung kam, als man merkte, dass die ebenfalls gefeierte Vererbung die Kapselung von Klassen auf unangenehmre Weise aufbrach: Wie in Kapitel 55 bemerkt, erzeugt die Vererbung starke Abhangigkeiten (auch zwischen den Implementierungsdetails!) von Klassen und ihren Subklassen. Diese Abhangigkeiten explizit zu machen vermag zwar vor Programmierfehlem zuschutzen, sie kann aber die Abhangigkeiten nicht besitigen -- sie dokumentiert sie lediglich. Die Abhangigkeiten zu beschranken bedeutet wiederum, einen Teil der Ausdrucksstarke und Flexibilitat der objektorientierten Programmierung aufzugeben, aber so ist das nun einmal: Alles hat seinen Preis.

Sehr viel dramatischer (und sehr viel weniger in aller Munde) ist jedoch ein ganz anderes Problem, das das gesamte bisherige Bemuhen der Objektorientierung um Kapselung auszuhebeln in der Lage ist: das **Aliasing-Problem**. Wenn namlich ein Objekt, das durch ein anderes Objekt gekapselt wird, indem das andere es in einer seiner Instanzvariablen halt, einen (weiteren) Alias besitzt, der nicht selbst dem kapselnden Objekt gehort, dann nuttzt es nichts, wenn diese Instanzvariable von außen unzuqreifbar ist91 -- sie wird namlich gar nicht gebraucht, um auf das gekapselte Objekt zuzugereifen. Man bedient sich einfach des Aliases.

Footnote 91: z. B. durch eine Deklaration mit private oder per Sprachdefinition wie in Smalltalk und Effel

Footnote 92: Man könnte hier argumentieren, dass Zeit ein Wert und kein Objekt und insofern auch nicht anderbar sein soll. Das ist hier aber gar nicht der Punkt.

In Smalltalk wird das Problem in folgendem einfachen Codefragment klar:

1532jetzt:=Time now.

1533a:=Anewerzeugungszeit:jetzt. "neues Objekt mit Erzeugungszeit"

1534jetztsetTime:Time now "Erzeugungszeit von a andert sich!"

Hier soll ein neues Objekt der Klasse A erzeugt werden und die Erzeugungszeit in einer entsprechenden Instanzvariable des Objekts festgehalten werden. Die Variable jetzt halt aber einen Alias auf das Objekt, das diese Zeit reprasentiert, andert man dieses Zeitobjekt (wie in Zeile 1534), dann betrifft dies auch die Erzeugungszeit des Objekts a.92 Nun konnte man meinen, es genugte, man ergarte sich einfach den (offensichtlichen) Alias jetzt und schriebe stattdessen

1535a:=Anewerzeugungszeit:Time now

Woher weiss man aber, dass die Methode now in der Klasse Time nicht einen Alias auf jedes neu erzeugte Objekt anlegt (beispielsweise weil Time Buch darüber fuhrt, welche Instanzen es von ihr gibt) und diesen Alias nicht herausgibt oder selbst verwendet, um die Objekte zu manipulieren? Auch die alternative scheinbare Losung,

1536a:=Anewerzeugungszeit:jetzt copy "neues Objekt mit Erzeugungsdatum"

funktioniert aus gleichem Grunde nicht zuverlassig, denn auch copy kann sich (heimlich) Aliase anlegen.

Ein anderes Beispiel, bei dem Aliase fehlerhaft eingesetzt werden, ist das folgende. Angenommen, Sie wollten eine Ampelsimulation an einem Fußangerüberweg programmieren.

Sie haben zwei Klassen, Ampel und Leuchte, und bauen ihre Objekte durch folgenden Code zusammen:

```
1537leuchteRot:=Leuchtenewfarbe:"rot".
1538leuchteGelb:=Leuchtenewfarbe:"gelb".
1539leuchteGruen:=Leuchtenewfarbe:"grun".
1540ampel1:=Ampelnew
1541autoRot:leuchteRot
1542autoGelb:leuchteGelb
1543autoGruen:leuchteGruen
1544fussgaengerRot:leuchteRot
1545fussgaengerGruen:leuchteGruen.
1546ampel2:=ampel1
```

Wenn Sie nun einem Fußanger per

```
1547ampel1fussgaengerGruenan
```

grunes Licht geben wollen, gehen leider mit der einen gleich alle vier grunen Leuchten an. War das in lhrem Sinn?

Man nennt Objekte, die die Implementierung eines Objektes ausmachen

```
**Repräsentations**und die hinter der Schnittstelle des Objektes verborgen werden sollen,

**Repräsentationsobjekte**. Die Leuchten des obigen Beispields sind allesamt Repräsentationsobjekte; sie kommen lediglich als _Innereien" der Objekte vor, deren Repräsentation sie ausmachen. Insbesondere gibt es in obigem Beispiel keine Verwendung einer Leuchte loggelost von einer Ampel. Dies muss aber nicht für alle Leuchten der Fall sein -- es ist durchaus denkbar, dass Leuchtenobjekte in anderen oder sogar im selben Programm auch ein unabhangiges Leben (aüberhalb von Ampeln) fuhren. Aber selbst das ist gar nicht notwendig -- im gegebenen Beispiel ware es auch denkbar, dass mit Leuchten noch einiges gemacht wird, bevor sie in eine Ampel eingebaut werden, so dass man das Aliasing-Problem weder an die Klasse Leuchte pauschal noch an deren Verwendung als Lieferant für Repräsentationsobjekte knupfen kann.

Wenn Aliase also schlecht sind, dann konnte man sie ja auch einfach verbieten. Tatsachlich bieten ja Programmiersprachen wie C#, C++ und Erfell die Moglichkeit an, Klassen als Werttypen zu definieren, so dass bei Zuweisungen nicht automatisch Aliase entstehen. Aber durch eine derart einfache Losung beschneidet man sich selbst nur wieder zahlreicher Moglichkeiten, wie das folgende Beispiel zeigt:
```
1548merkEsDir:=Dictionarynew.
1549a:=Anew.
1550merkEsDirat:"neinAObjekta"put:a.
1551a==(merkEsDirat:"neinAObjekta")
1552ifFalse:["Ohje,dubistnichtmehrdasselbe!"].
1553aaenderebeinenZustand.
1554a=(merksDirat:"neinAObjekta")
1555iffalse:["Ohje,dubistnichtmehrdasgleiche!"]Es ist gerade der Sinn eines Dictionaries (bzw. allgemeiner eines Containers wie einer Collection), dass keine Kopie, sondern das originale Objekt -- also ein Zeiger darauf -- gespeichert wirdl In einer Sprache ohne Referenzsementtik ware das jedoch nicht moglich. Man braucht also die Moglichkeit, fallweise zu unterscheiden, ob ein Objekt Aliase haben darf.

Das obige Beispiel stellt insofern kein grosses Problem dar, als der fehler-

hafte Umgang mit dem Aliasing durch unwartetes Programmverhalten

**Geheimisprinzip als**

**Teil der Spezifikation**

auffallt. Ein viel grosses Problem entsteht, wenn die Kapselung von Objekten (das Geheimisprinzip) Gegenstand der Spezifikation eines Programms ist, die Existenz von Aliasen also mit der Spezifikation nicht vereinbar ware. Dies ist bei allen sicherheitskrtischen Anwendungen der Fall, bei denen Daten geschützt werden mussen oder Funktionen nur durch autorisierte Benutzeninnen ausgefuhrt werden durfen. Gibt es dann Aliase von aussen auf diese Objekte als geheime Daten- oder Funktionstager, dann ist die Spezifikation nicht erfullt. Am Programmverhalten ist dies jedoch nicht zu erkenn.

Nachdem das Problem nun hinreichend klar geworden sein sollte, was kann man dagegen tun? zunächst einmal muss noch einmal Klargestellt werden, dass die Deklaration von Instanzvariablen als von aussen unzugeifbar (**private**) lediglich _Namen_ verbigt -- man kann über die Schnittstelle des Objekts nicht herausfinden, _wie_ es intern aufgebaut ist. Dieser Namenschutz (engl. name protection) ist das, was man landauftig (mit dem Wissen vom Aliasing-Problem) mit **Geheimisprinzip** (engl. **information hiding**) verbindet: Es verhindert, dass andere Klassen von der Existenz bestimmter Instanzvariablen abhangen, so dass diese problemlos geandert (z. B. umpenannt oder entfernt) werden können.

Das Geheimisprinzip vermag jedoch nicht zu verhindern, dass die Repra-

sentationsobjekte, deren Namen verborgen werden, noch andere Namen besitzen. Dies kann z. B. immer dann der Fall sein (und ist vom Objekt, das sein Implementationsgeheimnis wahren will, kaum zu verhindern), wenn ein Objekt seine Repräsentationsobjekte bei seiner Erzeugung von aussen geliefert bekommt (genau so, wie das in den obigen Beispielen in den Zeilen 1533, 1535 und 1540 der Fall war). Eine weitere Moglichkeit, die Kapselung zu durchbrechen, ist, selbst eine Referenz auf ein Repräsentationsobjekt herauszugeben, beispisweise durch einen Getter, aber das ware dann vom,,verbergenden" Objekt selbst zu verantworten (und zu verhindern gewesen).

Sobald also die Moglichkeit des Aliasing besteht, ist eine echte Kapselung über das Geheimisprinzip allein nicht mehr zur gewahrleisten. Man muss also das Aliasing irgendwie kontrollieren. Die Frage ist nur: Wie?

Eine Moglichkeit hatten wir bereits mehrfach angesprochen. Man kann

**ein Losungsansatz**

das Bestreben nach Kapselung als Ausdruck des Bestehens einer _Teil-Ganzes-Beziehung zwischen den Repräsentationsobjekten und dem Objekt, dessen Repräsentation sie ausmachen, verstehen. Die Teile sollen dabei dem Ganzen gehoren in dem Sinne, dass sie nicht zugleich auch Teile anderer Objekte sein können, und darüber hinaus auch nicht von andereren Objekten referenziert werden können. Letzteres kann man auf einfache Weise verhindern, wenn man aus den Objekten Wertobjekte macht und die verwendete Programmiersprache keine Zeiger auf Wertobjekte erlaubt. Von den in Kurseinheit 4 und Kurseinheit 5 genannten Programmiersprachen ist das jedoch nur in C#, und da auch nur im Safe mode, moglich, namlich wenn die,,Klasse" der Teil-Objekte per struct definiert wurde. Abgesehen von dieser Einschrankung ist eine solche Vorgehensweise nur selten ohne unerwunschte Nebenwirkungen -- sie bedeutet namlich immer auch, dass alle Objekte dieser,,Klasse" nur Wertobjekte sein und keine Referenzen haben durfen, was aber die Anwendungsdomane in der Regel nicht korrekt abbildet.

Vor diesem Hintergrund scheint der in Abschnitt 52.5.2 dargelegte Umgang Eiffels mit Referenz- und Wertvariablen ziemlich schlau ausgedacht zu sein. Zwar erlaubt Eiffel, auf Wertobjekte Referenzen zu haben (und somit zumindest theoretisch, dass ein Repräsentationsobjekt einen Alias besitzt), aber bei der Zuweisung einer Referenzvariable an eine Wertvariable wird immer eine (aliasfreie) Kopie des referenzierten Objekts erzeugt und zugewiesen, so dass kein Alias in die Repräsentation hinein entstehen kann. Umgekehrt wird bei der Zuweisung eines Wertobjekts an eine Referenzvariable immer eine Kopie des Wertobjekts erzeugt und die Referenz darauf angelegt. Es entsteht also faktisch kein Alias auf ein Wertobjekt, und als Wertobjekte angelegte Repräsentationsobjekte sind aliasfrei. Dumm ist nur, wenn man innerhalp der Kapsel Aliase auf Wertobjekte braucht.

Weitergehende Mechanism zur Aliaskontrolle in objektorientierten Programmiersprachen befinden sich derzeit alle noch in der Vorschlags- und Erprobungsphase und sollen hier deswegen nicht weiter behandelt werden.

## 59 Das Problem der mangelnden Skalierbarkeit

Zwar besteht jedes laufende objektorientierte Programm aus einer Menge von Objekten, jede Spezifikation eines solchen Programms besteht aber bei den heute gebrauchlichen klassenbasierten objektorientierten Programmiersprachen aus einer Menge von Klassen. Die strukturbbildende Einheit der objektorientierten Programmierung auf Programmechene ist daher die Klasse. Grosse Einheiten sind innerhalp der gangigsten objektorientierten Programmiersprachen nicht vorgesehen: Javas Packages und Ahnliche Konstrukte sind allenfalls Namensraume und Einheiten der Auslieferung -- der Status eines Sprachkonstrukts vergleichbar mit Klasse oder Methode kommt ihnen kaum zu.

Nun sind Klassen relativ feingranulare Gebilde. Zwar hindert einen nichts

daran, grose Klassen (mit Hunderten von Attributen und Methoden) zu

schreiben, aber dies gilt nicht nur als schlechter Stil, es spiegelt auch die Anwendungsdomane in aller Regel nicht angemessen wieder. Dort sind namlich alle grossen (komplexen) Dinge aus einfacheren zusammengesetzt, die, wenn sie selbst eine gewisse Komplexitat haben, selbst wieder aus kleineren zusammengesetzt sind usw. Dasselbe gilt auch für die Artefakte anderer Ingenieursdisciplinen: Bauplane sind in Komponenten und Unterkomponenten bzw. Systeme und Untersysteme strukturiert. Da wunscht man sich naturlich analoge Moglichkeiten in der objektorientietten Programmierung.

Nun ist es zwar moglich, Objekte mit Hilfe der Teil-Ganzes-Beziehung kursiv aufzubauen (und im oben diskutierten Rahmen auch zu kapslen, also Teile vollstandig hinter Ganzen zu verbergen), aber für Klassen gilt das nicht. Zwar ist es hier moglich, über sog. _innere Klassen_ (in Java) Klassen zu strukturieren, aber allein schon die Tatsache, wie relativ wenig davon Gebrauch gemacht wird, zeigt, dass es sich dabei um keinen besonders nutzlichen Mechanisme handelt.93 Tatsachlich ist es namlich -- wie schon in Kapitel 58 angesprochen -- so, dass Objekte einer Klasse nicht immer Teile von Objekten anderer Klassen sind (und schon gar nicht immer der gleichen Klassen), sondern vielmehr einzelne Exemplare (Instanzen) Teil sein und vielleicht sogar selbst Teile haben können. Man kann also die hierarchische Struktur objektorientietter Systeme genauso wenig auf Klassenebene vorschreiben, wie man den Aufbau einer Maschine anhand lediglich der Typen ihrer Teile (Schrauben etc.) beschreiben konnte (ohne festzulegen, wo jede einzelne Instanz genau hingenorte). Was man vielmehr brauchte, sind **Komponenten** als zusatzliches, von Klassen und Objekten verschiedenes Programmiersprachenkonstrukt.

Footnote 93: Das gilt allerdings nicht für ScALA, die _SCAlable language”– hier werden Singleton-Klassen, Objekte genannt, zur hierarchischen Strukturierung eines Programmiersprachen

Leider ist es mit der Einfuhrung von Komponenten in objektorientierte Programmiersprachen bislang noch nicht besonders weit. Das merkt man schon daran, dass keine weit verbreitete objektorientierte Programmiersprache das Schlusselwort **component** verwendet, ja nicht einmal verserviert. Stattdessen lasst man die Programmierrinnen alles in Form von Klassen definieren und Komponenten immer zur Laufzeit, per Aggregation von Objekten, zusammenbauer. So schwache Konzepte wie Pakete (Java) oder Assemblies (C#) können dabei keinesweg einen Komponentenbegriff ersetzen, da sie lediglich Klassen gruppieren (und dabei auch noch ignorieren, dass dieselbe Klasse Instanzen für Komponenten verschiedenen Typs liefern kann). Es ist meine personliche Vermutung, dass an dieser Front in den nachsten Jahren noch der groste Fortschritt erzielt werden kann.

## 60 Das Problem der mangelnden Eignung

To a woman with a hammer, everything looks like a nail.

Wie alle Ingenieurinnen verfallen objektorientierte Programmiererinnen gern dem Hammerprinzip: Wenn man einen Hammer in der Hand hat, sieht alles wie ein Nagel aus. Nicht alleAufgaben sind aber gleichermassen zur Losung per objektorientierter Programmierung geschaffen. Furiele logische und Suchprobleme sind beispielsweise _funktionale_ oder _logische Programmiersprachen_ weit besser geeignet; aber auch viele Batch- und Scripting-Probleme (in denen lediglich vorhandene Programme mit den richtigen Daten versorgt und angesto-Ben werden mussen) haben eher imperativ-prozeduralen denn objektorientierten Charakter.

Auch wenn pauschale Aussagen riskant sind, so erscheinen doch Probleme, die einen hohen algorithmischen Anteil und vergleichsweise simple Datenstrukturen verlangen, weniger geeignet für die objektorientierte Programmierung. Wie schon in Kapitel 56 erwahnt, verlangt die _,gute" objektorientierte Programmierung, den Code (die Funktionalitat) auf die Klassen aufzuteilen, die die Daten definieren, auf denen der Code arbeitet. Da groBere Probleme in der Regel auf durch verschiedene Klassen definierte Daten zugereifen mussen, wird der Code durch seine Datenbindung regelrecht zerfleddert.

Ein ahnlich gelagertes Problem hat man, wenn man Programme entwickelt, in denen es vor allem um Ablaufe geht. Hier mochte man, dass die Reihenfolge der Schritte, die auszufufren sind, in einem Stuck festgehalten wird (_Lokalitatsprinzip_!) und nicht auf zig Klassen aufgeteilt ist. In solchen Fallen steht das Interesse an der Struktur der Funktionen über dem an der Struktur der Daten -- dass hier die objektorientierte Programmierung nicht ideal ist, liegt eigentlich auf der Hand.

So hat man es bei der Wahl einer geeigneten Programmiersprache in der Praxis fast immer mit einem Abwagungsproblem zu tun. Wenn man sich für die objektorientierte Programmierung entscheidet, bleibt die Organisation der Funktionen auf der Strecke, wenn man sich für die prozedurale Programmierung entscheidet, werden die Daten auf kaum nachzuluzuelzhehende Weise hin- und hergeschickt oder sind global, was auch kein Idealzustand ist. Sprachen, die eine Mischung mehrerer Paradigmen erlauben, scheinen die Losung zu sein. für die Didaktik eignen sie sich jedoch weniger, schon weil sie Anfangerinnen mit ihrer grossen Auswahl an Konstrukten und der unüberschaubaren Anzahl von Alternativen, wie man ein einzelnes Problem losen kann, überfordern. C++ ist ein gutes Beispiel dafur.

Ein anderes Problem ist der Einsatz objektorientierter Programmierung in Verbindung mit relationalen Datenbanken. Zwar spiegelt ein gut entworfenes Datenbanksschema, genau wie ein gut entworfenes Klassenmodell, eine Strukturrie- rung der Anwendungsdomane wider, doch tun es beide mit ganz unterschiedlichen Mitteln: Wahrend relationale Datenbanken wertbasiert sind (alle Daten werden als Tupel primitiver Datentypen wie Zahlen und Zeichenketten dargestellt), sind objektorientierte Programme zeigerbasiert. Beziehungen werden in relationalen Datenbanken über die Verwendung gleicher Werte in _Schlusseln_ und _Fremschlusseln_ sowie über Join-Operationen hergestellt, in objektorientierten Programm über Referenzen und deren _Dereferenzierung (Navigation)_. Wikipedia Verebrung bzw. Subtyping, für die objektorientierte Programmierung charakteristisch, gibt es in relationalen Datenbanken gar nicht.94 Sollen also relationale Daten durch objektorientierte Programme verarbeitet werden, muss man sich an die Prinzipien der relationalen Welt anpassen und damit ein Gutteil dessen, was Objektorientierung ausmacht, aufgeben, wesegen man hier auch haufig von einem _Impedance mismatch_ spricht (das entsprechende deutsche Wort _Fehlanpassung" ist in diesem Zusammenhang ungebrauchlich).

Footnote 94: Dies ist strenggenommen nicht richtig: Schon der Standard SQL:1999 enthielt starke objektorientierte Anleihen. Ich bin mir jedoch nicht sicher, ob diese jemals in der Praxis angekommen sind.

Etwas anders gelagert ist der Fall, dass man eine relationale Datenbank dazu einsetzt, eine objektorientierte zu simulieren. In diesem Fall werden die Daten zunächst (wie in der gewohnlichen objektorientierten Programmierung) angelegt und nur zu Persistenz- und Synchronisationszwecken (bei Mehrbenutzerinnensystemen) in der Datenbank abgelegt. Die Abbildung der objektorientierten Klassenstruktur auf das relationale Schema wird dabei heute meistens durch ein sog. _Persistenzlayer_ erreicht -- das Programm selbst muss sich um die Datenhaltung nur auf sehr abstrakter Ebene kummern. Dennoch muss man auch hier die Frage stellen, warum man einer relationalen Datenbank den Vorzug vor einer objektorientierten gegeben hat -- am Ende, weil im betrieblichen Umfeld haufig bereits relationale Datenbanken mit gutem Ergebnis verwendet werden und die Umstellung auf Objektorientierung in der Datenhaltung mit unwagbaren Risiken verbunden scheint -- schlieBlich sind die Daten haufig der eigentliche Wert eines Softwaresystems.

Zuletzt, und beinahe paradoxerweise, ist auch die GUI-Programmierung

**GUI-Elementen** nicht unbedingt ein Hemspiel für die objektorientierte Programmierung.

Zwar kann man für die verschiedenen Arten von GUI-Elementen noch ganz gut Klassen angeben, die die Gemeinsamkeiten im Aussehen der in einem konkreten GUI verwendeten Objekte herausfaktorisieren, aber spatestens beim gemeinsamen Verhalten ist Schluss: Zwei Buttons beispielsweise unterscheiden sich nicht nur bezuglich ihrer Position und des angezeigten Texts, sondern auch darin, welche Aktion ausgefuhrt wird, wenn sie gedruckt werden. Da sich die Instanzen einer Klasse aber alle Methoden teilen, ist es nicht moglich, für verschiedene Buttons derselben Klasse verschiedene Implementierungen einer Methode anzugeben. Hier kann man lediglich versuchen, eine Indirektion einzubauen, in SMALITALK über einen Block, der die auszufuhrende Methode beinhaltet, in JAVA über anonymme innere Klassen, die für eine bestimmte Methodensignatur eine Implementierung liefern, die nur den Instanzen dieser (unbenannten) Klasse gehort, und in C++ sowie C# über Funktionszeiger (Delegates in C#). Von Haus aus besser geeignet scheint hier aber die prototypenbasierte Variante der objektorientierten Programmierung, wie in der Einleitung zu Kurseinheit 2 bermerkt (und wie sie ja auch in Form von JAVASCRIPT seit Jahren einen heimlichen Siegeszug feiert).

## 61 Losungen zu den Selbsttestaufgaben

**Selbsttestaufgabe 55.1 (Seite 306)**

Lesen Sie weiter!

[MISSING_PAGE_EMPTY:339]

**Kurseinheit 7: Objektorientierter Stil**

There does not now, nor will there ever, exist a programming language in which it is the least bit hard to write bad programs.

Lawrence Fion

Egal, wie formal sie auch sind: Programmiersprachen sind Sprachen und erlauben einer Autorin damit, sich auf eine personliche Art und Weise auszudrucken. Dabei bestimmt die Ausdrucksweise nicht den Inhalt des Programms (seine Funktion), sondern seine Qualitat, also z. B. wie effizient ein gegebenes Problem damit gelost wird oder wie verstandlich die Formulierung der Losung für die Betrachterin ist. Besonders die Verstandlichkeit hat etwas mit Schreibtstil zu tun; neben ihr spielen aber auch noch andere Parameter in Stilfragen eine Rolle, so z. B. Mode und Asthetik (Eleganz).

So hat es fraglos in den letzten Jahrzehnten eine Wandlung in Stilfragen gegeben, und zwar weg vom mathematisch-pregnanten hin zum prosaisch-verbosen Stil. Das folgende Beispiel soll davon einen Eindruck geben:

1556 PROGRAMM marriage(input,output);
1557 {Problem der stabilen Heirat}
1558 CONST n = 8;
1559 TYPE man = 1.. n; woman = 1.. n; rank = 1.. n;
1560 VAR m: man; w: woman; r: rank;
1562 wmr: array [man, rank] OF woman;
1563 mwr: ARRAY [woman, rank] OF man;
1564 rmw: ARRAY [man, woman] OF rank;
1565 rwm: ARRAY [woman, man] OF rank;
1567 x: ARRAY [man] OF woman;
1568 y: ARRAY [woman] OF man;
1569 single: ARRAY [woman] OF BOOLEAN;
1570
1571 PROCEDURE print;
1572 VAR m: man; rm, rw: INTEGER;
1573 BEGIN rm := 0; rw := 0;
1574 FOR m := 1 TO n DO
1575 BEGIN write(x[m]:4);
1576 rm := rm + rmw[m,x[m]]; rw := rw + rwm[x[m],m]
1577 END ;
1578 writeln(rm:8, rw:4)
1579 END (print) ;
15801581PROCEDURE try(m: man);
1582 VARr: rank; w: woman;
1583
1584FUNCTIONstable: BOOLEAN;
1585 VARpm: man; pw: women;
1586 i, lim: rank; s: BOOLEAN;
1587 BEGIN s: = TRUE; i := 1;
1588 Whittle (i < r) AND s D0
1589 BEGIN pw : wmr[m,i] ; i := i+1;
1590 IF NOT single[pw] THEN
1591 s := rvm[pw,m] > rvm[pw,y[pw]]
1592 END ;
1593 i := 1; lim := rvm[w,m];
1594 WMILE (i < lim) AND s D0
1595 BEGIN pm := mwr[w,i] ; i := i+1;
1596 IF pm < m THEN s := rmv[pm,w] > rmv[pm,x[pm]]
1597 END ;
1598 stable := s
1599 END (stable) ;
1600
1601 BEGIN {try}
1602 FOR r := 1 to n D0
1603 begin w := wmr[m,r];
1604 IF single[w] THEN
1605 IF stable THEN
1606 BEGIN x[m] := w; y[w] := m; single[w] := FALSE;
1607 IF m < n THEN try(succ(m)) ELSE print;
1608 single[w] := TRUE
1609 END
1610 END
1611 END (try);
1613 BEGIN
1614 FOR m := 1 TO n D0
1615 FOR r := 1 TO n D0
1616 BEGIN read(wmr[m,r]) ; rmw[m,wmr[m,r]] := r
1617 END;
1618 FOR w := 1 TO n D0
1619 FOR r := 1 TO n D0
1620 BEGIN read(mwr[w,r]); rvm[w,mwr[w,r]] := r
1621 END;
1622 FOR w := 1 TO n D0 single[w] := TRUE;
1623 try(1)
1624 END ;

Es handelt sich dabei um ein Pascal-Programm zur Losung des Problems der stabilen Heirat, wie es in dem Klassiker,,Algorithmen und Datenstrukturen" von Niklaus Wirth nachzulesen ist. Eine mir leider entfallene Quelle soll ubrigens gesagt haben, eine Untersuchung habe hervorgebracht, dass ein bedeutender Anteil aller Variablen in Programmen,,i" heisse. Nun wurden in obigem Beispiel die Variablen nicht,,i", sondern,,i",,,m",,,w" usw. genannt, aber das grundlegende Problem bleibt das gleiche: Man muss sich schon ziemlich in das Programm bzw. den dazugehrenden Text vertiefen, um zu erfassen, wofur die Variablen stehen.

Real programmers can write Fortran in any language.

Heute ist es ublich, Bezeichner (Namen für Module, Typen, Variablen, Prozeduren und Funktionen) in einem Programm so zu wahlen, dass Kmomentare bzgl. der Bedeutung des jeweiligen Programmelements unnotig sind, da sie nicht viel mehr ausdrucken können, als es der Bezeichner in seinem jeweiligen Kontext ohnen hunt. Dies geht sogar so weit, dass Leute wie Kent Beck (Mitinitiator und Verfechter des sog. Extreme Programming, Smalltalk-Veteran) meinen, ein gut geschriebenes objektorientiertes Programm brauchte gar keine Kommentare. Dem mochte ich entgegenhalten, dass manchmal die Losung eines Problems in seiner verstandlichsten Form um vieles uneleganter ist als eine, die mit einer gewissen Raffinesse daherkommt, sich dafur aber nicht jeder unmittelbar erschlieSt. In solchen Fallen ist die Versuchung gross, sich für die geistreichere Variante zu entscheiden und sie, für diejenigen Leserinnen, die einer nicht auf Anhieb folgen können, mit einem erklarenden Kommentar zu versehen. Nicht zuletzt sind es ja gerade die alles andere als offensichtlichen Algorithm, die ihren Autorinnen zu Beruhmtheit verholfen haben, und wer wurde nicht gern hier und da eine eigene Marke setzen. Kryptische Namen zu verwenden ist jedoch niemals ein Zeichen von Genialitat.

Wir kommen also gleich zur Stilregel Nummer 1 der objektorientierten Programmierung.

## 62 Namenwahl

Gegen die Verwendung langer, sprechender Bezeichner kann man einwenden, dass der Programmtext dadurch übermäbig lang wird. Anweisungen, die sonst in eine Zeile gepasst hatten, mussen u. U. mehrfach umgebrochen werden, was die Lesbarkeit nicht gerade erhoht. Auch hort man hier und da, dass lange Namen für die Programmiereerin zusatzliche Schreibarbeit bedeuten. Letzteres Argument kann man jedoch kaum gelten lassen, da die meisten Entwicklungsupebungen über eine automatische Vervollstandigungsfunktion verfugen, die einem das Tippen abnimmt (und damit auch Tippfehler aufdeckt oder vermeidel). Das erste Argument ist schon schwieriger zu entkraften: Natürlich sind pragnante Namen geschwatzigen vorzuziehen und auch in der Programmierung liegt die Wurze in der Kurze -- insbesondere sind lange Namen, die sich nur geringfugig unterscheiden (und das auch noch wenig offensichtlich), zu vermeiden. Als Faustregel ist ein Name dann gut gewahlt, wenn man alle Ausdrucke, in denen er vorkommt, schnell verstehen kann (und nicht nur, aufgrund falscher Assoziationen und Vermutungen, zu verstehen glaubt). Eine sorgfaltige Programmiererin wird sich also haufiger dabei beobachten, wie sie über einen passenden Namen für ein Programmelement langer nachsinnt. Diese Zeit ist jedoch gut investiert.

### 62.1 Verwendung von Abkurzungen

Abkurzungen sind nicht grundsatzlich zu vermeiden -- im Gegenteil, wenn sie etabliert sind und man davon ausgehen darf, dass eine Leserin des Programms sie kennt, ist ihre Verwendung (aus oben angefuhrten Gründen gegen zu lange Namen) sogar angezeigt. Auf hausgemachte Abkurzungen, deren Bedeutung man nur selbst kennt, sollte man hingegen verzichten.

Bei der Programmierung mit Java und anderen typisierten objektorien-tierten Programmiersprachen begegnet man haufig dem Phanomen, dass Typen und Variablen gleich heissen, sich nur in der Gross- bzw. Kleinschreibung ihres Anfangsbuchstabens unterscheiden. Ein typisches Beispiel dafur ist das folgende:

1625 **Iterator iterator = list.iterator():**

In diesen Fallen, wenn es keinen besseren Namen für die Variable gibt, ist es vollkommen legitim, eine Abkurzung für den Variablennamen zu wahlen, insbesondere dann, wenn die Sichtbarkeit der Variable auf die unmittelbare Umgebung der Deklaration beschrankt ist:

1626 **Iterator iter = list.iterator():**

oder
1627 **Iterator 1 = list.iterator():**

sind also legitim. Sobald dies jedoch nicht der Fall ist (typischerweise schon bei der Deklaration von Instanzvariablen), sollte der lange Name bevorzugt werden. Dies gilt auch für den Fall, dass der Typ der Variable aus dem Kontext abgeleitet werden kann und deswegen nicht mehr angegeben wird (_Typinferenz_).

### 62.2 Namenskonventionen

Haufig findet man in einzelnen Projekten und nicht selten in ganzen Firmen Namenskonventionen vor, an die sich alle halten sollten. Namenskonventionen erleichtem nicht nur die Bezeichnenwahl (indem die Programmiererin sich an bestimmte Regeln halten kann, wird ihre schopferische Freiheit eingeschrankt, was man durchaus auch als Entlastung empfinden kann), sie erleichtern auch das Lesen, weil die Leserin, die die Konventionen kennt, die Bedeutung des Bezeichners bzw. des dahinterstehenden Programmelements leichter eenschlusseln kann und sie sich somit schneller zurechtfindet. Allerdings ist es dazu notwendig, dass die Namenskonventionen genau festgeschrieben sind und dass sich alle darauf einigen -- wenn namlich jede ihre individuelle Auslegung der Regel hat, dann kann eine (vermeintliche) Namenskonventionen mehr Verwirung stifften als nutzen.

It would be a mistake to protest against the rules... on the grounds that they limit developer creativity. A consistent style favors rather than hampers creativity by channeling it to where it matters. A large part of the effort of producing software is spent reading existing software and making others read what is being written. Individual vagaries benefit no one; common conventions help everyone.

Bertrand Meyer

#### Mechanische (syntaktische) Namenskonventionen

Eine gangige Namenskonvention ist beispielsweise, Namen von Interfacetypen mit einem grossen _1" beginnen zu lassen. Andere Namenskonventionen verlangen, dass Bezeichner, die für ein Objekt oder einen Wert stehen (also Variablen und Funktionsnamen) den Typ dieses Objekts oder Werts widerspiegelen -- die sog. _ungarische Notation_, von der es allerdings verschiedene Auslegungen gibt. Nach einer, eher dummlichen, Auslegung mussen beispielsweise alle Variablen, die Strings bezeichnen, mit _st" beginnen (eine Information, die Compiler und IDE aber ohnehin bereithalten und die deswegen nicht noch den Namen belasten muss). Nach einer sinnvolleren Auslegung sollten Variablennamen um die Verwendung ihres so bezeichneten Inhalts erganzt werden, also die Funktion des durch sie bezeichneten Objekts oder Werts innerhalb des Kontextes, in dem die Variable gultig ist, angeben. Diese kontextbezogene Funktion kann in der objektorientierten Programmierung jedoch auch durch die Verwendung eines Interfaces anstelle einer Klasse als Typ bei der Deklaration der Variable ausgedruckt (und somit auch vom Compiler überpruft) werden.

#### Grammatiklach-inhaltliche (semantische) Namenskonventionen

Oberaus angemessen, wenn auch nicht immer in letzter Konsequenz ein-

klassen zuhalten, ist, die verschiedenen Wortarten einer naturlichen Sprache für verschiedene Arten von Programmelementen zu verwenden. So legt beispielsweise der in Kurseinheit 1, Kapitel 7 beschriebene Zusammenhang zwischen Klassen und Allgemeinbegriffen nahe, dass man für Klassennamen Substantive verwendet. Tatsachlich ist es eine vielzitierte objektorientierte Technik, in der Analysephase eines Projekts alle Substantive der Spezifikation zu extrahieren, um auf der Basis der so gewonnenen Liste die Menge der Klassen eines Systems zu identifizieren.

Methoden, die eine Aktion implementieren (_Befehle_ in Eiffel, s. Kursein-

heit 5, Abschnitt 52.2), wird man aufgrund ihres pradikativen Charakters mit Verben benennen, wobei es eine Stilfrage ist, ob man die Infinitu- oder die Imperatiform (im Englischen ubrigens kein Unterschied in der Erscheinungsform) bevorzugt. Personlich fuhle ich mich hier an keine Regel gebunden ausser an die, dass Ausdrucke durch meine Namenwahl moglichst lesbar werden. So klingt1628problemloesen

(Infinititiform) in meinen Ohren besser als

1629problemloesen

(Imperatiform),

1630ausgabegeareatdrucke:einenString

(Imperatiform) klingt dagegen besser als

1631ausgabegeareatdrucken:einenString

(Infinititiform). Man konnte naturlich der imperativen Form ein Reflexivpronomen hinzufugen wie etwa in

1632problemloeselich

aber das ist eher unublich (obwohl nicht ohne Charme!). Verberganzungen wie Prapositionen verwendet man in Smalltalkdauend (schon um mehrere Parameter voneinander abzusetzen); in Sprachen wie Java fugt man einem allgemeinen (und haufig überladenen) Verb dann gelegentlich noch ein Substantiv als Objekt des Pradikats hinzu, wie in

1633vectoraddElement(anElement).

Gerade dieses Beispiel ist jedoch nicht unumstritten, da,,Element" hier gewissermassen redundantist -- wenn es mehrere Methoden namens,,add" gibt, kann man sie auch mittels ihrer Parametertypen unterscheiden (also _überladen_). So heisst die entsprechende Methode im JDK heute auch nur noch **add(.)**.

Keine Verben, sondern Adjektive (oder Kopula plus Pradikatsnomen) verwendet man hingegen für Methoden, die eine Abfrage darstellen (Queries; s. Abschnitt 52.2), wie etwa

1634stapelvoll

bzw.

1635stapelistVoll

oder

1636mengehatElement:einElement

Fur Instanzvariablen verwendet man unterschiedliche Wortarten, und

**Instanzvariablen** zwar abhangig davon, ob eine Instanzvariable ein Attribut oder eine Beziehung reprasentiert. Wenn es sich um ein Attribut handelt, das eine mehrwertige Qualitat ausdruckt (wie Grosse, Farbe etc.), dann wird man den Namen der Qualitat verwenden und damit ein Substantiv (ggf. in Kleinschreibung). Wenn es sich um ein zweiwertiges (Boolesches) Attributhandelt, dann nimmt man das entsprechende Adjektiv (wie etwa **leer**), ein Gerundiuum (z. B. **laufend**) oder ein Partizip (wie etwa **geloest**). für Instanzvariablen, die Beziehungen ausdrucken, nimmt man geme den Namen der Gegenrolle, also beispielsweise **mutter** in einer Kind-Mutter-Beziehung. Bei :\(n\)-Beziehungen nehme ich personlich gern den Plural, also z. B. **kinder** (statt **kind**) für die umgekehrte Richtung.

Interfaces sind zwar wie Klassen Typen, aber bezeichnen keine Allgemein-

begriffe, sondern eher _Rollen_, die die Objekte, die konkrete Auspragungen der Allgemein-

begriffe sind, spielen können. Rollen werden aber, genau wie Allgemeinbegriffe, haufig

durch Substantive bezeichnet:,,Mutter" ist ein Beispiel hierfur. Andere Rollen, insbesondere die, die mit Parametern von Methoden verbunden sind, werden haufig durch Adjektive bezeichnet: **Druckbar** beispielsweise konnte der Parametertypp einer Methode drucken sein, den das zu druckende Objekt haben muss. Tatsachlich enden viele der gebrauchlichen Interfacenamen im Englischen auf,,able" oder,,ible", so z. B. bei **Serializable**.

Eine ganz interessante Option ergibt sich ubrigens für Programmiererinen, deren Muttersprache nicht Englisch ist: Man hat hier die Moglichkeit, bei der Wahl der Bezeichner zwischen zwei Sprachen zu wahlen und damit eine zu-satzliche Form der Differenzierung einzusetzen. Ich personlich verwende dann gerne für Begrifflichkeiten aus der Anwendungsdomane (also dem Gegenstandsbereich, mit dem sich das Programm befasst) deutsche Bezeichner und für solche aus der technischen Umsetzung (Hilfsklassen etc.) englische. Alternativ kann man naturlich auch alle selbst beigesteuerten Programmelemente auf Deutsch benennen, um sie von den aus Bibliotheken und Frameworks zusammengeklaubten zu unterscheiden.

## 63 Formatierungskonventionen

Neben den reinen Namenskonventionen einigt man sich haufig auch auf Formatierungskonventionen (zusammen mit Namenskonventionen und anderen Richtlinien englisch als _coding conventions_, deutsch oft auch, und etwas zu allgemein, als _Programmiersti_ bezeichnet). Diese regeln so Dinge wie Einruckungen und an welchen Stellen Zeilenumbruche, Leerzeilen und Leerzeichen einzufugen sind. Sie dienen damit ebenfalls der besseren Lesbarkeit.

**White space contributes as much to the effect produced by a software text as silence to the effect of a musical piece.**

Sertrand Meyer

Formatierungskonventionen sind aber nicht nur eine Richtschnur für die

Einzelne, die sich vielleicht unsicher ist, ob bzw. wo sie ein Leerzeichen

einfugen soll -- sie vermeiden auch den Effekt, dass jede Programmiererin im Team ihre eigenen Vorlieben pflegt, was in der Spitze dazu fuhrt,dass wenn eine Programmiiererin den Code einer anderen anfasst, sie zunächst einmal damit beginnt, diesen so zu formatieren, dass er ihren Lesgewohnheiten entspricht. Die ursprungliche Autorin reagiert naturlich emport und wird nichts anderes tun, als dies bei nachster Gelegenheit wieder ruckgangig zu machen, sprich zu ihren eigenen Vorlieben zuruckzukehren. Dies ist alles andere als produktiv.

Ein wirksames Gegenmittel gegen solch Energieverschwendung sind automatische Condeformatierer, die auf Knopfdruck bestimmte Codierungs- konventionen umsetzen. Wo immer verfugbar, sollte man sich zur Angewohnheit machen, diese auch einzusetzen, selbst wenn man allein arbeitet, schon um sich mit der Entwicklung des personlichen Programmierstils nicht zu weit von dem, was allgemein ublich ist, zu entfernen. Die Programmierung ist nicht geeignet, Individualitat zum Ausdruck zu bringen, geschweige denn, sie voll auszuleben.

## 64 Kurze Methoden

Wer sich den Quellcode objektorientierter Programme ansieht, der wird auffallen, dass die Methoden im Mittel ziemlich kurz sind. Wie bereits in Kurseinheit 6, Kapitel 56 enwahnt, ist dies Folge des Umatandes, dass in der objektorientierten Programmierung die Funktionalitat auf Basis der Daten, von denen sie abhangt, aufgebrochen und aufgeteilt wird. Sobald eine Funktion verschiedenartige Daten manipulert (also Objekte, die Instanzen verschiedener Klassen sind), ist es wahrscheinlich, dass diese Funktion nicht zur Ganze in einer Methode implementiert wird.

Was hier zunächst wie eine unmittelbare Folge des objektorientierten Paradigmas erscheint, hat sich zu einem objektorientierten Stil weiterentwickelt: Eine typische objektorientierte Programmiererin scheut sich nicht, Methoden zu schreiben, die nur aus einer Zeile bestehen (oder die nur eine Anweisung, wenn auch mit geschachtetlen Ausdrucken, enthalten) -- im Gegenteil, sie fuht sich sogar gut dabei, denn was sie da gerade produziert, gilt als objektorientierter Stil. So ist es sogar ublich, Teile einer Methode in eine neue auszulagern (das Extract-method-Refactoring, das einige vielleicht aus Eclupse und ahnlichen Entwicklungsupgebungen kennen), auch wenn dieser Teil (zunächst) ausschliesslich von seiner ursprunglichen Position aus aufgerufen wird, wenn es nur der besseren Lesbarkeit dient (also insbesondere Wiederverwendung keine Rolle spielt). Ein positiver Begleiteffekt dieser starken Zergliederung von Funktionalitat ist die hohe Dichte an Bezeichnem in objektorientierten Programmen: Da jede Teilfunktion, die in eine Methode ausgelapert wird, einen eigenen, eindeutigen (bis auf überladen/überschreiben) Namen haben muss, wird die Programmiererin dazu gezwungen, sich standig (in Form der Namenwahl für Bezeichner) dazu zu aussern, was sie gerade macht.

## 65 Deklarativer Stil

Einhergehend mit kurzen Methoden und sprechenden Bezeichnern ist ein deklarativer Programmierstil für die objektorientierte Programmierung typisch: Die Ausdrucksform bennutt sich mehr um das Was als um das Wie. Der Effizienggedanke ist dabei sekundar -- mogliche Optimierungen werden dem Compiler überlassen und ansonsten für spater aufgehoben, wenn sich heraustellen sollte, dass die Abarbeitung einer deklarativ formulierten Losung zu ineffizient ist.

Da die objektorientierte Programmierung aber ihrem Wesen nach eher imperativ als deklarativ ist, wird sich das Deklarative im wesentlichen auf den Aufruf von Methoden beschranken, die nach dem benannt sind, was sie tun. So ist es in der objektorientierten Programmierung durchaus ublich, einzelne Schleifen, in denen beispielsweise ein Element gesucht wird, aus einem Methodenrumpf in eine eigene Methode zu verbannen und durch einen entsprechenden Methodenaufruf zu ersetzen. Das Programm liest sich also nur deklarativ und ist es nicht wirklich -- es handelt sich ja auch nur um einen Stil.

Ein Beispiel für einen deklarativen Programmierstil geben die folgenden Gegenüberstellungen (Atome und Literale sind hier Konzepte aus der Aussagenlogik):

```
1637auswerten
1638Aatomauswerten=negiertnot
```

(deklarativ) in einer Klasse Literal mit Instanzvariable atom anstelle von

```
1639auswerten
1644negiert
1641ifFalse:[^atomauswerten]
1642iftrue:[^atomauswertennot]
```

(imperativ) oder

```
1644auswerten
1644(literalecollect:[.:1|1auswerten])includes:true
```

(deklarativ) in einer Klasse Klausel mit Instanzvariable literale anstelle von

```
1645auswerten
1646|answer|=false.
1648literaledo:[:.1|answer:=answeror:1auswerten]
```

(imperativ). Es davert eine Weile, bis man sich das Imperative abgewohnt hat, aber es lohnt sich.

Fur beide Alternativen der Methode auswerten in Klasse Klausel gibt es ubrigens eine Shortcut-Variante (die so heißt, weil die Iteration ggf. vorzeitig abgebrochen wird):

[MISSING_PAGE_FAIL:349]

die Verwendung bestimmter Bibliotheksklassen aus -- man denke nur an die allgegenwartige Verwendung des Collection-Frameworks, ohne das Programmiererinnen zur standigen Abfassung ewig gleichen Codes verdammt waren.

Zum objektorientierten Programmierstil gehort es, eine Losung eines konkreten Problems moglichst umfassend aus existierenden, idealerweise verbreiteten und bewahrten Bibliotheken zusammenzieklauben. Jede nicht selbst geschriebene Programmzeile ist ein Gewinn, jede Implementierung einer noch so kleinen Funktion, die es bereits in irgendeiner Bibliothek gibt, ist ein Verlust. Dabei sind die Vorteile der Verwendung von Bibliotheken manningfaltig: In der Regel können Sie voraussetzen, dass die Implementierungen korrekt sind (und Probleme und Sonderfalle berucksichtigen, an die Sie im Traum nicht gedacht hatten), die Wartung und Anpassung übernehmen andere für Sie und nicht zuletzt durfen Sie bei weit verbreiteten Bibliotheken voraussetzen, dass deren Funktionalitat auch anderen Programmiererinnen bekannt ist, so dass die Verwendung einer Bibliotheksklasse keiner weiteren Erklarung bedarf. Ihr eigener Beitrag wird dadurch klein und überschaubar, was man Ihnen in keinem Fall als Faulheit oder Arbeitsverweigerung auslegen sollte95, sondern als wahre Grosse: Sie kennen das Werk anderer, Sie wissen es zu schatzen und zu nutzen.

Footnote 95: Ganz im Gegenteil: Ich würde es als Unterlassung ansehen, wenn sich jemand weigert, sich erst in Bibliotheken umzusehen, bevor sie mit der Entwicklung eigener Ideen beginnt.

## 67 Ausgewogene Verteilung

Ein weiteres Kennzeichen der objektorientierten Programmierung ist, dass Klassen nicht ins Uferlose wachsen. Wenn der Methodenumfang einer Klasse immer weiter ansteigt, wird die erfahrene objektorientierte Programmiererin bald den Verdacht schopfen, dass es sich bei der Klasse in Wirklichkeit nicht um eine, sondern um mehrere handelt. Dafur gibt es zwei Erklarungen:

1. Die Klasse steht nicht für _eine_ Abstraktion der Anwendungsdomane, sondern für mehrere. In diesem Fall sollte die Aufteilung der Klasse in mehrere -- eine für jede Abstraktion -- leicht fallen: Man ordnet zunächst die Daten den Abstraktionen (Allgemeinbegriffen) zu und lasst dann die Methoden den Daten folgen.
2. Die Klasse steht zwar für _eine_ Abstraktion der Anwendungsdomane, aber dies auf einem hoheren Abstraktionsniveau als das der Implementierung, die Sie gerade betrachten. Dafur gibt es wiederum mindestens zwei mogliche Erklarungen:* Die Abstraktion ist eine Generalisierung (s. Kurseinheit 1, Abschnitt 9.1) und Sie haben all deren _Spezialisierungen_ in einer Klasse zusammengefasst. In diesem Fall mussen Sie lediglich die unterschiedlichen Spezialisierungen identifizieren und die jeweils darauf bezogenen (dafur charakteristischen) Daten und Funktionen in neu zu schaffenden Subklassen verlagern. Lediglich das allen Fallen gemeinsame Protokoll verbleibt dann in der (idealerweise abstrakten) neuen Superklasse. Ein guter Indikator für diesen Fall ist das wiederholte Vorkommen _gleicher Fallunterscheidungen_, insbesondere dann, wenn diese Fallunterscheidungen die Art der Objekte betreffen (vgl. dazu auch das sog. Replace-conditional-with-polymorphism-Refactoring).
* Die Abstraktion ist eine _Aggregation_ (oder _Komposition_, s. Kurseinheit 1, Abschnitt 2.3), also eine Zusammensetzung eines Ganzen aus mehreren Teilen. In diesem Fall mussen Sie die Teile als logische Einheiten identifizieren und dafur neue Klassen formulieren. für den Fall, dass diese neuen Klassen außerhalb der Abstraktion keine Bedeutung haben, können Sie in Erwagung ziehen, sie als innere Klassen zu deklarieren (wenn lhre Programmiersprache das erlaubt), um so den Namensraum nicht zu überfrachten und die von anderen wahrgenommene Zahl der Klassen nicht unnotig zu vergrossern.

## 68 Das Gesetz Demeters (Law of Demeter)

Eine der klassischen Arbeiten zum Thema objektorientierter Programmierstil ist die zum sog.

**Law of Demeter** von Lieberherr, Holland und Riel. Demeter ist ein CASE-Werkzeug, das selbst kaum weiter Verbreitung gefunden hat und das wohl heute weitgehend unbekannt ware, wenn nicht eben dieses Gesetz Demeters es zu einiger Bekanntheit gebracht hatte.

### Bedeutung

Das Gesetz Demeters besagt nicht mehr, als das Nachrichten nur an Objekte versendet werden durfen, die der Sender selbst kennt oder erzeugt. Dabei ist Kennen ganz im Sinne von Kurseinheit 1 zu verstehen: Ein Objekt kennt ein anderes, wenn es in direkter Beziehung dazu steht, wenn es also auf eine Variable direkt (also ohne den Umweg über ein anderes Objekt) Zugriff hat, die das andere Objekt benennt. Es kennt das andere Objekt dauerhaft (oder zumindest für eine langere Dauer), wenn es sich bei der Variable um eine Instanzvariable handelt, und temporar, wenn es sich bei der Variable um den formalen Parameter einer Methode handelt (wobei die Dauer des Kennens dann auf die Dauer der Abarbeitung der Methode beschrankt ist, es sei denn, der formale Parameter wird einer Instanzvariable zugewiesen). Temporare (lokale) Variablen werden beim Gesetz Demeters nicht mitgezahlt.

Das Gesetz Demeters wird typischerweise verletzt, wenn Nachrichten an Objekte gesendet (Methoden auf Objekten aufgerufen) werden, die selbst nur als Ergebnis eines Nachrichtenausdrucks (Methodenaufrufs)vorliegen. Dies ist in der Regel bei Kettenaufrufen der Fall (s. u.), kann aber auch über eine zwischenzeitliche Zuweisung zu einer temporaren Variable erfolgen.

Sinn und Zweck des Gesetzes Demeters ist, die Kopplung und damit die **Ziel des Gesetzes**Entwurfsabhangigkeiten zwischen Klassen zu verringern. Wird das Gesetz Demeters verletzt, kann die Anderung (des Protokolls) einer Klasse dazu fuhren, dass auch Klassen ange-passt werden mussen, die selbst in keiner unmittelbaren Beziehung zu der Klasse stehen (sondem eben nur in einer mittelbaren, die nach dem Gesetz vermieden werden soll).

Das Gesetz Demeters wird oft (und leicht verkurzt) in folgender Phrase zusammengefasst:

\begin{tabular}{l} Bezogen auf Smalltalk heißt das, dass Methodenaufrufe zwar geschachtelt, aber nicht verkettet erfolgen durfen: \\
1662 a doX \\ ist also erlaubt, wenn **a** eine Instanzvariable oder ein formaler Parameter ist, ebenso \\
1663 a doX: b doY \\ wenn für b dasselbe gilt, nicht jedoch \\
1664 a doX doY \\ oder \\
1665 \\
1666 b := a doX. \\
1667 b doY \\ \end{tabular}

Man beachte, dass Demeters Gesetz faktisch eine neue, kontextabhangige _Zugreifbarkeits-regel_ einfuhrt: Eigenschaften von Objekten, die ein Objekt nicht selbst kennt, sind für das Objekt gleichgestellt mit denen von Objekten, die es zwar selbst kennt, auf die es aber nicht zugreifen darf.

### Automatische überprufung

Man kann sich fragen, ob sich die Einhaltung des Law of Demeter so wie die Einhaltung der Zugreifbarkeitsregeln automatisch überprufen lasst. Dabei gibt es aber ein Problem: Das Gesetz ist namlich oben in Termini von Objekten, nicht von Variablen oder Typen formuliert. Eine überprufung wurde also die Auswertung von konkreten Zuweisungen und damit des dynamischen Programmflusses erfordern, die aber mechanisch extrem aufwendig bis gar nicht durchzufuhren ist. Stattdessen prufen automatische Checker des Law of Demeter zumeist lediglich die Variablendekarationen und ob alle Methodenaufrufe einer Klasse nur auf Ausdrucken erfolgen, die den Typ einer Instanzvariable oder eines formalen Parameters (wenn der Aufruf au s einer Methode heraus erfolgt, was meistens der Fall ist) haben. Daraus folgt, dass eine solche Prufung in smalltalk nicht moglich ist (da Ausdrucke nicht typisiert sind).

Was aber tun, wenn man die Funktion von Ausdrucken wie oben haben und zugleich Demeters Gesetz folgen mochte? Die Antwort ist einfach: Man erweitert das Protokoll der Klasse des ersten Nachrichtenempfangers um die Methode(n), die man nicht verkettet aufrufen darf, also beispielsweise die Klasse des von **a** benannten Objekts um die Methode **doY**. Da **a** das Ergebnis von **doX**, nennen wir es **b**, irgendwo herhaben muss (sonst konnte es es ja nicht zuruckgeben), kann auch **a** die Methode **doY** aufrufen und das Ergebnis zuruckgeben. Die Implementierung von **doY** wurde dann durch **a** **b** **doY** abgeschlossen.

Komplizierter wird die Sache jedoch, wenn die Verkettung langer ist, wenn also der zu vermeindende Ausdruck **a** **doX** **doZ** heissen wurde, denn dann musste auch noch **doZ** zur Klasse von **a** hinzugtefugt und mit entsprechenden Implementierungen versehen werden. Man ahnt schon, wozu das fuhrt: zu einem Wachstum des Protokolls von **a**.

### Ein Beispiel

Ein konkretes Beispiel für die Verletzung des Law of Demeter ist die folgende alternative Implementierung der Methode **auswerten** in der Klasse **Klausel** (Zeilen 1650-1652):

```
1666auswerten
1669literale
1670detect:[:l|
16711negiert
1672ifTrue:[1atomwertnot]
1673ifFalse:[1atomwert]
1674ifNone:[^false].
1675Atrue
```

Hier wird (in Zeilen 1672 und 1673) zunächst **atom** an **l** (ein Literal, das dem Empfanger der Methode, einer Klausel, bekannt ist) geschickt und dann an das Ergebnis, ein Atom, die Nachricht wert. Diese Verkettung ist ein VerstoB gegen das Gesetz Demeters. Die Musterlosung

```
1676auswerten
1677literaledetect:[:l|lauswerten]ifNone:[^false].
1678Atrue
```

enthalt diesen Verstoss nicht. Dafur aber andere.

Versuchen Sie, bevor Sie weiterlesen, weitere Verstossegen das Gesetz Demeters in dem Beispiel zu finden.

Der erste Verstoss ergibt sich aus der Umsetzung der :\(n\)-Beziehung zwischen Klausel und Literalen über Zwischenobjekte. Eine Klausel kennt genaugenommen nicht ihre Literale direkt, sondern das Zwischenobjekt, in diesem Fall eine Instanz der Klasse **Set**. So stellt bereits der Aufruf von **atom** bzw. **auswerten** auf der Variable **1** eine Verletzung des Law of Demeter dar. Etwas deutlicher sieht man das, wenn man anstelle einer Menge und des Iterators **detect** : ein Array und eine Zahlschleife verwendet:

1679 **1 to: literale size do: [ :i ] (literale at: i) auswerten -**

Bei der Verwendung von Collections als Zwischenobjekte muss man also immer eine Ausnahme von Demeters Gesetz machen.

Der zweite Verstoss findet sich in Zeile 1672: **atom** wert not ist ein verketteter Ausdruck derselben Qualitat wie **1 atom** wert (selbe Zeile). Die Losung ware hier, der Klasse **Atom** eine Methode **not** zu spendieren, die den negierten Wert zuruckliefert, aber warum das besserer Stil sein soll, ist kaum noch zu begründen. Auch wenn dieses Problem in Java und Co. nicht existiert (da hier die logische Negation keine Nachricht/Methode, sondern ein primitiver Operator eines primitiven Datentyps ist), so zeigt es doch die Grenzen des Law of Demeter auf. So ist das Gesetz auch nicht allgemein anerkannt, sondern umstritten; dennoch sollte man es verinnerlichen und sich bei Kettenausdrucken stets fragen, ob nicht eine Verlagerung einer hinteren Methode in eines der Objekte auf der Strecke sinnvoll ware.

## 69 Klassenhierarchie

Der Begriff des Programmierstis kann weiter gefasst werden, als dies in den bisherigen Kapiteln dieser Kursenheit der Fall war. Tatsachlich ist die Abgrenzung eines Stilbogriffs von allgemeinen Handlunggrundsatzen und guter Pravis in der Programmierung nicht einfacher als in jeder anderen Disziplin, in der eine gewisse schopferische Freiheit besteht -- sie ist fast immer willkurlich. Im folgenden soll daher noch kurz ein Entwurfsprinzip vorgestellt werden, dass ich personlich eher nicht als Stilfrage einstufen wurde, dass aber dennoch haufiger in diesem Zusammenhang genannt wird.

Wie bereits in Kurseinheit **6** und (teilweise auch schon in Kurseinheit **2**, Abschnitt 10.1) bermerkt, ist die Vererbung Aushangeschild und Problemkind der objektorientierten Programmierung zugleich. Es verwundert daher nicht, dass sich eine ganze Menge von Programmierrichtinien mit genau diesem Thema beschaffigen. Die meines Erachtens gewichtigste aller Regeln zu diesem Thema ist jedoch:Fur Java lasst sich diese Regel auch als,,deklariere jede Klasse entweder als abstrakt oder als final" formulieren. Der Grund dafur, dass nur die Blatter der Klassenhierarchie instanziierbar sein sollen, ist einfach: Wenn man mit der Funktionalitat einer Klasse (bzw. genauer und in diesem Fall wichtig, der Funktionalitat der Instanzen einer Klasse) nicht zufrieden ist, will man die Implementierung der Klasse antern. Als Programmiererin mochte man diese Anderung unabhangig von der Frage, ob davon auch andere Klassen betroffen sind, durchfuhren können. Deswegen wird man die Anderungen auch nur an der Klasse selbst und nicht etwa an einer ihrer Superklassen durchfuhren. Betrifft der Anderungswunsch eine gerbrte Methode, so überschreibt man diese in der betreffenden Klasse nach seinen Vorstellungen. Nur wenn eine eingehende Analyse der Superklasse und all ihrer Subklassen ergibt, dass die gewunschte Anderung für alle sinnvoll ist und den Erwartungen der Klienten entspricht, kann man darüber nachdenken, die Anderung in der Superklasse durchzufuhren.

Wenn nun aber die Klasse, deren Verhalten man andern mochte, selbst Subklassen hat, dann ist man der Freiheit beraubt, nur für sich zu entscheiden -- von jeder Anderung, die man durchfuhrt, muss man furchten, dass sie sich auf andere Klassen ausbreitet und den Vertrag dieser Klassen mit ihren Klienten bricht. (Siehe auch das Fragile-base-class-Problem in Kapitel 55). Etwas subtiler, aber genau dasselbe Problem, ereilt die Designerin von Klassenbibliotheken, wenn sie beschliebst, das Verhalten einer Klasse zu andern: Selbst wenn sie sich sicher ist, dass dies innerhalb der Bibliothek keine anderen als die gewunschten Auswirkungen hat, so kann sie doch nicht sicher sein, dass irgend eine Verwenderin ihrer Bibliothek von der Klasse, die sie gerade geandert hat, erbt und somit eine Verhaltensanderung erfahrt, mit der sie nicht leben kann.

Nun ist aber, wie gerade erst (Kapitel 66) enwahnt, einer der wichtigsten Gedanken der Objektorientierung, existierende Code, vor allem Bibliotheksklassen, per Verebrung wiederzuvenwenden. Wenn die Bibliothekskdessignerin aber alle relevanten Klassen (das sind ublicheweise gerade die konkreten, also die instanziierbaren) final deklariert hat, dann ist das nicht moglich. Eine einfache Konvention erlaubt jedoch, diese Beschrankung zu umgehen: In der Bibliothek wird einfach die Klasse, von der geerbt werden soll, als abstrakt deklariert und per Verebrung eine Subklasse davon abgeleitet, die zunächst keine Anderungen (Differentia) hinzufugt, dafur aber konkret (also instanziierbar) und auch final ist. Sollte die Bibliothekskesignerin Anderungen durchfuhren wollen, kann sie das zunächst an ihrer finalen Klasse tun und nur, wenn sie sich vollkommen sicher ist, dass sie alle Klienten ihrer Bibliothek mit den Anderungen beglucken mochte, die Anderungen in der abstrakten Superklasse durchfuhren.

Fazit

Die Quintessenz der Bedeutung von Stil lasst sich kaum besser wiedergeben als durch ein weiteres Zitat von Bertrand Meyer:

_Good software is good in the large and in the small, in its highlevel architecture and in its low-level details. True, quality in the details does not guarantee quality of the whole; but sloppiness in the details usually indicates that something more serious is wrong too.... A serious engineering process requires doing everything right: the grandiose and the mundane._

_So you should not neglect the relevance of such seemingly humble details as text layout and choice of names. True, it may seem surprising to move on... from... formal specifications... to whether a semicolon should be preceded by a space.... The explanation is simply that both issues deserve our care, in the same way that when you write quality O-O software both the design and the realization will require your attention._

Das Kapitel,A sense of style" aus Bertrand Meyers Buch empfehle ich jeder, die glaubt, Stil sei eine personliche Angelegenheit und ansonsten nicht so wichtig. über Meyers konkrete Vorgaben mag man streiten, über die prinzipielle Wurdigung der Wichtigkeit von Stil hingegen nicht.

Wer Java programmiert, die mag sich die Java Coding Standards des Software Engineering Institutes der Carnegie-Mellon-Universitat zu Gemute fuhren. Man kann sich wundern, was an der Verwendung einer Programmiersprache alles regulierungsfahig ist (und fragen, warum man die eine oder andere Regel nicht in die Definition der Sprache gepackt hat). Lesenswert ist auch der Eintrag zum Thema,,Programmierstil" in der deutschsprachigen Wikipedia.

## 71 Losungen zu den Selbsttestaufgaben

**Selbsttestaufgabe 68.1 (Seite 330)**

Lesen Sie weiter!

[MISSING_PAGE_EMPTY:357]

[MISSING_PAGE_EMPTY:358]

* [75] Universalienstreit................... _de.wikipedia.org/wiki/Universalienproblem_ Extension und Intension................... _de.wikipedia.org/wiki/Extension_und_Intension_
* [76] Familienahnlichkeit................... _de.wikipedia.org/wiki/Familiarianhnlichkeit_
* Information Resource Dictionary System (IRDS) framework................... _www.iso.org/standard/17985.html_
* [96] Genus proximum et differentia specifica _de.wikipedia.org/wiki/Genus_proximum_et_differentia_specifica_
* [119] DHH Ingalls
* A simple technique for handling multiple polymorphism
* OOPSLA (1986) 347-349................... _doi.org/10.1145/28697.28732_
* [132] Model View Controller................... _de.wikipedia.org/wiki/Model_View_Controller_
* [145] L Cardelli Type Systems* in: CRC Handbook of Computer Science and Engineering (1996) Chapter 103................... _homepage.divms.uiowa.edu/~tinelli/classes/185/Fall06/notes/cardelli-95.pdf_
* [146] B Pierce: Types and Programming Languages (The MIT Press, 2002)................... _dblp.org/rec/books/daglib/0005958_
* [155] Boolesche Algebra................... _de.wikipedia.org/wiki/Boolesche_Algebra_ Kurs 01661................... _www.fernuni-hagen.de/fu-search/index.jsp?query=01661_
* [181] Kurs 01853................... _www.fernuni-hagen.de/fu-search/index.jsp?query=01853_
* [195] J Palsberg, MI Schwartzbach: Object-Oriented Type Systems (John Wiley & Sons, 1994)................... _dblp.org/rec/books/daglib/0070753_ BC Pierce: Types and Programming Languages (MIT Press 2002)................... _dblp.org/rec/books/daglib/0005958_
* [199] The Java Language Specification... _docs.oracle.com/javase/specs/jls/se 11/html/index.html_ The Long Strange Trip to Java.... _www.blinkenlights.com/classiccmp/javaorigin.html_
* [202] IEEE 754................... _de.wikipedia.org/wiki/IEEE_754_
* [212] Oracle Java 8: Lambda Quick Start _www.oracle.com/webfolder/technetwork/tutorial/solve/java/Lambda-QuickStart/index.html_
* [217] Kurs 01853................... _www.fernuni-hagen.de/fu-search/index.jsp?query=01853_ Java Pakete und Module................... _docs.oracle.com/javase/specs/jls/se 10/html/jls-7.html_
* [220] zirkulare Abhangigkeit................... _en.wikipedia.org/wiki/Circular_dependency_
* [221] Open Services Gateway Initiative... _de.wikipedia.org/wiki/OSGi_ PS Canning, WR Cook, WL Hill, WG Olthoff
* Interfaces for Strongly-Typed Object-Oriented Programming
* in: Proc. of OOPSLA (1989) 457-467 _doi.org/10.1145/74877.74924_
* [222] Index...................
* [223] M Naftalin, P Wadler Java Generics and Collections (O'Reilly, 2006)................... _dblp.org/rec/books/daglib/0017180_
* [230] M Torgersen, E Ernst, CP Hansen, P von der Ahe, G Bracha, N Gafter
* Adding wildcards to the Java programming language
* Journal of Object Technology 3:11 (2004) 97-116................... _doi.org/10.5381/jot.2004.3.11.a5_
* [242] Kurs 01853................... _www.fernuni-hagen.de/fu-search/index.jsp?query=01853_ F Steimann, J Oqvist, G Hedin
* Multitudes of Objects: First Implementation and Case Study for Java
* Journal of Object Technology 13:5 (2014) 1:1-33................... _doi.org/10.5381/jot.2014.13.5.a1_
* [244] O Kiselyov, A Biboudis, N Palladinos, Y Smaragdakis "Stream fusion, to completeness" in: Proc. of POPL (2017) 285-299... _doi.org/10.1145/3009837.3009880_
* [248] Threads in Java.................. _de.wikipedia.org/wiki/Thread_(_Informatik)_
* [249] Kurs 01853.................. _www.femuni-hagen.de/fu-search/index.jsp?query=01853_
* [250] Kurs 01853.................. _www.femuni-hagen.de/fu-search/index.jsp?query=01853_
* [251] C# Language Specification.................. _docs.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/index_
* [252] Exception tunneling_.................. _wiki.c2.com/?ExceptionTunneling_
* [253] Versioning, Virtual, and Override... _www.artina.com/intv/nonvirtual.html_
* [254] Kurs 01853.................. _www.femuni-hagen.de/fu-search/index.jsp?query=01853_
* [255] B Stroustrup "A history of C++: 1979-1991" in: Second ACM SIGPLAN Conference on History of Programming Languages HOPL-II (1993) 271-297
* [256]_doi.acm.org/10.1145/154766.155375_
* [257] M Ellis, B Stroustrup: The Annotated C++ Reference Manual (Addison-Wesley 1990)
* [258]_dblp.org/rec/books/aw/Ellis590_
* [259] J Coplien: Advanced C++ Programming Styles and Idioms (Addison-Wesley Professional 1991)
* [260]_dblp.org/rec/books/aw/Coplien92_
* [261] ECMA-Standard 367: EIFFL: Analysis, Design and Programming Language (2nd edition, June 2006).................. _www.ecma-international.org/publications/standards/ECma-367.htm_
* [262] B Meyer: Object-Oriented Software Construction (2. Ausgabe, Prentice Hall, 2000).................. _dblp.org/rec/html/books/ph/Meyer97_
* [263] B Meyer "Overloading vs. object technology" Journal of Object-Oriented Programming (Oct/Nov 2001) 3-7.................. _citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.1.9234_
* [264] Kurs 01853.................. _www.femuni-hagen.de/fu-search/index.jsp?query=01853_
* [265] B Meyer: Object-Oriented Software Construction (2. Ausgabe, Prentice Hall, 2000).................. _dblp.org/rec/html/books/ph/Meyer97_
* [266] B Liskov, JM Wing "A Behavioral Notion of Subtyping." ACM Trans. Program. Lang. Syst. 16:6 (1994) 1811-1841.................. _doi.org/10.1145/197320.197383_
* [267] B Liskov, JM Wing "A Behavioral Notion of Subtyping." ACM Trans. Program. Lang. Syst. 16:6 (1994) 1811-1841.................. _doi.org/10.1145/197320.197383_
* [268] W Codenie et al..,From custom applications to domain-specific frameworks" CACM 40:10 (1997) 71-77.................. _doi.org/10.1145/262793.262807_
* [269] Kurs 01853.................. _www.femuni-hagen.de/fu-search/index.jsp?query=01853_
* [270] L Mikhailov, E Sekerinski "A study of the fragile base class problem" in: Proc. of ECOOP (1998) 355D382.................. _doi.org/10.1007/BFb0054099_
* [271] S Williams, C Kindel,The Component Object Model: A Technical Overview"
* [272]_www.cs.umd.edu/~pugh/com/_
* [273] B Stroustrup: The Design and Evolution of C++ (Addison-Wesley 1994)
* [274]_dblp.org/rec/books/daglib/0076736_
* [275] W Wulf, M Shaw "Global variable considered harmful" ACM SIGPLAN Notices 8:2 (1973) 28-34.................. _doi.org/10.1145/953353.953355_
* [276] C Ponder, B Bush "Polymorphism considered harmful" ACM SIGPLAN Notices 27:6 (1992) 76-79.................. _doi.org/10.1145/130981.130991_* [315] F Steimann "Fatal Abstraction" in: Proc, of Onward! (2018) 125-130. doi.org/10.1145/3276954.3276966
* [322] Schlussel und Fremdschlussel...... de.wikipedia.org/wiki/Schl%C3%BCssel_(Datenbank) F Steimann "Content over container: object-oriented programming with multiplicities" in: Proc. of Onward! (2013) 173-186. doi.org/10.1145/2509578.2509582
* [326] N Wirth: Algorithmen und Datenstrukturen (PASCAL-Version, Teubner Verlag, 2000). dblp.org/rec/html/books/daglib/0095640
* [329] B Meyer: Object-Oriented Software Construction (Prentice Hall, 2000). dblp.org/rec/html/books/ph/Meyer97 ungarische Notation. de.wikipedia.org/wiki/Ungarische_Notation
* [332] Extract-method-Refactoring. refactoring.com/catalog/extractMethod.html
* [336] Replace-conditional-with-polymorphism-Refactoring _refactoring.com/catalog/replaceConditionalWithPolymorphism.html_ KJ Lieberherr, IM Holland, A Riel "Object-oriented programming: An objective sense of style" in: OOPSLA (1988) 323-334. doi.org/10.1145/62083.62113
* [341] B Meyer: Object-Oriented Software Construction (2. Ausgabe, Prentice Hall, 2000). dblp.org/rec/html/books/ph/Meyer97 Programmierstil. de.wikipedia.org/wiki/Programmierstil
* [342]

## Index

:1-Beziehung **30**:

:n-Beziehung **30**:

A

Abfrag **276**:

Abh\(\ddot{\text{a}}\)ngigkeit **217**:

abstrakte Klasse **5**:

S. Klasse **6**:

Abstraktionshierarchie **94**:

Accessor **53**, s. Zugriffsmethode

Aggregation **32**, _283_, _334_:

aktives Objekt **136**, _138_:

aktueller Parameter **45**:

Alias **18**, **23**, _79_, _168_, _224_, _283_:

Aliasing **15**, **23**, _27_, _52_:

Aliasing-Problem **314**:

Allgemeinbegriff **74**, _313_:

Generalisierung als **96**:

Anderungsbhangigkeit **217**:

Annotation **239**, **247**, _261_:

Annotationstyp **199**:

Anweisung **13**, _45_:

Application Programming Interface **198**:

Aristoteles **97**:

Array store exception **224**, _230_:

Array-Initialisierer **199**:

Array-Literal **15**, _126_:

Array-Typ **199**:

Assoziaitypeicher **124**:

atomares Objekt **129**:

Attribut **28**:

und Zustand **34**:

-wert **34**:

Attribute **261**:

Aufzahlungstyp **199**:

Ausdruck **36**, **37**:

Nachrichten- **37**:

primitiver **37**:

Zuweisungs- **37**:

Ausgabestrom **248**:

Auto boxing und unboxing **262**:

Auto unboxing **201**:

B

Base class **109**:

Basisklasse **302**:

Befehl **276**, _327_:

Behavioural subtyping **5**:

s. verhaltensbasiertes Subtyping **297**:

benannte Instanzvariable **29**:

Beziehung **312**:

:1-**30**:

:n-**30**:

leere **31**:

binare Methode **39**:

binare Nachricht **39**:

Block **58**, _266_:

boolesche Algebra **155**:

Boxing und Unboxing **264**:

Bytecode **197**:

Call by reference **50**, _71_, _201_, _210_, _269_:

in C# **255**:

Call by value **50**, _71_, _201_, _210_, _268_:

Call stack **60**:

Change log **8**:

Child class **109**:

Client-Schnittstelle **103**:

Closure **60**:

Coding convention **329**:

Collection **61**:

Garbage **5**:

Garbage collection **187**:

heterogene **187**:

-Klassen **120**:

Stream zum Zugriff auf eine **134**:

Nachrichten- **37**:

Common Intermediate Language **254**:

primitiver **37**:

Common Type System **260**:

Zuweisungs- **37**:

Compilation unit **4**, _203_, _218_:

Congable **109**:
Component Object Model 305 Continuation 60, 64 Cross cast 178, 236 Datenkapselung 276 declaration-site variance 265 Declaration-site variance 228 Default-Methode 222 Definition 151, 220 Dekaration 147, 151 deklariertes Element 146 Delegate 260, 261 Delegation 124, 270 denotationale Semantik 155 Dependent type 171 Dereferenzierung 320 Derived class 109 direkte Instanz 97, 99, 202 direkte Instanz 80 direkte Subklasse 108, s. Subklasse direkte Superklasse 108, s. Superklasse direkter Subtyp 172 Dispatch 217, s. a. dynamisches Binden double 119, 209 multi 196 single 119 Double dispatch 119, s. Dispatch Down cast 116, 178, 187, 227, 236, 251 Durchgangigkeit der Konzepte 2 dynamische Typprufung 178 dynamischen Typprufung 224 dynamisches Binden 49, 62, 64, 73, 145, 271, 291, 303

Eigenschaft 2, 75 Einfachverbung 197 Endrekursion 66 Event 260 Event handler 260 Exception chaining 256 checked 245, 256 tunneling 256 unchecked 245, 256 Exception handling in Eifel 277 Expansion 159, 180 rekursive Typen 191 Export dedizierter 277, 306 Extension 75, 80, 146 einer Generalisierung 97

Factory-Methode 89, 207 Fall through 214 Fallunterscheidung 119, 292, 309 gleiche 334 per dynamischem Binden 250, 286, s. a. versteckte F. versteckte 49, 62 Familienahnlichkeit 76 Feld 28, 204 Filterfunktion 161, 164, 239 Fluent API 41, 42 formaler Parameter 23, 45, 46, 48, 125, 152 eines Blocks 61 formaler Typparameter 183 Forwarding 124, 270 Fragile-base-class-Problem 117, 256, 302 Fremdschlussel 320 Friend 277 funktionale Anforderung 293 funktionale Programmiersprache 266, 319 funktionale Programmierung 3, 16, 18, 60

Garbage collection 5, 25, 145, 197, 254, 275 Geheimisprinzip 36, 180, 316 Generalisierung 94, 173, 334 Ergebnis der 95 Vorgang der 95 Generics 183 generischer Typ 183 Genus et differentiae 97 Getter 53, 222, 257, 276 Lazy initialization per 87 Gleichheit von Objekten 16 globale Variable 21, 77 Goto 63 Hiding 21 H Home context 59, 71, 116bei Continuations....60

Identitat...................2, 2, 268

eines Objekts....12

von Objekten....16

image...................8

Impedance mismatch....320

imperative Programmierung....16

Implementation...................57

Implementationsogeheimnis....36, 52, 55, 57, 86,

_215, 306_

Indexer...................29, 259

indirekte Instanz....98, 202, s. Instanz

indirekter Subtyp...................172

indizierte Instanzvariable....29

Information hiding....36, 276, 306, 316

initialiserung....85, 100, 152

 lazy...................87, 131

fur Klassenvariablen....89

Inkusionspolymorphiie....177

inlining....310

innere Klasse....203, 204, 318

Instanz....73, 79

direkte....80, 98

indirekte....80, 98

instanzlierbar

nicht...................104

Instanzlierung....79

einer parametrischen Typdefinition....188

eines parametrischen Typs....182, 184

Instanzmethode....84, 204

Instanzvariable....28, 76, 84, 204

integer Entwicklungsurgebung....198

Intension....75, 76, 146, 204

einer Generalisierung....96

Interface....55, 57, 148, 180

Marker...................239

Tagging....239

Interface-als-Typ-Konzept....181, 302

interfacebasiette Programmierung....178, 181

interfaceimplementation....220

Interfacemplementerung

explizitte....262

implizite....263

Interfacetyp...................199

Interfacebasiette....221

interner Iterator....224

Invariante....169

Zustandswechsel........300

Invariante....175

list-ein-Beziehung....94

Iteration...................63

externe....67

interner 67, 241

Iterator...................240

Java Virtual Machine....197

JUnit....115

Kapselung....33, 36, 52, 313

Kardinalitat....30

Klasse....30

abgeleitete....109

abstrakte....101, 104, 106

als Interface....270, 272

in Eiffel....277

in Java....205

vs. Typ...................178

Basis-....109

konkrete....105

Klassen

-definition....76

-hierarchie....108

-methode....83

in Java....204

-typ...................199

-variable....83

in Java....204

in Java....204

-variable....83

in Java....204

in Java....204

Klassenmethode....84

Klassenschrittstelle....313

Klassenvariable....84

Klassenvariable....84

Klassifikation....75, 79

Klonen....81

Kommentar....57

Komponente....318

Komposition....32, 33, 334

konkrete Klasse....105

Konstante....55, 204

Konstruktor...................84, 206

Kontext eines Blocks....58

Kontravariane....175

von Wildcard-Typen....231Kontrollfuh8

Beeinflussung durch Return 47

Kontrollstruktur 61

primitive 49

Kopie

flache 129

tiefe 129

kovariante Redefinition 98

Kovarianz 175

von Wildcard-Typen 1231

L Lambda-Ausdruck 60, 211, 241, 266

Lautzieittyfrehler 224

Law of Demeter 334

Lazy initialization 87, s. Initialisierung

Lebenszklus 26

Liskov-Substitutionsprinzip 298

Literal 13, 27, 55, 80

Klassen 200

Literaloptimierung 71

Live programming 6

Live-Programmierung 4

logische Programmiersprache 319

lokale Variable 21, 28, 45, 152

Lokalitstprinzip 307, 319

loschen von Methoden 122

M

Marker interface 164

Marker-Interface 261

Mehrfachhierarchie 172

Mehrfachwererbung 270

Member 204, 220

Mereologie 33

Message dispatching 119

Message pattern 45

Metaklasse 82, 267

Metaprogramiersystem 93

metasyntaktische Variable 38, 46, 203

Method ambiguous error 208

Method dispatching 119

Method dispatching 45

Methode 45

binare 191

konstante 20

Multi- 217

Methoden

-aufruf 22, 42, 47, 48

-formpf 45, 57, 152

-signature 45, 57, 109

Methodedeklaration 152

Modularsierung 2

hierarchische 312

von Programmen 148

Monitor 246

Multi-dispatch 119, 209

Multi-Methoden 217

Multiplizitat 30

Nachricht 37

Nachrichtenausdruck 37

Nachrichtenausdruck 37

Nachrichtenkategorie 58

Nachrichtenselektor 39, 46

Nachrichtenversand 37

Name 17, 18

Namensaquivalenz 159

Navigation 320

Nebenfrekt 41

Nebenwirkung 41

Netzwerkmodel 27

nichtfunktionale Anforderung 293

nominale Typkonformitat

in Java 202

nominale Typkonformitat

in Java 221

nominale Typkonformitatsdeklaration 221

Navarianz 175

von Java 202

Null pointer exception 150

Nur-Lesen 54

Nur-Schreiben 54

Objekt

atomares 13

strukturiertes 28

wachsendes 131

zusammengesetztes 14

Objektgeflecht 27

Objektorientierung

klassenbasierte Form 73

prototyppenbasierte Form 73

offene Rekursion 107, 116, 271, 303

Open Services Gateway Initiative 219operationale Semantik 155 OSGi 219 Outer this 204 package local 239 parallee Austfuhrung 62 parametrische Typedefinition 182 parametrischer Polymorphismus 5. Polymorphismus 5. Parent class 109 passives Objekt 136 Pattern 260 Persistent2ayer 320 Pipelining 242 Platzhalter 19 Pointer 19 Pointervariable 19, 25 Polymorphic 49, 176 Inklusions- 5. Inklusionspolymorphic vs. Polymorphismus 49 Polymorphismus 49 pamartrischer 177, 182 vs. Polymorphic 49 primitive Methode 80, 85 primitive Typ 199 in Java 201 Programmierstil 329 Property 257 Protokoll 48, 55, 57, 127, 153, 178 Protokollbeschreibung 57 Prototyp 76 Pseudo-Typvariable Self 153, 191, 193 Pseudovariable 14, 23, 45, 48, 70, 77 self und super im Home context 59

qualifizierter Export 270, 277 R

Raw type 236 Redefinition 167, 170, 277 Redundanz 148, 149 Refactoring 304 Referenz 19 ReferenzSennantik 19, 27, 201, 223, 268 Reflection 247, 264 reflektiver Zugriff 219 relationales Datenmodell 27 Repräsentationsobjekt 315 Repräsentationsunabhangigkeit 276 Return-Arweisung 44, 47 bei Continuation 60 Rolle 301, 329 Rollenwechsel eines Objekts 178 Routine 276 Runtime type information 273

Schlossel 123, 320 Schlussewort 13, 63, 70 Schlussewort nachricht 39, 70 Schnittstelle 148, 180 eines Moduls 215 Schnittstellenspezifikation eines Moduls 216 Seiteneffekt 41, 42, 55, 214, 332 self 48 semantischer Fehler 149, 160 Separation of concerns 313 Setter 53, 222, 257, 276 Sichtparkeit 20, 216 Sichtparkeit 21 21 von Variablen 201 Signatur 152 Softwarekrise 2 Speicherbereinigung 42, s. a. Garbage collection Spezialisierung 99, 171, 334 Statik und Dynamik Unterscheidung zwischen 111 statischen Typprifung 224 statisches Binden 49 Streams-Konkatenation 25 Strings 14 Struktur 11 von Objekten 28 Strukturaquivalenz 159 strukturierte Programmierung 63, 309 Subklasse 91, 108 direkt 108 in Java 205 Subklassenbeziehung 108, 205 Substituierbarkeit 281, 292 Subtyp 171 Subtyppenbieiung 171 Subtyppenbierachie 172Subtyping... _2, **172**, _291 verhaltensezogenes... _298_ Subtypoplymorphic... **177** Superklase... **108** direkte... **108** Supertyp... **171** Symbol... **14**

Tagging interface... _164_ tatschlicher Parameter... **45**, _50_ tatsachlicher Typparameter... **183** Teil-Ganzes-Beziehung... _32, 316_ Template... **272** temporare Variable... _41, 45_ Test... _148_ Trennung der Belange... **313** Tupel... **289** Typ... **146** -annotation... **148**, _149, 167_ als Ausdruck einer Invariante... _169_ fehlerhafte... _151_ in Strongtalk... _153_ Weglassen von in Strongtalk... _154_ -aquivalenz... **159** nominale... **159** strukturele... _159_ -erveiterung... **162**, _205_ -expansion... _264, 272_ -fehler... **148**, _160_ -hierarchie... **172** -inference2... _147, 234, 264, 326_ -invariante... _157_ -konformitat... _292_ des Subtypen mit dem Supertypen... _175_ nominale... **163** strukturele... _163_ -konstruktor... _154_ -korrektheit... _149_ -prufung... _150_ -regel... _146_ die von Ausdrucken einzuhalten sind... _157_ zur Zuordnung eines Typs zu Ausdrucken... _157_ -system... **146**, _157_ optionales... _145_ -urwandlung... _176_, **178**, _227, 235, 236, 273_ -variable... **182** Type branding... **160**, _161, 165_ Type cast... _273_ Type erasure... _236, 264_ Typverietwang... _261, 281_ Typinferenz... _149_ Typinvariante... **148** Typisierung... _156_ typkonformitat... _163_, _s.a._ Typkonformitat... _281_ -überladen... _119_ -überscheben... _102_, _121, 167_ in Eiffel... _277_ -mit Aufruf von super... _117_ -UML... _11, 30, 80_ unare Nachricht... **39** ungarische Notation... _263, 327_ Unified Modeling Language... \(5\) UML Universalienstreit... _75, 104_ unsicher (unsafe)... _254_ unveränderliches Objekt... _34_ Up cast... **178**, _236_ Use-site variance... _228_ -V_ Variable... _2, 14, 17, **18**, _27_ metasyntaktische... _38_ -fehler... _149_ veränderliches Objekt... _34_ verankerter Typ... _283_ Vererburg... _2, 101, 261, 281_ bei Typerveiterung... _162_ Verberbungsablnigkeit... _217_ Vererbungssinterface... _306_ Vererbungsschmittstelle... _103_ Verhalten... _11, 75_ verhaltenbasiertes Subtyping... **297** Verweis... **19**, _27_ Verweissemantik... **19**, s. Referenzsmentik Verwendung eines Programmelements... **152** Virtual function table... _272_ -W_ Wert... **12**, _123_ Werten... _12Wertsemantik **19**, _168_, _201_, _268_

Wertzuweisung **2**, **21**

Wiederverwendung **2**

Wildcard-Typ **229**

Wrapper-Typ **199**

Z

Zeichenkette **14**

Zu-eins-Beziehung **30**

Zugreifbarkeitsregel **335**

Zugriffsmethodode **53**, _220_, s. a. Getter und Setter automatische Einrichtung von **93**

Zugriffsmodifikator **180**, _216_

Zulassigkeit von Methodenaufrufen **158**

von Zuweisungen **158**

von Zuweisungen **158**

von Zuweisungen **158**

von Zuweisungen und Methodenaufrufen **149**

Zu-n-Beziehung **30**

zusammengesetztes Objekt **129**

Zustand **2**, _16_, **34**, _52_

Zuweisung **21**

explizite **50**, _286_

implizite **22**, **50**, _51_, _165_, _268_

linke und rechte Seite **22**

unzulassige **22**

Zuweisungskompatibilitat **157**, **158**, _163_, _205_, _281_, _291_

bei parametrisierten Subtypen **186_

unter parametrischem Polymorphismus **182_

Zuweisungsoperator **21**, _23_, _41_

Zuweisungsversuch **286**

Zwischenobjekt **31**, _68_, _79_, _240_