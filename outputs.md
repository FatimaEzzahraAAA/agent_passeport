# python main.py :

Modèles disponibles pour génération de contenu :
- models/gemini-2.5-flash
- models/gemini-2.5-pro
- models/gemini-2.5-flash-preview-tts
- models/gemini-2.5-pro-preview-tts
- models/gemma-4-26b-a4b-it
- models/gemma-4-31b-it
- models/gemini-flash-latest
- models/gemini-flash-lite-latest
- models/gemini-pro-latest
- models/gemini-2.5-flash-lite
- models/gemini-2.5-flash-image
- models/gemini-3-flash-preview
- models/gemini-3.1-pro-preview
- models/gemini-3.1-pro-preview-customtools
- models/gemini-3.1-flash-lite-preview
- models/gemini-3.1-flash-lite
- models/gemini-3-pro-image-preview
- models/gemini-3-pro-image
- models/nano-banana-pro-preview
- models/gemini-3.1-flash-image-preview
- models/gemini-3.1-flash-image
- models/gemini-3.1-flash-lite-image
- models/gemini-nano-banana-2.1
- models/gemini-3.5-flash
- models/gemini-3.5-flash-lite
- models/gemini-omni-flash-preview
- models/gemini-omni-1.1-flash
- models/gemini-3.5-transcribe
- models/gemini-3.6-flash
- models/gemini-3.7-flash
- models/gemini-3.8-flash
- models/gemini-4-argon
- models/lyria-3-clip-preview
- models/lyria-3-pro-preview
- models/lyria-3.5
- models/gemini-3.1-flash-tts-preview
- models/gemini-3.8-flash-tts
- models/gemini-3.8-flash-lite-tts
- models/gemini-robotics-er-2-preview
- models/gemini-2.5-computer-use-preview-10-2025
- models/antigravity-preview-05-2026
- models/antigravity-preview-09-2026
- models/antigravity-preview-latest
- models/deep-research-max-preview-04-2026
💬 Réponse : Je ne trouve pas cette information dans ma base de connaissances actuelle.
------------------------------------------------------------

👤 Utilisateur : Quel est le prix exact du timbre fiscal pour un passeport ?
🤖 Assistant (en réflexion)...
💬 Réponse : Je ne trouve pas cette information dans ma base de connaissances actuelle.
------------------------------------------------------------    

👤 Utilisateur : Quel est le prix exact du timbre fiscal pour un passeport ?
🤖 Assistant (en réflexion)...

💬 Réponse : Je ne trouve pas cette information dans ma base de connaissances actuelle.
------------------------------------------------------------    

👤 Utilisateur : Comment obtenir un visa pour aller aux États-Unis ?
🤖 Assistant (en réflexion)...

💬 Réponse : Je suis désolé, mais ma spécialité porte uniquement sur les démarches administratives liées au passeport marocain. 

Je ne peux donc pas vous renseigner sur les procédures d'obtention de visa pour d'autres pays comme les États-Unis. N'hésitez pas à me poser une question concernant le passeport marocain !    
------------------------------------------------------------    
(.venv)

# python indexation.py :

Nettoyage des anciennes données...
Lecture du corpus...
Fichier page1.txt découpé en 19 chunks.
Fichier page2.txt découpé en 26 chunks.
Fichier page3.txt découpé en 11 chunks.
Fichier page4.txt découpé en 24 chunks.
Fichier page5.txt découpé en 17 chunks.
Fichier page6.txt découpé en 33 chunks.

Génération des embeddings pour 130 chunks au total...
  -> Traitement du lot 1...
  -> Traitement du lot 2...
  -> Traitement du lot 3...
    ⚠️ Limite d'API atteinte. Pause de 60 secondes pour laisser  le quota se réinitialiser...
    🔄 Reprise du traitement...
  -> Traitement du lot 4...

Envoi des 130 vecteurs à Pinecone...
✅ Indexation terminée avec succès !
(.venv)

# python agent_rag.py :

=== TESTS DE L'AGENT RAG (PARTIE B) ===

👤 Utilisateur : Quels sont les documents nécessaires pour renouveler un passeport ?
🤖 L'IA cherche dans le contexte et répond...
⚠️ Modèle gemini-3.8-flash surchargé. Pause de 2s et on essaie lle suivant...
⚠️ Modèle gemini-3.7-flash surchargé. Pause de 2s et on essaie lle suivant...

💬 Réponse : D'après les informations fournies dans le texte, voici les documents nécessaires pour constituer le dossier de renouvellement d'un passeport :

* **Le formulaire de demande de passeport biométrique** renseigné, daté et signé, avec le code **e-timbre** valide (code de 16 chiffres).
* **Une photocopie de la Carte Nationale d’Identité Électronique (CNIE)** en cours de validité.
* **Une photographie d’identité récente** (de format 35 × 45 mm, prise de face, sur fond bleu, blanc ou gris clair, laissant voir les caractéristiques du visage).
* **L’ancien passeport** (ou le justificatif correspondant si ce document n’est plus en votre possession).
------------------------------------------------------------    
📊 Évaluation de la fidélité (Faithfulness) en cours...
⚠️ Modèle gemini-3.8-flash surchargé. Pause de 2s et on essaie lle suivant...
⚠️ Modèle gemini-3.7-flash surchargé. Pause de 2s et on essaie lle suivant...
⚠️ Modèle gemini-3.5-flash surchargé. Pause de 2s et on essaie lle suivant...
❌ Erreur : 404 NOT_FOUND. {'error': {'code': 404, 'message': 'This model models/gemini-2.5-flash is no longer available to new users. Please update your code to use models/gemini-3.8-flash for the latest features and improvements. We recommend you to use the Interactions API (https://ai.google.dev/gemini-api/docs/get-started).', 'status': 'NOT_FOUND'}}

👤 Utilisateur : Quel est le prix exact du timbre fiscal pour un passeport ?
🤖 L'IA cherche dans le contexte et répond...
e suivant...
➡️ La réponse est-elle fidèle au contexte ? OUI
============================================================

👤 Utilisateur : Comment obtenir un visa pour aller aux États-Unis ?
🤖 L'IA cherche dans le contexte et répond...
⚠️ Modèle gemini-3.8-flash surchargé. Pause de 2s et on essaie le suivant...
⚠️ Modèle gemini-3.7-flash surchargé. Pause de 2s et on essaie le suivant...

💬 Réponse : Je ne trouve pas cette information dans ma base de connaissances actuelle.
------------------------------------------------------------
📊 Évaluation de la fidélité (Faithfulness) en cours...
⚠️ Modèle gemini-3.8-flash surchargé. Pause de 2s et on essaie le suivant...
⚠️ Modèle gemini-3.7-flash surchargé. Pause de 2s et on essaie le suivant...
➡️ La réponse est-elle fidèle au contexte ? OUI
➡️ La réponse est-elle fidèle au contexte ? OUI
============================================================    
(.venv)

# adk run agent_passeport :

Log setup complete: C:\Users\Admin\AppData\Local\Temp\agents_log\agent.20261104_200115.log
To access latest log: tail -F C:\Users\Admin\AppData\Local\Temp\agents_log\agent.20261104_200115.log
C:\Users\Admin\Documents\ISMAGI\Formations\.data_maroc_bootcamp\8. ai engineering\.venv\Lib\site-packages\google\adk\cli\cli.py:351: UserWarning: [EXPERIMENTAL] InMemoryCredentialService: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  credential_service = InMemoryCredentialService()
C:\Users\Admin\Documents\ISMAGI\Formations\.data_maroc_bootcamp\8. ai engineering\.venv\Lib\site-packages\google\adk\auth\credential_service\in_memory_credential_service.py:33: UserWarning: [EXPERIMENTAL] BaseCredentialService: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  super().__init__()
Running agent agent_passeport_adk, type exit to exit.
[user]: Quels sont les documents à fournir pour un premier passeport biométrique ?
[agent_passeport_adk]: Pour une première demande de passeport biométrique au Maroc, la composition du dossier dépend de votre situation (âge, etc.), mais voici les éléments principaux requis pour un adulte :

*   **Le formulaire de demande :** Il doit être dûment renseigné, daté et signé par le demandeur. Ce formulaire doit inclure le code de l'e-timbre (composé de seize chiffres) permettant le paiement des droits de timbre.
*   **La Carte Nationale d'Identité Électronique (CNIE) :** Une photocopie de votre CNIE en cours de validité est obligatoire. Notez que pour les majeurs ainsi que les mineurs âgés de 12 à 18 ans, une CNIE valide est indispensable.
*   **Photographie :** Une photographie d'identité récente et conforme aux normes en vigueur.

**Quelques précisions importantes :**
*   **Dépôt :** La démarche se fait en personne auprès de l'annexe administrative ou du caïdat dont vous dépendez.
*   **Individualisation :** Chaque demandeur, y compris chaque enfant, doit constituer son propre dossier individuel.
*   **Si votre CNIE n'est pas valide :** Il est impératif de faire le nécessaire pour la renouveler avant ou en parallèle de votre demande de passeport.

Je vous recommande de consulter le site officiel dédié (ou de vous rendre à votre autorité locale) pour vérifier les éventuelles pièces complémentaires spécifiques à votre situation familiale (notamment pour les mineurs ou les cas de double nationalité).  
[user]: Je vis à l'étranger, comment puis-je renouveler mon passeport au consulat ?
[agent_passeport_adk]: Pour renouveler votre passeport marocain alors que vous résidez à l'étranger, voici les points clés à retenir :

*   **Le dépôt est obligatoire en personne :** Bien que vous puissiez préparer certaines étapes en ligne, le dépôt du dossier de demande de renouvellement doit obligatoirement être effectué en personne auprès du service consulaire marocain dont vous dépendez (celui de votre lieu de résidence).
*   **La procédure :** Le passeport biométrique n'est pas prorogeable. Le renouvellement implique l'émission d'un nouveau titre. Il est conseillé de vérifier la date d'expiration de votre document actuel et d'anticiper la demande, car le dépôt se fait contre récépissé.
*   **Liste des pièces :** La liste des documents nécessaires à l'étranger peut différer de celle appliquée au Maroc. Il est impératif de consulter le site web ou de contacter directement votre consulat pour obtenir la liste exacte des pièces exigées selon votre situation, car les exigences consulaires sont spécifiques.

**Conseil :** Avant de prendre des engagements de voyage, je vous recommande vivement de vérifier auprès de votre consulat les délais de traitement actuels et la liste précise des documents requis pour éviter tout dossier incomplet.
[user]: Est-ce que je peux faire ma carte d'identité en même temps que mon passeport à l'étranger ?
[agent_passeport_adk]: Oui, il est tout à fait possible d'effectuer les démarches pour votre Carte Nationale d'Identité Électronique (CNIE) et votre passeport auprès des services consulaires de votre lieu de résidence à l'étranger.

Voici quelques précisions importantes :

*   **Procédures distinctes :** Bien que vous puissiez potentiellement traiter les deux, ce sont des démarches administratives qui nécessitent chacune leur propre dossier.
*   **Immatriculation consulaire :** Pour toute demande au consulat, votre immatriculation consulaire doit être à jour.
*   **Mineurs :** À partir de 12 ans, les mineurs peuvent demander leur CNIE en même temps que leur passeport.
*   **Dépôt en personne :** Comme pour le passeport, le dépôt de la demande de CNIE doit se faire en personne au consulat.      

vérifier leur liste spécifique avant toute démarche.
2.  **Prenez rendez-vous :** La plupart des démarches consulaires exigent une prise de rendez-vous préalable.
3.  **Dépôt :** Le dépôt doit en principe se faire en personne. Si vous envisagez de mandater un proche, vous devez impérativement contacter le consulat au préalable pour savoir s'ils acceptent une procuration et quelles sont les modalités précises (originaux à présenter, etc.).
4.  **Nature du document :** Gardez à l'esprit que ce certificat ne prouve pas votre célibat et ne remplace pas l'acte de mariage.

Si votre question concerne une situation très spécifique ou si une autorité vous a expressément demandé ce document pour un mariage **au Maroc**, je vous invite à vérifier auprès de l'Adoul ou du tribunal de la famille de votre lieu de résidence au Maroc, car les exigences peuvent varier selon les cas particuliers (notamment en cas de double nationalité ou de mariage mixte).
[user]: Quels sont les documents pour demander un visa pour les États-Unis ?
[agent_passeport_adk]: Je suis spécialisé dans les démarches administratives liées au **passeport marocain**.

Les informations contenues dans ma base de connaissances ne couvrent pas les procédures de délivrance de visas pour les États-Unis. Pour obtenir les documents requis et connaître la procédure, je vous invite à consulter directement le site officiel de l'**Ambassade des États-Unis au Maroc** ou le portail officiel du Département d'État américain (travel.state.gov).
[user]: Comment obtenir un certificat de coutume pour me marier au Maroc ?
[agent_passeport_adk]: Comme je vous l'ai indiqué précédemment, le **certificat de coutume** est un document destiné aux ressortissants marocains souhaitant se marier **à l'étranger**.

Si votre projet est de vous marier **au Maroc**, ce document n'est généralement pas requis car les autorités marocaines (le *Adoul* ou le tribunal de la famille) appliquent directement le Code de la famille marocain.

Pour un mariage au Maroc, vous devez vous adresser directement au **Tribunal de la famille** (*Mahkamat al-Osra*) dont dépend votre lieu de résidence (ou celui du futur conjoint) au Maroc. Ils vous fourniront la liste officielle des documents nécessaires (actes de naissance, certificats médicaux, etc.).

Si, toutefois, une autorité spécifique vous a expressément demandé un "certificat de coutume" alors que vous êtes déjà au Maroc, il est possible qu'il s'agisse d'une situation particulière (ex: mariage mixte avec un ressortissant étranger où le consulat du pays étranger exige un document prouvant votre statut matrimonial). Dans ce cas précis, je vous invite à :

1.  **Clarifier** avec l'autorité qui a formulé cette demande quel document exact est attendu.
2.  **Contacter le service consulaire marocain** le plus proche si vous êtes résident à l'étranger, ou le ministère des Affaires étrangères si vous êtes sur le territoire, pour savoir s'ils peuvent émettre une attestation équivalente répondant à cette demande particulière.

Si vous avez besoin d'informations sur d'autres démarches liées au passeport marocain, n'hésitez pas à me solliciter.
[user]: 

