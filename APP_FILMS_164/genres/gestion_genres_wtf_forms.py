"""
    Fichier : gestion_genres_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjouterGenres(FlaskForm):
    rue_regexp = "^(?!.*['\-\s]{2,})([A-Za-zÀ-ÖØ-öø-ÿ0-9]+['\- ]?)*[A-Za-zÀ-ÖØ-öø-ÿ0-9]+$"
    rue = StringField("Rue", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                         Regexp(rue_regexp,
                                                message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    ville = StringField("Ville", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                             Regexp(rue_regexp,
                                                    message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    date_debut = DateField("Date de début", format='%Y-%m-%d', validators=[DataRequired(message="Date requise")])

    submit = SubmitField("Enregistrer le Chantier")


class FormWTFUpdateGenre(FlaskForm):
    """
        Dans le formulaire "genre_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """


class FormWTFUpdateGenre(FlaskForm):
    nom_rue_update_regexp = "^(?!.*['\-\s]{2,})([A-Za-zÀ-ÖØ-öø-ÿ0-9]+['\- ]?)*[A-Za-zÀ-ÖØ-öø-ÿ0-9]+$"
    nom_rue_update_wtf = StringField("Rue ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                         Regexp(nom_rue_update_regexp,
                                                                message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    nom_genre_update_regexp = "^(?!.*['\-\s]{2,})([A-Za-zÀ-ÖØ-öø-ÿ0-9]+['\- ]?)*[A-Za-zÀ-ÖØ-öø-ÿ0-9]+$"
    nom_genre_update_wtf = StringField("Ville ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                             Regexp(nom_genre_update_regexp,
                                                                    message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    date_genre_wtf_essai = DateField("Date de début", validators=[InputRequired("Date obligatoire"),
                                                                  DataRequired("Date non valide")])

    submit = SubmitField("Update genre")


class FormWTFDeleteGenre(FlaskForm):
    """
        Dans le formulaire "genre_delete_wtf.html"

        nom_genre_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_genre".
    """
    nom_genre_delete_wtf = StringField("Effacer ce genre")
    submit_btn_del = SubmitField("Effacer genre")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
