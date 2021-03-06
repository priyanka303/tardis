# functions that are important for the general usage of TARDIS

def run_tardis(config, atom_data=None):
    """
    This function is one of the core functions to run TARDIS from a given
    config object.

    It will return a model object containing

    Parameters
    ----------

    config: ~str or ~dict
        filename of configuration yaml file or dictionary

    atom_data: ~str or ~tardis.atomic.AtomData
        if atom_data is a string it is interpreted as a path to a file storing
        the atomic data. Atomic data to use for this TARDIS simulation. If set to None, the
        atomic data will be loaded according to keywords set in the configuration
        [default=None]
    """
    from tardis.io.config_reader import Configuration
    from tardis.simulation import Simulation
    from tardis.atomic import AtomData

    if atom_data is not None:
        try:
            atom_data = AtomData.from_hdf5(atom_data)
        except TypeError:
            atom_data = atom_data

    try:
        tardis_config = Configuration.from_yaml(config)
    except TypeError:
        tardis_config = Configuration.from_config_dict(config)

    simulation = Simulation.from_config(tardis_config, atom_data=atom_data)
    simulation.run()

    return simulation
