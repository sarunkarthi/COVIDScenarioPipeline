import numpy as np
import pandas as pd
import datetime, time, multiprocessing, itertools, sys
import matplotlib.pyplot as plt
from COVIDScenarioPipeline.SEIR import seir, setup, results

class SomeStateSpatialSetup():
    """
        Setup for Maryland at the county scale.
    """
    def __init__(self):
        folder = 'west-coast/'
        self.data = pd.read_csv(f'data/{folder}geodataNEW.csv')
        self.mobility = np.loadtxt(f'data/{folder}mobilityNEW.txt')
        self.popnodes = self.data['pop2010'].to_numpy()
        self.nnodes = len(self.data)
        #self.counties_shp = gpd.read_file(f'data/{folder}somestate-counties-shp/somestate.shp')
        #self.counties_shp.sort_values('GEOID', inplace=True)

if __name__ == '__main__':          # For windows thread

    nsim = int(sys.argv[1])
    some_geo_id = float(sys.argv[2])
    some_geo_id1 = float(sys.argv[3])

    s = setup.Setup(setup_name = 'mid-SomeState',
                    spatial_setup = SomeStateSpatialSetup(),
                    nsim =  int( sys.argv[1]),
                    ti = datetime.date(2020, 3, 1),
                    tf = datetime.date(2020, 7, 1),
                    interactive = False,
                    write_csv = True)

    p = setup.COVID19Parameters(s)

    seeding_place = some_geo_id
    seeding_amount = [3]
    s.buildIC(seeding_places = [int(s.spatset.data[s.spatset.data['geoid'] == seeding_place].id)], 
            seeding_amount = seeding_amount)

    #s.set_filter(np.loadtxt('data/california/filter_github.txt')/100)

    tic = time.time()
    seir.onerun_SEIR(s, p, 0)
    print(f">>> Compilation done in {time.time()-tic} seconds...")

    seir = seir.run_parallel(s, p)

    results = results.Results(s, seir)

    simR = results.save_output_for_R(seir)

    results.plot_quick_summary()

    results.build_comp_data()  # Long !!

    nodes_to_plot = [int(s.spatset.data[s.spatset.data['geoid']== some_geo_id].id),
                    int(s.spatset.data[s.spatset.data['geoid']== some_geo_id1].id)]



    fig, axes = results.plot_all_comp(nodes_to_plot)
    fig.autofmt_xdate()

    results.plot_comp_mult('cumI', nodes_to_plot)
    fig, axes = results.plot_comp('cumI', nodes_to_plot)

    if s.interactive:
        plt.show()
