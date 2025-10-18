# dashboard_defense_ukraine.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configuration de la page
st.set_page_config(
    page_title="Analyse Stratégique Avancée - Ukraine",
    page_icon="🇺🇦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé avancé
st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        background: linear-gradient(45deg, #0057B7, #FFDD00, #FFFFFF, #0057B7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .metric-card {
        background: linear-gradient(135deg, #0057B7, #003F7F);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .section-header {
        color: #0057B7;
        border-bottom: 3px solid #FFDD00;
        padding-bottom: 0.8rem;
        margin-top: 2rem;
        font-size: 1.8rem;
        font-weight: bold;
    }
    .nato-card {
        background: linear-gradient(135deg, #0057B7, #003F7F);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    .ukraine-card {
        background: linear-gradient(135deg, #0057B7, #FFDD00);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .resistance-card {
        background: linear-gradient(135deg, #0057B7, #003F7F);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .aid-card {
        background: linear-gradient(135deg, #FFDD00, #0057B7);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .innovation-card {
        background: linear-gradient(135deg, #0057B7, #003F7F);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

class DefenseUkraineDashboardAvance:
    def __init__(self):
        self.branches_options = self.define_branches_options()
        self.programmes_options = self.define_programmes_options()
        self.major_programs = self.define_major_programs()
        self.international_aid = self.define_international_aid()
        
    def define_branches_options(self):
        return [
            "Forces Armées Ukrainiennes", "Forces Terrestres", 
            "Forces Aériennes", "Forces Navales", 
            "Forces d'Assaut Aérien", "Garde Nationale",
            "Forces Spéciales", "Résistance Territoriale"
        ]
    
    def define_programmes_options(self):
        return [
            "Coopération OTAN-Ukraine", "Programme d'Assistance Sécuritaire",
            "Modernisation des Forces Armées", "Défense Anti-Aérienne",
            "Forces de Réaction Rapide", "Défense Cybernétique",
            "Production d'Armements Nationale", "Reconstruction Militaire"
        ]
    
    def define_major_programs(self):
        return {
            "Défense Anti-Aérienne": {"pays": "UA/INT", "type": "Systèmes SAM", "statut": "Déploiement", "budget": "10 Md$"},
            "Chars de Combat": {"pays": "UA/INT", "type": "Chars", "statut": "Opérationnel", "quantite": "500+"},
            "Drones Bayraktar": {"pays": "TR/UA", "type": "Drone", "statut": "Opérationnel", "quantite": "50+"},
            "HIMARS": {"pays": "US/UA", "type": "MLRS", "statut": "Opérationnel", "portee": "300 km"},
            "Leopard 2": {"pays": "DE/UA", "type": "Char", "statut": "Déploiement", "quantite": "80+"},
            "F-16": {"pays": "INT/UA", "type": "Avion de combat", "statut": "Formation", "livraison": "2024"}
        }
    
    def define_international_aid(self):
        return {
            "États-Unis": {
                "aide_militaire": 45.0, 
                "aide_financiere": 30.0, 
                "equipement": "HIMARS, Abrams, Stryker",
                "formation": "Pilotes F-16, maintenance"
            },
            "Union Européenne": {
                "aide_militaire": 25.0, 
                "aide_financiere": 50.0, 
                "equipement": "Leopard 2, CAESAR",
                "formation": "Support logistique, médical"
            },
            "Royaume-Uni": {
                "aide_militaire": 15.0, 
                "aide_financiere": 8.0, 
                "equipement": "Challenger 2, Storm Shadow",
                "formation": "Forces spéciales, marine"
            },
            "Allemagne": {
                "aide_militaire": 12.0, 
                "aide_financiere": 15.0, 
                "equipement": "Leopard 2, Gepard",
                "formation": "Maintenance, logistique"
            },
            "Pologne": {
                "aide_militaire": 8.0, 
                "aide_financiere": 5.0, 
                "equipement": "T-72, PT-91",
                "formation": "Support logistique"
            },
            "Canada": {
                "aide_militaire": 5.0, 
                "aide_financiere": 7.0, 
                "equipement": "Léopard 2, NASAMS",
                "formation": "Formation médicale"
            }
        }
    
    def generate_advanced_data(self, selection):
        """Génère des données avancées et détaillées pour l'Ukraine"""
        annees = list(range(2014, 2028))
        
        config = self.get_advanced_config(selection)
        
        data = {
            'Annee': annees,
            'Budget_Defense_Mds': self.simulate_advanced_budget(annees, config),
            'Personnel_Milliers': self.simulate_advanced_personnel(annees, config),
            'PIB_Militaire_Pourcent': self.simulate_military_gdp_percentage(annees),
            'Operations_Militaires': self.simulate_advanced_operations(annees, config),
            'Readiness_Operative': self.simulate_advanced_readiness(annees),
            'Capacite_Defense': self.simulate_advanced_defense(annees),
            'Temps_Reaction_Jours': self.simulate_advanced_reaction(annees),
            'Aide_Internationale': self.simulate_international_aid(annees),
            'Developpement_Technologique': self.simulate_tech_development(annees),
            'Capacite_Projection': self.simulate_projection_capacity(annees),
            'Couverture_Anti_Aerienne': self.simulate_air_defense_coverage(annees),
            'Interoperabilite_OTAN': self.simulate_nato_interoperability(annees),
            'Cyber_Capabilities': self.simulate_cyber_capabilities(annees),
            'Production_Armements': self.simulate_weapon_production(annees)
        }
        
        # Données spécifiques aux programmes
        if 'otan' in config.get('priorites', []):
            data.update({
                'Formation_OTAN': self.simulate_nato_training(annees),
                'Exercices_Conjoint': self.simulate_joint_exercises(annees),
                'Integration_Systemes': self.simulate_systems_integration(annees)
            })
        
        if 'defense_aerienne' in config.get('priorites', []):
            data.update({
                'Systemes_SAM': self.simulate_sam_systems(annees),
                'Couverture_Air': self.simulate_air_coverage(annees),
                'Interception_Capacite': self.simulate_interception_capacity(annees)
            })
        
        if 'innovation' in config.get('priorites', []):
            data.update({
                'Programmes_Innovation': self.simulate_innovation_programs(annees),
                'Recherche_Defense': self.simulate_defense_research(annees),
                'Technologies_Emergentes': self.simulate_emerging_tech(annees)
            })
        
        if 'reconstruction' in config.get('priorites', []):
            data.update({
                'Reconstruction_Infra': self.simulate_infrastructure_reconstruction(annees),
                'Modernisation_Equipement': self.simulate_equipment_modernization(annees),
                'Industrie_Defense': self.simulate_defense_industry(annees)
            })
        
        return pd.DataFrame(data), config
    
    def get_advanced_config(self, selection):
        """Configuration avancée avec plus de détails pour l'Ukraine"""
        configs = {
            "Forces Armées Ukrainiennes": {
                "type": "forces_armees",
                "budget_base": 15.0,
                "personnel_base": 700,
                "operations_base": 100,
                "priorites": ["otan", "defense_aerienne", "innovation", "reconstruction", "conventionnel"],
                "doctrines": ["Défense Territoriale", "Guerre Hybride", "Résistance Nationale"],
                "capacites_speciales": ["Forces de Réaction Rapide", "Défense Anti-Aérienne", "Cyber Défense"]
            },
            "Coopération OTAN-Ukraine": {
                "type": "cooperation_otan",
                "personnel_base": 500,
                "operations_base": 50,
                "priorites": ["integration", "formation", "standardisation", "interopérabilité"],
                "programmes": ["Partenariat Renforcé", "Fonds d'Investissement OTAN", "Programme de Modernisation"],
                "objectifs": "Alignement complet avec les standards OTAN"
            },
            "Programme d'Assistance Sécuritaire": {
                "type": "programme_aide",
                "budget_base": 30.0,
                "priorites": ["equipement", "formation", "maintenance", "soutien logistique"],
                "partenaires": ["États-Unis", "UE", "Royaume-Uni", "Canada", "Pays Scandinaves"],
                "objectifs": "Renforcement des capacités de défense face à l'agression russe"
            },
            "Forces Terrestres": {
                "type": "branche_principale",
                "budget_base": 8.0,
                "personnel_base": 300,
                "priorites": ["defense_terrestre", "mecanisation", "artillerie", "mobilité"],
                "capacites_uniques": ["Brigades Mécanisées", "Artillerie Précise", "Défense Antichar"],
                "doctrine": "Défense en profondeur et contre-offensives localisées"
            }
        }
        
        return configs.get(selection, {
            "type": "branche",
            "personnel_base": 100,
            "operations_base": 20,
            "priorites": ["defense_generique"]
        })
    
    def simulate_advanced_budget(self, annees, config):
        """Simulation avancée du budget avec variations géopolitiques"""
        budget_base = config.get('budget_base', 15.0)
        budgets = []
        for annee in annees:
            base = budget_base * (1 + 0.15 * (annee - 2014))
            # Variations selon événements géopolitiques
            if 2014 <= annee <= 2015:  # Annexion de la Crimée
                base *= 1.3
            elif 2022 <= annee:  # Invasion à grande échelle
                base *= 3.5
            budgets.append(base)
        return budgets
    
    def simulate_advanced_personnel(self, annees, config):
        """Simulation avancée des effectifs"""
        personnel_base = config.get('personnel_base', 700)
        personnel = []
        for annee in annees:
            base = personnel_base * (1 + 0.05 * (annee - 2014))
            if 2022 <= annee:  # Mobilisation générale
                base *= 1.8
            personnel.append(base)
        return personnel
    
    def simulate_military_gdp_percentage(self, annees):
        """Pourcentage du PIB consacré à la défense"""
        pourcentage = []
        for annee in annees:
            base = 3.0 + 0.5 * (annee - 2014)
            if 2022 <= annee:  # Augmentation massive après l'invasion
                base = 15.0 + 2.0 * (annee - 2022)
            pourcentage.append(min(base, 25.0))
        return pourcentage
    
    def simulate_advanced_operations(self, annees, config):
        """Opérations militaires avec intensité variable"""
        base = config.get('operations_base', 50)
        operations = []
        for annee in annees:
            if 2014 <= annee <= 2021:  # Conflit de faible intensité
                operations.append(base + 5 * (annee - 2014))
            else:  # Guerre à grande échelle
                operations.append(base * 5 + 10 * (annee - 2022))
        return operations
    
    def simulate_advanced_readiness(self, annees):
        """Préparation opérationnelle avancée"""
        readiness = []
        for annee in annees:
            base = 60 + 2.0 * (annee - 2014)
            if 2022 <= annee:  # Amélioration due à l'expérience du combat
                base += 15
            readiness.append(min(base, 95))
        return readiness
    
    def simulate_advanced_defense(self, annees):
        """Capacité de défense avancée"""
        defense = []
        for annee in annees:
            base = 50 + 3.0 * (annee - 2014)
            if 2022 <= annee:  # Renforcement massif
                base += 20
            defense.append(min(base, 90))
        return defense
    
    def simulate_advanced_reaction(self, annees):
        """Temps de réaction avancé"""
        reaction = []
        for annee in annees:
            base = max(48 - 2.0 * (annee - 2014), 12)
            if 2022 <= annee:  # Amélioration due à l'expérience
                base = max(24 - 1.0 * (annee - 2022), 6)
            reaction.append(base)
        return reaction
    
    def simulate_international_aid(self, annees):
        """Aide internationale"""
        aide = []
        for annee in annees:
            if 2014 <= annee <= 2021:  # Aide limitée
                aide.append(2.0 + 0.5 * (annee - 2014))
            else:  # Aide massive après l'invasion
                aide.append(40.0 + 5.0 * (annee - 2022))
        return aide
    
    def simulate_tech_development(self, annees):
        """Développement technologique global"""
        return [min(40 + 3.0 * (annee - 2014), 85) for annee in annees]
    
    def simulate_projection_capacity(self, annees):
        """Capacité de projection de puissance"""
        return [min(35 + 2.5 * (annee - 2014), 75) for annee in annees]
    
    def simulate_air_defense_coverage(self, annees):
        """Couverture de défense anti-aérienne"""
        coverage = []
        for annee in annees:
            base = 30 + 3.0 * (annee - 2014)
            if 2022 <= annee:  # Renforcement massif
                base += 25
            coverage.append(min(base, 85))
        return coverage
    
    def simulate_nato_interoperability(self, annees):
        """Interopérabilité avec l'OTAN"""
        return [min(30 + 4.0 * (annee - 2014), 80) for annee in annees]
    
    def simulate_cyber_capabilities(self, annees):
        """Capacités cybernétiques"""
        return [min(35 + 3.5 * (annee - 2014), 85) for annee in annees]
    
    def simulate_weapon_production(self, annees):
        """Production d'armements (indice)"""
        production = []
        for annee in annees:
            base = 20 + 2.0 * (annee - 2014)
            if 2022 <= annee:  # Augmentation de la production nationale
                base += 15
            production.append(min(base, 70))
        return production
    
    def simulate_nato_training(self, annees):
        """Formation OTAN"""
        return [min(5 + 2.0 * (annee - 2014), 50) for annee in annees]
    
    def simulate_joint_exercises(self, annees):
        """Exercices conjoints"""
        return [min(3 + 1.5 * (annee - 2014), 30) for annee in annees]
    
    def simulate_systems_integration(self, annees):
        """Intégration des systèmes"""
        return [min(20 + 3.0 * (annee - 2014), 75) for annee in annees]
    
    def simulate_sam_systems(self, annees):
        """Systèmes SAM"""
        systems = []
        for annee in annees:
            base = 10 + 2.0 * (annee - 2014)
            if 2022 <= annee:  # Livraisons massives
                base += 20
            systems.append(min(base, 70))
        return systems
    
    def simulate_air_coverage(self, annees):
        """Couverture aérienne"""
        coverage = []
        for annee in annees:
            base = 25 + 2.5 * (annee - 2014)
            if 2022 <= annee:  # Renforcement
                base += 20
            coverage.append(min(base, 80))
        return coverage
    
    def simulate_interception_capacity(self, annees):
        """Capacité d'interception"""
        return [min(30 + 3.0 * (annee - 2014), 75) for annee in annees]
    
    def simulate_innovation_programs(self, annees):
        """Programmes d'innovation"""
        return [min(15 + 2.5 * (annee - 2014), 60) for annee in annees]
    
    def simulate_defense_research(self, annees):
        """Recherche défense"""
        return [min(20 + 2.0 * (annee - 2014), 65) for annee in annees]
    
    def simulate_emerging_tech(self, annees):
        """Technologies émergentes"""
        return [min(15 + 3.0 * (annee - 2014), 70) for annee in annees]
    
    def simulate_infrastructure_reconstruction(self, annees):
        """Reconstruction des infrastructures"""
        reconstruction = []
        for annee in annees:
            if annee < 2022:
                reconstruction.append(10 + 1.0 * (annee - 2014))
            else:
                reconstruction.append(15 + 5.0 * (annee - 2022))
        return reconstruction
    
    def simulate_equipment_modernization(self, annees):
        """Modernisation des équipements"""
        modernization = []
        for annee in annees:
            base = 20 + 2.0 * (annee - 2014)
            if 2022 <= annee:  # Accélération
                base += 15
            modernization.append(min(base, 80))
        return modernization
    
    def simulate_defense_industry(self, annees):
        """Industrie de défense"""
        industry = []
        for annee in annees:
            base = 15 + 1.5 * (annee - 2014)
            if 2022 <= annee:  # Développement accéléré
                base += 20
            industry.append(min(base, 75))
        return industry
    
    def display_advanced_header(self):
        """En-tête avancé avec plus d'informations"""
        st.markdown('<h1 class="main-header">🇺🇦 ANALYSE STRATÉGIQUE AVANCÉE - DÉFENSE UKRAINIENNE</h1>', 
                   unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
            <div style='text-align: center; background: linear-gradient(135deg, #0057B7, #FFDD00); 
            padding: 1rem; border-radius: 10px; color: white; margin: 1rem 0;'>
            <h3>🛡️ SYSTÈME DE DÉFENSE NATIONALE - RÉSISTANCE ET MODERNISATION</h3>
            <p><strong>Analyse multidimensionnelle des capacités militaires et stratégiques (2014-2027)</strong></p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_advanced_sidebar(self):
        """Sidebar avancé avec plus d'options"""
        st.sidebar.markdown("## 🎛️ PANEL DE CONTRÔLE AVANCÉ")
        
        # Sélection du type d'analyse
        type_analyse = st.sidebar.radio(
            "Mode d'analyse:",
            ["Analyse Intégrée Ukrainienne", "Programmes de Coopération", "Aide Internationale", "Scénarios Stratégiques"]
        )
        
        if type_analyse == "Analyse Intégrée Ukrainienne":
            selection = st.sidebar.selectbox("Niveau d'analyse:", self.branches_options)
        elif type_analyse == "Programmes de Coopération":
            selection = st.sidebar.selectbox("Programme stratégique:", self.programmes_options)
        elif type_analyse == "Aide Internationale":
            selection = st.sidebar.selectbox("Pays partenaire:", ["États-Unis", "Union Européenne", "Royaume-Uni", "Allemagne", "Pologne", "Canada"])
        else:
            selection = "Scénarios Stratégiques"
        
        # Options avancées
        st.sidebar.markdown("### 🔧 OPTIONS AVANCÉES")
        show_geopolitical = st.sidebar.checkbox("Contexte géopolitique", value=True)
        show_cooperation = st.sidebar.checkbox("Analyse des coopérations", value=True)
        show_technical = st.sidebar.checkbox("Détails techniques", value=True)
        threat_assessment = st.sidebar.checkbox("Évaluation des menaces", value=True)
        
        # Paramètres de simulation
        st.sidebar.markdown("### ⚙️ PARAMÈTRES DE SIMULATION")
        scenario = st.sidebar.selectbox("Scénario:", ["Résistance Prolongée", "Contre-Offensive", "Défense Territoriale", "Modernisation Accélérée"])
        
        return {
            'selection': selection,
            'type_analyse': type_analyse,
            'show_geopolitical': show_geopolitical,
            'show_cooperation': show_cooperation,
            'show_technical': show_technical,
            'threat_assessment': threat_assessment,
            'scenario': scenario
        }
    
    def display_strategic_metrics(self, df, config):
        """Métriques stratégiques avancées"""
        st.markdown('<h3 class="section-header">🎯 TABLEAU DE BORD STRATÉGIQUE UKRAINIEN</h3>', 
                   unsafe_allow_html=True)
        
        derniere_annee = df['Annee'].max()
        data_actuelle = df[df['Annee'] == derniere_annee].iloc[0]
        data_2014 = df[df['Annee'] == 2014].iloc[0]
        
        # Première ligne de métriques
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="metric-card">
                <h4>💰 BUDGET DÉFENSE TOTAL 2027</h4>
                <h2>{:.0f} Md$</h2>
                <p>📈 {:.1f}% du PIB ukrainien</p>
            </div>
            """.format(data_actuelle['Budget_Defense_Mds'], data_actuelle['PIB_Militaire_Pourcent']), 
            unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="metric-card">
                <h4>👥 EFFECTIFS TOTAUX</h4>
                <h2>{:,.0f}K</h2>
                <p>⚔️ +{:.1f}% depuis 2014</p>
            </div>
            """.format(data_actuelle['Personnel_Milliers'], 
                     ((data_actuelle['Personnel_Milliers'] - data_2014['Personnel_Milliers']) / data_2014['Personnel_Milliers']) * 100), 
            unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="nato-card">
                <h4>🛡️ CAPACITÉ DE DÉFENSE</h4>
                <h2>{:.0f}%</h2>
                <p>⚡ {} opérations/an</p>
            </div>
            """.format(data_actuelle['Capacite_Defense'], 
                     int(data_actuelle.get('Operations_Militaires', 0))), 
            unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class="aid-card">
                <h4>🤝 AIDE INTERNATIONALE</h4>
                <h2>{:.0f} Md$</h2>
                <p>🔧 {} formations OTAN</p>
            </div>
            """.format(data_actuelle['Aide_Internationale'], 
                     int(data_actuelle.get('Formation_OTAN', 0))), 
            unsafe_allow_html=True)
        
        # Deuxième ligne de métriques
        col5, col6, col7, col8 = st.columns(4)
        
        with col5:
            reduction_temps = ((data_2014['Temps_Reaction_Jours'] - data_actuelle['Temps_Reaction_Jours']) / 
                             data_2014['Temps_Reaction_Jours']) * 100
            st.metric(
                "⏱️ Temps de Réaction",
                f"{data_actuelle['Temps_Reaction_Jours']:.1f} jours",
                f"{reduction_temps:+.1f}%"
            )
        
        with col6:
            croissance_ad = ((data_actuelle['Couverture_Anti_Aerienne'] - data_2014['Couverture_Anti_Aerienne']) / 
                           data_2014['Couverture_Anti_Aerienne']) * 100
            st.metric(
                "🛡️ Défense Anti-Aérienne",
                f"{data_actuelle['Couverture_Anti_Aerienne']:.1f}%",
                f"{croissance_ad:+.1f}%"
            )
        
        with col7:
            if 'Systemes_SAM' in df.columns:
                croissance_sam = ((data_actuelle['Systemes_SAM'] - data_2014.get('Systemes_SAM', 10)) / 
                                data_2014.get('Systemes_SAM', 10)) * 100
                st.metric(
                    "🚀 Systèmes SAM",
                    f"{data_actuelle['Systemes_SAM']:.0f} unités",
                    f"{croissance_sam:+.1f}%"
                )
        
        with col8:
            st.metric(
                "📊 Préparation Opérationnelle",
                f"{data_actuelle['Readiness_Operative']:.1f}%",
                f"+{(data_actuelle['Readiness_Operative'] - data_2014['Readiness_Operative']):.1f}%"
            )
    
    def create_comprehensive_analysis(self, df, config):
        """Analyse complète multidimensionnelle"""
        st.markdown('<h3 class="section-header">📊 ANALYSE MULTIDIMENSIONNELLE UKRAINIENNE</h3>', 
                   unsafe_allow_html=True)
        
        # Graphiques principaux
        col1, col2 = st.columns(2)
        
        with col1:
            # Évolution des capacités principales
            fig = go.Figure()
            
            capacites = ['Readiness_Operative', 'Capacite_Defense', 'Cyber_Capabilities', 'Interoperabilite_OTAN']
            noms = ['Préparation Opér.', 'Capacité Défense', 'Capacités Cyber', 'Interopérabilité OTAN']
            couleurs = ['#0057B7', '#FFDD00', '#003F7F', '#0057B7']
            
            for i, (cap, nom, couleur) in enumerate(zip(capacites, noms, couleurs)):
                if cap in df.columns:
                    fig.add_trace(go.Scatter(
                        x=df['Annee'], y=df[cap],
                        mode='lines', name=nom,
                        line=dict(color=couleur, width=4),
                        hovertemplate=f"{nom}: %{{y:.1f}}%<extra></extra>"
                    ))
            
            fig.update_layout(
                title="📈 ÉVOLUTION DES CAPACITÉS STRATÉGIQUES UKRAINIENNES (2014-2027)",
                xaxis_title="Année",
                yaxis_title="Niveau de Capacité (%)",
                height=500,
                template="plotly_white",
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Analyse de l'aide internationale et des opérations
            strategic_data = []
            strategic_names = []
            
            if 'Aide_Internationale' in df.columns:
                strategic_data.append(df['Aide_Internationale'])
                strategic_names.append('Aide Internationale')
            
            if 'Operations_Militaires' in df.columns:
                strategic_data.append(df['Operations_Militaires'] / 10)  # Normalisation
                strategic_names.append('Opérations Militaires (x10)')
            
            if 'Production_Armements' in df.columns:
                strategic_data.append(df['Production_Armements'])
                strategic_names.append('Production d\'Armements')
            
            if strategic_data:
                fig = make_subplots(specs=[[{"secondary_y": True}]])
                
                for i, (data, nom) in enumerate(zip(strategic_data, strategic_names)):
                    fig.add_trace(
                        go.Scatter(x=df['Annee'], y=data, name=nom,
                                 line=dict(width=4)),
                        secondary_y=(i > 0)
                    )
                
                fig.update_layout(
                    title="🤝 AIDE ET OPÉRATIONS - ÉVOLUTION COMPARÉE",
                    height=500,
                    template="plotly_white"
                )
                st.plotly_chart(fig, use_container_width=True)
    
    def create_geopolitical_analysis(self, df, config):
        """Analyse géopolitique avancée"""
        st.markdown('<h3 class="section-header">🌍 CONTEXTE GÉOPOLITIQUE UKRAINIEN</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Architecture de sécurité ukrainienne
            st.markdown("""
            <div class="nato-card">
                <h4>🏛️ ARCHITECTURE DE SÉCURITÉ UKRAINIENNE</h4>
                <p><strong>OTAN:</strong> Partenaire Renforcé - Intégration progressive</p>
                <p><strong>Union Européenne:</strong> Accord d'Association - Candidature</p>
                <p><strong>Partenariats:</strong> États-Unis, Royaume-Uni, Pologne, Canada</p>
                <p><strong>Fronts:</strong> Est - Donbass, Sud - Crimée, Mer Noire</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Analyse des relations internationales
            st.markdown("""
            <div class="ukraine-card">
                <h4>🌐 RELATIONS STRATÉGIQUES</h4>
                <p><strong>États-Unis:</strong> Principal soutien militaire et financier</p>
                <p><strong>Russie:</strong> Agresseur - Guerre hybride et conventionnelle</p>
                <p><strong>Union Européenne:</strong> Soutien politique, économique et militaire</p>
                <p><strong>Pologne:</strong> Allié stratégique - Support logistique</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Analyse des défis sécuritaires
            challenges_data = {
                'Année': [2014, 2015, 2020, 2021, 2022, 2023, 2024],
                'Niveau_Defi': [7, 8, 6, 7, 10, 9, 8],  # sur 10
                'Evenement': ['Annexion Crimée', 'Guerre Donbass', 'Stagnation', 'Tensions', 'Invasion', 'Contre-offensive', 'Stabilisation']
            }
            challenges_df = pd.DataFrame(challenges_data)
            
            fig = px.line(challenges_df, x='Année', y='Niveau_Defi', 
                         title="📉 ÉVOLUTION DES DÉFIS SÉCURITAIRES",
                         labels={'Niveau_Defi': 'Niveau de Défi'},
                         markers=True)
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
            
            # Indice de résistance nationale
            resistance = [min(60 + 3.0 * (annee - 2014), 90) for annee in df['Annee']]
            fig = px.area(x=df['Annee'], y=resistance,
                         title="🕊️ RÉSISTANCE NATIONALE ET COHÉSION SOCIALE",
                         labels={'x': 'Année', 'y': 'Niveau de Résistance (%)'})
            fig.update_traces(fillcolor='rgba(0, 87, 183, 0.3)', line_color='#0057B7')
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
    
    def create_cooperation_analysis(self, df, config):
        """Analyse des coopérations internationales"""
        st.markdown('<h3 class="section-header">🤝 ANALYSE DES COOPÉRATIONS INTERNATIONALES</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Aide internationale par pays
            aid_data = []
            for pays, data in self.international_aid.items():
                aid_data.append({
                    'Pays': pays,
                    'Aide Militaire (Md$)': data['aide_militaire'],
                    'Aide Financière (Md$)': data['aide_financiere'],
                    'Équipement': data.get('equipement', 'Divers')
                })
            
            aid_df = pd.DataFrame(aid_data)
            
            fig = px.bar(aid_df, x='Pays', y='Aide Militaire (Md$)',
                        title="💰 AIDE MILITAIRE INTERNATIONALE",
                        color='Aide Militaire (Md$)',
                        color_continuous_scale='blues')
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Programmes majeurs
            programs_data = []
            for programme, details in self.major_programs.items():
                programs_data.append({
                    'Programme': programme,
                    'Pays': details['pays'],
                    'Statut': details['statut'],
                    'Type': details['type']
                })
            
            programs_df = pd.DataFrame(programs_data)
            
            fig = px.treemap(programs_df, path=['Type', 'Programme'],
                            title="🌳 PROGRAMMES D'ARMEMENT UKRAINIENS",
                            color='Type')
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
            
            # Carte des fronts
            st.markdown("""
            <div class="resistance-card">
                <h4>🗺️ DISPOSITIFS DE DÉFENSE UKRAINIENS</h4>
                <p><strong>Front Est:</strong> Donbass - Bakhmut, Avdiivka, Marinka</p>
                <p><strong>Front Sud:</strong> Kherson, Zaporijjia - Contre-offensive</p>
                <p><strong>Défense Anti-Aérienne:</strong> Protection des villes critiques</p>
                <p><strong>Forces Spéciales:</strong> Opérations derrière les lignes</p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_technical_analysis(self, df, config):
        """Analyse technique détaillée"""
        st.markdown('<h3 class="section-header">🔬 ANALYSE TECHNIQUE AVANCÉE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Analyse des systèmes d'armes
            systems_data = {
                'Système': ['HIMARS', 'Bayraktar TB2', 'Leopard 2A6', 
                           'NASAMS', 'CAESAR', 'Storm Shadow', 'Patriot'],
                'Portée (km)': [300, 150, 5, 40, 40, 250, 160],
                'Année Service': [2022, 2020, 2023, 2022, 2022, 2023, 2023],
                'Statut': ['Opérationnel', 'Opérationnel', 'Opérationnel', 'Opérationnel', 'Opérationnel', 'Opérationnel', 'Opérationnel']
            }
            systems_df = pd.DataFrame(systems_data)
            
            fig = px.scatter(systems_df, x='Portée (km)', y='Année Service', 
                           size='Portée (km)', color='Statut',
                           hover_name='Système', log_x=True,
                           title="🎯 CARACTÉRISTIQUES DES SYSTÈMES D'ARMES UKRAINIENS",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Analyse de la modernisation
            modernization_data = {
                'Domaine': ['Forces Aériennes', 'Forces Terrestres', 
                          'Défense Anti-Aérienne', 'Forces Navales', 'Cybersécurité'],
                'Niveau 2014': [30, 35, 25, 20, 30],
                'Niveau 2027': [75, 80, 85, 50, 80]
            }
            modern_df = pd.DataFrame(modernization_data)
            
            fig = go.Figure()
            fig.add_trace(go.Bar(name='2014', x=modern_df['Domaine'], y=modern_df['Niveau 2014'],
                                marker_color='#0057B7'))
            fig.add_trace(go.Bar(name='2027', x=modern_df['Domaine'], y=modern_df['Niveau 2027'],
                                marker_color='#FFDD00'))
            
            fig.update_layout(title="📈 MODERNISATION DES CAPACITÉS MILITAIRES UKRAINIENNES",
                             barmode='group', height=500)
            st.plotly_chart(fig, use_container_width=True)
            
            # Innovation technologique
            st.markdown("""
            <div class="innovation-card">
                <h4>🚀 TECHNOLOGIES D'AVANT-GARDE UKRAINIENNES</h4>
                <p><strong>Drones:</strong> Bayraktar TB2, Leleka, PD-2</p>
                <p><strong>Anti-navires:</strong> Neptune, Harpoon</p>
                <p><strong>Artillerie Précise:</strong> HIMARS, CAESAR, M777</p>
                <p><strong>Défense Aérienne:</strong> Patriot, IRIS-T, NASAMS</p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_doctrinal_analysis(self, config):
        """Analyse doctrinale avancée"""
        st.markdown('<h3 class="section-header">📚 ANALYSE DOCTRINALE UKRAINIENNE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="nato-card">
                <h4>🛡️ DOCTRINE DE DÉFENSE NATIONALE</h4>
                <p><strong>Défense territoriale:</strong> Protection du territoire</p>
                <p><strong>Résistance nationale:</strong> Mobilisation totale</p>
                <p><strong>Guerre hybride:</strong> Réponse aux menaces multiples</p>
                <p><strong>Défense active:</strong> Contre-offensives localisées</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="ukraine-card">
                <h4>🇺🇦 DOCTRINE OPÉRATIONNELLE</h4>
                <p><strong>Défense en profondeur:</strong> Échange espace-temps</p>
                <p><strong>Manœuvre:</strong> Frappes précises sur la logistique</p>
                <p><strong>Défense anti-aérienne:</strong> Protection des centres vitaux</p>
                <p><strong>Guerre de l'information:</strong> Lutte contre la désinformation</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="resistance-card">
                <h4>⚡ DOCTRINE DE RÉSISTANCE</h4>
                <p><strong>Résilience:</strong> Continuité des fonctions de l'État</p>
                <p><strong>Mobilisation:</strong> Participation de toute la société</p>
                <p><strong>Défense territoriale:</strong> Protection locale</p>
                <p><strong>Reconstruction:</strong> Pendant le conflit</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Principes opérationnels
        st.markdown("""
        <div class="nato-card">
            <h4>🎖️ PRINCIPES OPÉRATIONNELS DES FORCES UKRAINIENNES</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div><strong>• Flexibilité:</strong> Adaptation aux conditions changeantes</div>
                <div><strong>• Initiative:</strong> Exploitation des opportunités</div>
                <div><strong>• Précision:</strong> Utilisation efficace des ressources limitées</div>
                <div><strong>• Résilience:</strong> Capacité à encaisser les coups</div>
                <div><strong>• Innovation:</strong> Solutions créatives aux problèmes tactiques</div>
                <div><strong>• Interopérabilité:</strong> Intégration avec les systèmes OTAN</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def create_threat_assessment(self, df, config):
        """Évaluation avancée des menaces"""
        st.markdown('<h3 class="section-header">⚠️ ÉVALUATION STRATÉGIQUE DES MENACES</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Matrice des menaces
            threats_data = {
                'Type de Menace': ['Invasion Conventionnelle', 'Guerre Hybride', 'Attaques Missiles', 
                                 'Cyber Attaque', 'Guerre Économique', 'Déstabilisation Interne'],
                'Probabilité': [0.7, 0.9, 0.8, 0.9, 0.8, 0.6],
                'Impact': [0.9, 0.7, 0.8, 0.6, 0.7, 0.5],
                'Niveau Préparation': [0.8, 0.7, 0.8, 0.7, 0.5, 0.6]
            }
            threats_df = pd.DataFrame(threats_data)
            
            fig = px.scatter(threats_df, x='Probabilité', y='Impact', 
                           size='Niveau Préparation', color='Type de Menace',
                           title="🎯 MATRICE RISQUES - PROBABILITÉ VS IMPACT",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Capacités de réponse
            response_data = {
                'Scénario': ['Défense Territoriale', 'Contre-Offensive', 'Défense Anti-Aérienne', 
                           'Guerre Cyber', 'Soutien Civil', 'Résistance Prolongée'],
                'Forces Armées': [0.9, 0.8, 0.8, 0.6, 0.4, 0.7],
                'Partenaires': [0.7, 0.6, 0.8, 0.5, 0.6, 0.8],
                'Société': [0.6, 0.5, 0.4, 0.3, 0.9, 0.9]
            }
            response_df = pd.DataFrame(response_data)
            
            fig = go.Figure(data=[
                go.Bar(name='Forces Armées', x=response_df['Scénario'], y=response_df['Forces Armées']),
                go.Bar(name='Partenaires', x=response_df['Scénario'], y=response_df['Partenaires']),
                go.Bar(name='Société', x=response_df['Scénario'], y=response_df['Société'])
            ])
            fig.update_layout(title="🛡️ CAPACITÉS DE RÉPONSE PAR ACTEUR",
                             barmode='group', height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        # Recommandations stratégiques
        st.markdown("""
        <div class="ukraine-card">
            <h4>🎯 RECOMMANDATIONS STRATÉGIQUES UKRAINIENNES</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div><strong>• Modernisation continue:</strong> Alignement avec les standards OTAN</div>
                <div><strong>• Défense anti-aérienne:</strong> Priorité absolue pour la protection</div>
                <div><strong>• Capacités de projection:</strong> Forces de frappe précises</div>
                <div><strong>• Défense cyber:</strong> Protection des infrastructures critiques</div>
                <div><strong>• Résilience sociétale:</strong> Maintien de la cohésion nationale</div>
                <div><strong>• Partenariats stratégiques:</strong> Renforcement des alliances</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def create_programs_database(self):
        """Base de données des programmes ukrainiens"""
        st.markdown('<h3 class="section-header">🚀 BASE DE DONNÉES DES PROGRAMMES UKRAINIENS</h3>', 
                   unsafe_allow_html=True)
        
        programs_data = []
        for nom, specs in self.major_programs.items():
            programs_data.append({
                'Programme': nom,
                'Pays': specs['pays'],
                'Type': specs['type'],
                'Statut': specs['statut'],
                'Budget/Quantité': specs.get('budget', specs.get('quantite', 'N/A'))
            })
        
        programs_df = pd.DataFrame(programs_data)
        
        # Affichage interactif
        col1, col2 = st.columns([2, 1])
        
        with col1:
            fig = px.treemap(programs_df, path=['Type', 'Programme'],
                            title="🌳 CARTE DES PROGRAMMES D'ARMEMENT UKRAINIENS",
                            color='Type')
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("""
            <div class="innovation-card">
                <h4>📋 PROGRAMMES MAJEURS UKRAINIENS</h4>
            """, unsafe_allow_html=True)
            
            for programme in programs_data:
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.1); padding: 0.5rem; margin: 0.2rem 0; border-radius: 5px;">
                    <strong>{programme['Programme']}</strong><br>
                    🇺🇦 {programme['Pays']} • 🎯 {programme['Type']}<br>
                    📊 {programme['Statut']} • 💰 {programme['Budget/Quantité']}
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    def create_strategic_synthesis(self, df, config, controls):
        """Synthèse stratégique finale"""
        st.markdown('<h3 class="section-header">💎 SYNTHÈSE STRATÉGIQUE - DÉFENSE UKRAINIENNE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="nato-card">
                <h4>🏆 POINTS FORTS STRATÉGIQUES</h4>
                <div style="margin-top: 1rem;">
                    <div class="ukraine-card" style="margin: 0.5rem 0;">
                        <strong>🛡️ Résilience Nationale Exceptionnelle</strong>
                        <p>Cohésion sociale et capacité à résister malgré les pertes</p>
                    </div>
                    <div class="resistance-card" style="margin: 0.5rem 0;">
                        <strong>⚡ Adaptabilité Tactique</strong>
                        <p>Innovation rapide et solutions créatives sur le terrain</p>
                    </div>
                    <div class="aid-card" style="margin: 0.5rem 0;">
                        <strong>🤝 Soutien International Solide</strong>
                        <p>Aide militaire et financière massive des partenaires occidentaux</p>
                    </div>
                    <div class="innovation-card" style="margin: 0.5rem 0;">
                        <strong>🚀 Intégration Technologique Rapide</strong>
                        <p>Adoption efficace des systèmes d'armes modernes</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="ukraine-card">
                <h4>🎯 DÉFIS ET VULNÉRABILITÉS</h4>
                <div style="margin-top: 1rem;">
                    <div class="ukraine-card" style="margin: 0.5rem 0;">
                        <strong>💸 Dépendance à l'Aide Extérieure</strong>
                        <p>Fragilité en cas de réduction du soutien international</p>
                    </div>
                    <div class="ukraine-card" style="margin: 0.5rem 0;">
                        <strong>🔧 Base Industrielle Limitée</strong>
                        <p>Capacité de production nationale insuffisante</p>
                    </div>
                    <div class="ukraine-card" style="margin: 0.5rem 0;">
                        <strong>🌐 Supériorité Aérienne Adverse</strong>
                        <p>Désavantage face à l'aviation russe</p>
                    </div>
                    <div class="ukraine-card" style="margin: 0.5rem 0;">
                        <strong>⚡ Pression Démographique</strong>
                        <p>Impact de la guerre sur la population et l'économie</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Perspectives futures
        st.markdown("""
        <div class="metric-card">
            <h4>🔮 PERSPECTIVES STRATÉGIQUES 2027-2035</h4>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 1rem;">
                <div>
                    <h5>🛡️ INTÉGRATION OTAN</h5>
                    <p>Processus d'adhésion accéléré avec réformes structurelles</p>
                </div>
                <div>
                    <h5>🏭 INDUSTRIE DE DÉFENSE</h5>
                    <p>Développement de capacités nationales avec partenaires étrangers</p>
                </div>
                <div>
                    <h5>🚀 MODERNISATION TECHNOLOGIQUE</h5>
                    <p>Transition vers des systèmes de pointe et autonomie stratégique</p>
                </div>
                <div>
                    <h5>🕊️ RÉSOLUTION DU CONFLIT</h5>
                    <p>Scénarios variés de résolution avec garanties de sécurité</p>
                </div>
                <div>
                    <h5>🌍 RÉGIONALISATION</h5>
                    <p>Rôle de pivot dans la sécurité de l'Europe de l'Est</p>
                </div>
                <div>
                    <h5>💡 INNOVATION MILITAIRE</h5>
                    <p>Leader dans les tactiques de guerre hybride et innovation</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Scénarios stratégiques
        st.markdown("""
        <div class="nato-card">
            <h4>🎭 SCÉNARIOS STRATÉGIQUES FUTURS</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div>
                    <h5>🟢 SCÉNARIO OPTIMISTE</h5>
                    <p>Victoire militaire, reconstruction rapide, intégration OTAN/UE, prospérité économique</p>
                </div>
                <div>
                    <h5>🟡 SCÉNARIO INTERMÉDIAIRE</h5>
                    <p>Gel du conflit, reconstruction partielle, intégration progressive, tensions persistantes</p>
                </div>
                <div>
                    <h5>🔴 SCÉNARIO PESSIMISTE</h5>
                    <p>Conflit prolongé, dégradation économique, dépendance accrue, instabilité régionale</p>
                </div>
                <div>
                    <h5>🔵 SCÉNARIO TRANSFORMATIONNEL</h5>
                    <p>Réforme complète, leadership régional, innovation militaire, modèle de résilience</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def run_advanced_dashboard(self):
        """Exécute le dashboard avancé complet"""
        # Sidebar avancé
        controls = self.create_advanced_sidebar()
        
        # Header avancé
        self.display_advanced_header()
        
        # Génération des données avancées
        df, config = self.generate_advanced_data(controls['selection'])
        
        # Navigation par onglets avancés
        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
            "📊 Tableau de Bord", 
            "🔬 Analyse Technique", 
            "🌍 Contexte Géopolitique", 
            "🤝 Coopérations Internationales",
            "⚠️ Évaluation Menaces",
            "🚀 Programmes d'Armement",
            "💎 Synthèse Stratégique"
        ])
        
        with tab1:
            self.display_strategic_metrics(df, config)
            self.create_comprehensive_analysis(df, config)
        
        with tab2:
            self.create_technical_analysis(df, config)
        
        with tab3:
            if controls['show_geopolitical']:
                self.create_geopolitical_analysis(df, config)
        
        with tab4:
            if controls['show_cooperation']:
                self.create_cooperation_analysis(df, config)
        
        with tab5:
            if controls['threat_assessment']:
                self.create_threat_assessment(df, config)
        
        with tab6:
            if controls['show_technical']:
                self.create_programs_database()
        
        with tab7:
            self.create_strategic_synthesis(df, config, controls)

# Lancement du dashboard
if __name__ == "__main__":
    dashboard = DefenseUkraineDashboardAvance()
    dashboard.run_advanced_dashboard()