"""
The mechanism for defining a neuron model which can be simulated in the SNS Toolbox
William Nourse
May 7, 2021
Execute Order 66
"""

"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
IMPORTS
"""

from typing import Dict, Any
import warnings
import numbers

from __utilities__ import validColor, setTextColor

"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
BASE CLASS
"""

class Neuron:
    def __init__(self, name: str = 'Neuron',
                 color: str = 'white',
                 membraneCapacitance: float = 5.0,
                 membraneConductance: float = 1.0,
                 bias: float = 0.0) -> None:
        """
        Constructor for base Neuron class
        :param name:    Name of this neuron preset
        :param color:   Background fill color for the neuron, taken from the standard SVG colors
        :param membraneCapacitance: (nF)
        :param membraneConductance: (uS)
        :param bias:                Bias current (nA)
        """
        # TODO: Type checking
        self.params: Dict[str, Any] = {}
        if validColor(color):
            self.params['color'] = color
        else:
            warnings.warn('Specified color is not in the standard SVG set. Defaulting to white.')
            self.params['color'] = 'white'
        self.params['fontColor'] = setTextColor(self.params['color'])
        if isinstance(name,str):
            self.params['name'] = name
        else:
            raise ValueError('Neuron name must be a string')
        if isinstance(membraneCapacitance,numbers.Number):
            self.params['membraneCapacitance'] = membraneCapacitance
        else:
            raise ValueError('Membrane capacitance must be a number (int, float, double, etc.)')
        if isinstance(membraneConductance,numbers.Number):
            self.params['membraneConductance'] = membraneConductance
        else:
            raise ValueError('Membrane conductance must be a number (int, float, double, etc.')
        if isinstance(bias,numbers.Number):
            self.params['bias'] = bias
        else:
            raise ValueError('Bias must be a number (int, float, double, etc.')

"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
SPECIFIC MODELS
"""

# Only one of these (for now, or for forever *shrugs*)

class NonSpikingNeuron(Neuron):
    def __init__(self, **kwargs) -> None:
        """
        Classic non-spiking neuron model, whose dynamics are as follows:
        membraneCapacitance*dU/dt = -membraneConductance*U + bias + synaptic + external
        """
        super().__init__(**kwargs)
