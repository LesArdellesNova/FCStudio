1. Tous les fichiers possèdent un en-tête FCStudio.

2. Toutes les classes possèdent une docstring.

3. Toutes les fonctions publiques sont typées.

4. Le SDK ne dépend jamais des outils CLI.

5. Les outils CLI ne contiennent aucune logique métier.

6. Un modèle ne contient aucun traitement.

7. Les analyseurs ne produisent jamais d'affichage.

8. Les outils ne lisent jamais directement un fichier :
   ils passent toujours par le SDK.

9. Toute nouvelle fonctionnalité est documentée dans :
   - CHANGELOG
   - ROADMAP
   - Architecture si nécessaire.

10. Une tâche n'est validée que lorsque :
    - le code compile,
    - les tests manuels sont réalisés,
    - la documentation est à jour.