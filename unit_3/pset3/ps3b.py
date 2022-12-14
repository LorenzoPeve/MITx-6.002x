from __future__ import annotations
# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

import random
import numpy as np
import pylab
random.seed(0)
from random import choices as CH

from util import choices

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce.
    """

class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    Model the virus population inside a patient as if it were left untreated.
    """

    def __init__(self, maxBirthProb: float, clearProb: float) -> None:
        """
        Initialize a SimpleVirus instance.

        Args:
            maxBirthProb (float): Maximum reproduction probability between 0-1.
            clearProb (float): Maximum clearance probability between 0-1.
        """

        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        return self.maxBirthProb

    def getClearProb(self):
        return self.clearProb

    def doesClear(self) -> bool:
        """
        Stochastically determines whether this virus particle is cleared from
        the patient's body at a time step.
        """
        p = self.getClearProb()
        return choices([True, False], weights=[p, 1-p], k=1)[0]
    
    def reproduce(self, popDensity: float) -> SimpleVirus:
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        Args:
            popDensity (float): the population density defined as the current
                virus population divided by the maximum population.         
        
        Returns: 
            A new instance of the SimpleVirus class representing the offspring
            of this virus particle. The child should have the same maxBirthProb
            and clearProb values as this virus. 
        
        Raises a NoChildException if this virus particle does not reproduce.               
        """
        p = self.maxBirthProb * (1 - popDensity)
        reproduce = choices([True, False], weights=[p, 1-p], k=1)[0]
            
        if reproduce:
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            raise NoChildException

class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses: list[SimpleVirus], maxPop: int):
        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        return self.viruses

    def getMaxPop(self):
        return self.maxPop

    def getTotalPop(self) -> int:
        """Returns the size of the current total virus population."""
        return len(self.getViruses())

    def update(self) -> int:
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        1 - Determine whether each virus particle survives and updates the list
            of virus particles accordingly.   
        
        2 - The current population density is calculated. This population
            density value is used until the next call to update() 
        
        3 - Based on this value of population density, determine whether each 
            virus particle should reproduce and add offspring virus particles to 
            the list of viruses in this patient.                    

        Returns: 
            The total virus population at the end of the update.
        """

        # Remove viruses that dont survive
        for v in self.getViruses().copy():
            if v.doesClear():
                self.getViruses().remove(v)

        popDensity = self.getTotalPop() / self.getMaxPop()

        # Try reproducing each virus
        for v in self.getViruses().copy():
            try:
                new_virus = v.reproduce(popDensity)
            except NoChildException:
                continue

            if self.getTotalPop() + 1 <= self.getMaxPop():
                self.getViruses().append(new_virus)
            else:
                break

        return self.getTotalPop()

def simulationWithoutDrug(
        numViruses: int, maxPop: int, maxBirthProb: float, 
        clearProb: float, numTrials: int):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).

    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    Args:
        numViruses (int): number of SimpleVirus to create for patient.
        maxPop (int): maximum virus population for patient.
        maxBirthProb (float): Maximum reproduction probability.   
        clearProb (float): Maximum clearance probability.
        numTrials (int): number of simulation runs to execute.
    """
    T = 300
    pop_at_time_step = [0 for _ in range(T)]
    for i in range(numTrials):

        v = [SimpleVirus(maxBirthProb, clearProb) for _ in range(numViruses)]
        p = Patient(v, maxPop)

        for t in range(T):
            pop_at_time_step[t] += p.update()

    average_pop = [i/numTrials for i in pop_at_time_step]
    return average_pop

def plot_population_over_time(pop: list) -> None:
    
    pylab.plot(pop, label = "SimpleVirus")
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc = "best")
    pylab.show()


class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(
        self, maxBirthProb: float, clearProb: float, 
        resistances: dict, mutProb:float):

        """
        Args:
            maxBirthProb (float): Maximum reproduction probability between 0-1.
            clearProb (float): Maximum clearance probability between 0-1.
            resistances (dict): A dictionary of drug names (strings) mapping to
                the state of this virus particle's resistance (either True or 
                False) to each drug. eg. {'guttagonol':False, 'srinol':False},
                means that this virus particle is resistant to neither
                guttagonol nor srinol.
            
            mutProb (float): Mutation probability for this virus particle. This
                is the probability of the offspring acquiring or losing
                resistance to a drug.
        """

        super().__init__(maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb

    def getResistances(self):
        return self.resistances

    def getMutProb(self):
        return self.mutProb

    def isResistantTo(self, drug: str) -> bool:
        """
        Get the state of this virus particle's resistance to a drug. This 
        method is called by getResistPop() in TreatedPatient to determine how
        many virus particles have resistance to a drug.       

        Returns True if this virus instance is resistant to the drug, False
        otherwise.
        """
        resistant = self.resistances.get(drug)
        if resistant:
            return resistant
        return False

    def reproduce(self, popDensity, activeDrugs: list) -> ResistantVirus:
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the
        drugs in the activeDrugs list.

        The virus reproduces with probability: maxBirthProb * (1-popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        Args
            popDensity (float): the population density, defined as the current
                virus population divided by the maximum population       

            activeDrugs (list[str]): a list of the drug names acting on this
                virus particle.

        Returns:
            A new instance of the ResistantVirus class representing the 
            offspring of this virus particle. The child should have the same
            maxBirthProb and clearProb values as this virus.
        
        Raises a NoChildException if this virus particle does not reproduce.
        """

        def _mutation(p_mute: float, resistances: dict):

            inherited_resistances = {}

            for k, v in resistances.items():

                inherit = choices([True, False], weights=[1-p_mute, p_mute])[0]
                if inherit:
                    inherited_resistances[k] = v
                else:
                    inherited_resistances[k] = not v
            
            return inherited_resistances

        for drug in activeDrugs:
            if not self.isResistantTo(drug):
                raise NoChildException
        
        p = self.maxBirthProb * (1 - popDensity)
        reproduce = choices([True, False], weights=[p, 1-p], k=1)[0]
            
        if reproduce:
            inherited_resistances = _mutation(self.mutProb, self.resistances)

            return ResistantVirus(
                self.maxBirthProb, self.clearProb, inherited_resistances,
                self.mutProb)
        else:
            raise NoChildException

class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses: list[SimpleVirus], maxPop: int) -> None:

        self.viruses = viruses
        self.maxPop = maxPop
        self.drugs = []

    def addPrescription(self, newDrug: list) -> None:
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        Args:
            newDrug (str): The name of the drug to administer to the patient.
        """

        if newDrug not in self.drugs:
            self.drugs.append(newDrug)

    def getPrescriptions(self) -> list:
        return self.drugs

    def getResistPop(self, drugResist: list[str]) -> int:
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        Args:
            drugResist: Which drug resistances to include in the population.
            e.g. ['guttagonol'] or ['guttagonol', 'srinol'].

        Returns: 
            The population of viruses with resistances to all drugs in the 
            drugResist list.
        """

        c = 0
        for v in self.viruses:
            for d in drugResist:
                if not v.isResistantTo(d):
                    break
            else:
                c += 1
        return c

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        Returns: 
            The total virus population at the end of the update.
        """

        # Remove viruses that dont survive
        for v in self.getViruses().copy():
            if v.doesClear():
                self.getViruses().remove(v)

        popDensity = self.getTotalPop() / self.getMaxPop()

        # Try reproducing each virus
        for v in self.getViruses().copy():
            try:
                new_virus = v.reproduce(popDensity, self.drugs)
            except NoChildException:
                continue

            if self.getTotalPop() + 1 <= self.getMaxPop():
                self.getViruses().append(new_virus)
            else:
                break

        return self.getTotalPop()


def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.
    
    At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    T = 150
    pop_at_time_step = [0 for _ in range(T*2)]
    pop_gutt_time_step = [0 for _ in range(T*2)]
    for i in range(numTrials):

        # 1. instantiates a patient
        v = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) 
            for _ in range(numViruses)]

        p = TreatedPatient(v, maxPop)

        # 2. First 150 timesteps
        for t in range(T):
            pop_at_time_step[t] += p.update()
            pop_gutt_time_step[t] += p.getResistPop(['guttagonol'])

        # 3. Adds guttagonol
        p.addPrescription('guttagonol')

        # 4. Second 150 timesteps
        for t in range(T,T*2):
            pop_at_time_step[t] += p.update()
            pop_gutt_time_step[t] += p.getResistPop(['guttagonol'])

    average_pop = [i/numTrials for i in pop_at_time_step]
    average_gutt_pop = [i/numTrials for i in pop_gutt_time_step]
    
    pylab.plot(average_pop, label = "TotalPop")
    pylab.plot(average_gutt_pop, label = "Guttagonol-resistant Virus")
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc = "best")
    pylab.show()