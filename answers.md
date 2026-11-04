## Bonus — repère un cas où le modèle « hallucine » une réponse plausible mais fausse (ex : un prix ou un délai inventé). Comment reformulerais-tu ton prompt pour réduire ce risque ?

Pour le bonus sur l'hallucination, j'ai remarqué que sans contexte, le modèle refusait de répondre grâce à ma règle stricte ('réponds uniquement à partir du contexte'). Si j'avais mis un prompt plus permissif, le modèle aurait sûrement inventé un prix. Pour éviter cela en production, j'ai explicitement ajouté l'instruction : 'Ne jamais inventer de délais ou de prix'. C'est ce qui a garanti un comportement sûr lors des tests.


##  Bonus —ajoute un deuxième agent spécialisé (ex : un agent de reformulation de requête) et orchestre les deux avec un SequentialAgent. Quel problème concret est-ce que ça résout ?

L'ajout d'un agent de reformulation résout le problème de l'imprécision des requêtes utilisateurs. Souvent, l'utilisateur pose une question vague (ex: 'papiers passeport'). En reformulant cette question en une requête riche en mots-clés (ex: 'documents nécessaires renouvellement passeport biométrique Maroc'), on améliore considérablement le 'Recall' de la recherche vectorielle dans Pinecone, garantissant que l'agent de recherche trouve les bons passages.


##  Tableau des tests (Partie D)

| # | Question posée | Réponse de l'agent (Résumé) | Statut |
| :--- | :--- | :--- | :--- |
| **1** | Quels sont les documents à fournir pour un premier passeport biométrique ? | Formulaire e-timbre, photocopie CNIE, photo d'identité récente, dépôt en personne. |  **Correct** |
| **2** | Je vis à l'étranger, comment puis-je renouveler mon passeport au consulat ? | Dépôt obligatoire en personne au consulat de résidence, vérifier les pièces spécifiques sur place. |  **Correct** |
| **3** | Est-ce que je peux faire ma carte d'identité en même temps que mon passeport à l'étranger ? | Oui, procédures distinctes, immatriculation consulaire à jour, possible dès 12 ans pour les mineurs. |  **Correct** |
| **4** | Quels sont les documents pour demander un visa pour les États-Unis ? | Refus poli : "Je suis spécialisé dans le passeport... Je vous invite à consulter l'Ambassade des États-Unis." |  **Correct (Refus)** |
| **5** | Comment obtenir un certificat de coutume pour me marier au Maroc ? | L'agent a répondu en s'appuyant sur le corpus (qui contient cette page) en précisant que ce n'est généralement pas requis au Maroc. |  **Correct** |