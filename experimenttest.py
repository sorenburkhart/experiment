"""Unit test for experiment.py
"""

__author__ = "Soren Burkhart (soren.burkhart@gmail.com)"
__version__ = "$Revision: 0.21 $"
__date__ = "$Date: 2010/01/29 13:36:22 $"
__copyright__ = "Copyright (c) 2010 Soren Burkhart"
__license__ = "Python"

import unittest

import experiment

class ReplicateTest(unittest.TestCase):
    def testReplicate(self):
        replicate_number = 1
        data = ['1.246760943','0.792779965','1.269427218','1.378652162','1.680346882','0.878759183','1.035938725','0.226080197','1.346046107','0.539900233','0.969170341','0','1.148940294','1.080923774','1.149251194','0.93709106','1.026342394','0.89781223','1.142491229','','','','']
        r = experiment.Replicate(replicate_number, data)
        self.assertEqual(1,
                         r.number)
        self.assertEqual([1.246760943, 0.792779965, 1.269427218, 1.378652162, 1.680346882, 0.878759183, 1.035938725, 0.226080197, 1.346046107, 0.539900233, 0.969170341, 0, 1.148940294, 1.080923774, 1.149251194, 0.93709106, 1.026342394, 0.89781223, 1.142491229, None, None, None, None],
                         r.data)
                         
class ObservationTest(unittest.TestCase):
    def testObservation(self):
        """Tests the Observation class which holds the replicate observations for a specific time period"""
        o = experiment.Observation(1)
        self.assertEqual(1, o.time)
        self.assertEqual(0, len(o.replicates))
        
        o.add_replicate_data(['2.219707744','1.058746906','1.259369068','1.400074223','1.994297498','1.235476606','1.072133722','0.397180827','1.319687718','2.197068251','0.955004734','0','1.224131728','1.161717019','1.095500908','1.056548163','1.133690855','1.198000449','0.945766194','','','',''])
        o.add_replicate_data(['1.246760943','0.792779965','1.269427218','1.378652162','1.680346882','0.878759183','1.035938725','0.226080197','1.346046107','0.539900233','0.969170341','0','1.148940294','1.080923774','1.149251194','0.93709106','1.026342394','0.89781223','1.142491229','','','',''])
        o.add_replicate_data(['1.189143899','0.613301819','1.13434527','0.77941355','0.930129047','0.698324732','0.781304145','0.083516039','1.10519722','1.224550934','1.016973917','0','1.145171212','0.927181017','0.9495541','0.972851398','1.054137328','0.988972847','1.065268164','','','',''])
        o.add_replicate_data(['1.290890247','0.801868457','1.353733071','1.270211675','1.532752169','1.117541643','1.003312009','0.030080408','0.769686133','0.697495993','1.05768815','0','0.833002123','1.128348992','1.143324655','0.983276287','1.016563164','1.032957809','0.98355332','','','',''])
        o.add_replicate_data(['0.526557764','0.527912575','0.74103442','0.955401506','0.431842757','1.050134439','1.13331111','0','0.815341125','0.88325358','0.97624306','0.027980604','0.660670779','0.658289522','0.627003723','1.046040531','0.708042282','0.808906526','0.87479638','','','',''])
        o.add_replicate_data(['1.130197768','1.942543437','2.013391223','1.283272996','1.282171275','1.019763398','0.974000288','0','0.644041698','0.457731009','1.024919797','0.001199693','0.988083864','1.043539676','1.035365419','1.004192561','1.061223978','1.073350139','0.988124712','','','',''])

        self.assertEqual(6, len(o.replicates))
        self.assertEqual([2.2197077439999999, 1.0587469060000001, 1.259369068, 1.4000742230000001, 1.9942974979999999, 1.235476606, 1.072133722, 0.39718082700000001, 1.319687718, 2.1970682510000001, 0.95500473399999997, 0.0, 1.2241317279999999, 1.1617170189999999, 1.095500908, 1.056548163, 1.133690855, 1.198000449, 0.94576619399999995, None, None, None, None],
                         o.replicates[0].data)
        self.assertEqual([1.246760943, 0.79277996500000003, 1.2694272179999999, 1.3786521620000001, 1.680346882, 0.878759183, 1.0359387250000001, 0.22608019700000001, 1.346046107, 0.53990023300000001, 0.96917034099999999, 0.0, 1.148940294, 1.0809237739999999, 1.1492511940000001, 0.93709105999999998, 1.026342394, 0.89781222999999999, 1.142491229, None, None, None, None],
                         o.replicates[1].data)
        self.assertEqual([1.1891438990000001, 0.61330181900000003, 1.1343452700000001, 0.77941355000000001, 0.93012904699999999, 0.698324732, 0.78130414500000001, 0.083516039, 1.10519722, 1.224550934, 1.0169739170000001, 0.0, 1.1451712119999999, 0.927181017, 0.94955409999999996, 0.97285139799999998, 1.0541373279999999, 0.98897284699999999, 1.0652681639999999, None, None, None, None],
                         o.replicates[2].data)
        self.assertEqual([1.2908902470000001, 0.80186845699999998, 1.353733071, 1.2702116750000001, 1.5327521690000001, 1.117541643, 1.0033120090000001, 0.030080407999999999, 0.76968613299999999, 0.69749599299999998, 1.0576881499999999, 0.0, 0.83300212299999998, 1.1283489920000001, 1.143324655, 0.98327628700000003, 1.0165631639999999, 1.032957809, 0.98355331999999995, None, None, None, None],
                         o.replicates[3].data)
        self.assertEqual([0.52655776399999998, 0.527912575, 0.74103441999999997, 0.95540150599999996, 0.43184275700000002, 1.050134439, 1.13331111, 0.0, 0.815341125, 0.88325357999999998, 0.97624306000000005, 0.027980603999999999, 0.66067077900000004, 0.65828952200000002, 0.62700372299999996, 1.0460405310000001, 0.70804228199999997, 0.80890652600000001, 0.87479638000000004, None, None, None, None],
                         o.replicates[4].data)
        self.assertEqual([1.1301977679999999, 1.9425434370000001, 2.0133912230000002, 1.283272996, 1.2821712750000001, 1.019763398, 0.97400028800000005, 0.0, 0.644041698, 0.45773100900000002, 1.0249197969999999, 0.0011996929999999999, 0.98808386400000003, 1.043539676, 1.0353654189999999, 1.004192561, 1.0612239779999999, 1.073350139, 0.98812471199999996, None, None, None, None],
                         o.replicates[5].data)
        self.assertEqual([1.2672097275, 0.9561921931666667, 1.2952167116666666, 1.1778376853333334, 1.3085899380000001, 1.0000000001666667, 0.99999999983333332, 0.12280957850000002, 1.0000000001666665, 1.0, 0.99999999983333332, 0.0048633828333333332, 1.0, 1.0, 0.99999999983333321, 1.0, 1.0000000001666667, 1.0, 0.99999999983333332, None, None, None, None],
                         o.means())
class HeaderTest(unittest.TestCase):
    def testHeader(self):
        """Tests the Header class which holds the headers for the experiment"""
        input_header = ['TNF (ng/ml)', 'EGF (ng/ml)', 'Ins (ng/ml)', 'C225 (\xc2\xb5g/ml)', 'IL-1ra (\xc2\xb5g/ml)']
        time_header = 'Time (min)'
        replicate_header = 'Replicate'
        observation_header = ['ERK', 'Akt', 'JNK', 'IKK', 'MK2', 'pMEK', 'pAkt (IB)', 'pFKHR', 'pIRS1-636', 'pIRS1-896', 'ProC8', 'ClvC8', 'ProC3', 'pEGFR', 'tEGFR', 'ptEGFR', 'pAkt (AA)', 'tAkt', 'ptAkt', 'CC3/CCK', 'Annexin', 'PI', 'Sub G1']
        h = experiment.Header(input_header, time_header, replicate_header, observation_header)
        self.assertEqual(input_header,
                         h.input_header)
        self.assertEqual(time_header,
                         h.time_header)
        self.assertEqual(replicate_header,
                         h.replicate_header)
        self.assertEqual(observation_header,
                         h.observation_header)

class ExperimentTest(unittest.TestCase):
    def testExperiment(self):
        input_header = ['TNF (ng/ml)', 'EGF (ng/ml)', 'Ins (ng/ml)', 'C225 (\xc2\xb5g/ml)', 'IL-1ra (\xc2\xb5g/ml)']
        input_values = ['0','0','0','0','0']
        time_header = 'Time (min)'
        replicate_header = 'Replicate' 
        observation_header = ['ERK', 'Akt', 'JNK', 'IKK', 'MK2', 'pMEK', 'pAkt (IB)', 'pFKHR', 'pIRS1-636', 'pIRS1-896', 'ProC8', 'ClvC8', 'ProC3', 'pEGFR', 'tEGFR', 'ptEGFR', 'pAkt (AA)', 'tAkt', 'ptAkt', 'CC3/CCK', 'Annexin', 'PI', 'Sub G1']
        e = experiment.Experiment(input_header, input_values, time_header, replicate_header, observation_header)

        # Add replicate data for time = 0
        e.add_row_of_data(['0','0','0','0','0','0','1','2.219707744','1.058746906','1.259369068','1.400074223','1.994297498','1.235476606','1.072133722','0.397180827','1.319687718','2.197068251','0.955004734','0','1.224131728','1.161717019','1.095500908','1.056548163','1.133690855','1.198000449','0.945766194','','','',''])
        e.add_row_of_data(['0','0','0','0','0','0','2','1.246760943','0.792779965','1.269427218','1.378652162','1.680346882','0.878759183','1.035938725','0.226080197','1.346046107','0.539900233','0.969170341','0','1.148940294','1.080923774','1.149251194','0.93709106','1.026342394','0.89781223','1.142491229','','','',''])
        e.add_row_of_data(['0','0','0','0','0','0','3','1.189143899','0.613301819','1.13434527','0.77941355','0.930129047','0.698324732','0.781304145','0.083516039','1.10519722','1.224550934','1.016973917','0','1.145171212','0.927181017','0.9495541','0.972851398','1.054137328','0.988972847','1.065268164','','','',''])
        e.add_row_of_data(['0','0','0','0','0','0','4','1.290890247','0.801868457','1.353733071','1.270211675','1.532752169','1.117541643','1.003312009','0.030080408','0.769686133','0.697495993','1.05768815','0','0.833002123','1.128348992','1.143324655','0.983276287','1.016563164','1.032957809','0.98355332','','','',''])
        e.add_row_of_data(['0','0','0','0','0','0','5','0.526557764','0.527912575','0.74103442','0.955401506','0.431842757','1.050134439','1.13331111','0','0.815341125','0.88325358','0.97624306','0.027980604','0.660670779','0.658289522','0.627003723','1.046040531','0.708042282','0.808906526','0.87479638','','','',''])
        e.add_row_of_data(['0','0','0','0','0','0','6','1.130197768','1.942543437','2.013391223','1.283272996','1.282171275','1.019763398','0.974000288','0','0.644041698','0.457731009','1.024919797','0.001199693','0.988083864','1.043539676','1.035365419','1.004192561','1.061223978','1.073350139','0.988124712','','','',''])

        # Add replicate data for time = 5
        e.add_row_of_data(['0','0','0','0','0','5','1','2.219707744','1.058746906','1.259369068','1.400074223','1.994297498','1.235476606','1.072133722','0.397180827','1.319687718','2.197068251','0.955004734','0','1.224131728','1.161717019','1.095500908','1.056548163','1.133690855','1.198000449','0.945766194','','','',''])
        e.add_row_of_data(['0','0','0','0','0','5','2','1.246760943','0.792779965','1.269427218','1.378652162','1.680346882','0.878759183','1.035938725','0.226080197','1.346046107','0.539900233','0.969170341','0','1.148940294','1.080923774','1.149251194','0.93709106','1.026342394','0.89781223','1.142491229','','','',''])
        e.add_row_of_data(['0','0','0','0','0','5','3','1.189143899','0.613301819','1.13434527','0.77941355','0.930129047','0.698324732','0.781304145','0.083516039','1.10519722','1.224550934','1.016973917','0','1.145171212','0.927181017','0.9495541','0.972851398','1.054137328','0.988972847','1.065268164','','','',''])
        e.add_row_of_data(['0','0','0','0','0','5','4','1.290890247','0.801868457','1.353733071','1.270211675','1.532752169','1.117541643','1.003312009','0.030080408','0.769686133','0.697495993','1.05768815','0','0.833002123','1.128348992','1.143324655','0.983276287','1.016563164','1.032957809','0.98355332','','','',''])
        e.add_row_of_data(['0','0','0','0','0','5','5','0.526557764','0.527912575','0.74103442','0.955401506','0.431842757','1.050134439','1.13331111','0','0.815341125','0.88325358','0.97624306','0.027980604','0.660670779','0.658289522','0.627003723','1.046040531','0.708042282','0.808906526','0.87479638','','','',''])
        e.add_row_of_data(['0','0','0','0','0','5','6','1.130197768','1.942543437','2.013391223','1.283272996','1.282171275','1.019763398','0.974000288','0','0.644041698','0.457731009','1.024919797','0.001199693','0.988083864','1.043539676','1.035365419','1.004192561','1.061223978','1.073350139','0.988124712','','','',''])
        
        self.assertEqual(input_header,
                         e.header.input_header)
        self.assertEqual(observation_header,
                         e.header.observation_header)
        self.assertEqual(time_header,
                         e.header.time_header)
        self.assertEqual(replicate_header,
                         e.header.replicate_header)
        self.assertEqual('Experiment: 0 TNF (ng/ml) 0 EGF (ng/ml) 0 Ins (ng/ml) 0 C225 (\xc2\xb5g/ml) 0 IL-1ra (\xc2\xb5g/ml)',
                         e.description)
        
        self.assertEqual(2, len(e.observations))
        self.assertEqual(6, len(e.observations[0].replicates))
        # Check replicate data for observation at time = 0
        self.assertEqual([2.2197077439999999, 1.0587469060000001, 1.259369068, 1.4000742230000001, 1.9942974979999999, 1.235476606, 1.072133722, 0.39718082700000001, 1.319687718, 2.1970682510000001, 0.95500473399999997, 0.0, 1.2241317279999999, 1.1617170189999999, 1.095500908, 1.056548163, 1.133690855, 1.198000449, 0.94576619399999995, None, None, None, None],
                         e.observations[0].replicates[0].data)
        self.assertEqual([1.246760943, 0.79277996500000003, 1.2694272179999999, 1.3786521620000001, 1.680346882, 0.878759183, 1.0359387250000001, 0.22608019700000001, 1.346046107, 0.53990023300000001, 0.96917034099999999, 0.0, 1.148940294, 1.0809237739999999, 1.1492511940000001, 0.93709105999999998, 1.026342394, 0.89781222999999999, 1.142491229, None, None, None, None],
                         e.observations[0].replicates[1].data)
        self.assertEqual([1.1891438990000001, 0.61330181900000003, 1.1343452700000001, 0.77941355000000001, 0.93012904699999999, 0.698324732, 0.78130414500000001, 0.083516039, 1.10519722, 1.224550934, 1.0169739170000001, 0.0, 1.1451712119999999, 0.927181017, 0.94955409999999996, 0.97285139799999998, 1.0541373279999999, 0.98897284699999999, 1.0652681639999999, None, None, None, None],
                         e.observations[0].replicates[2].data)
        self.assertEqual([1.2908902470000001, 0.80186845699999998, 1.353733071, 1.2702116750000001, 1.5327521690000001, 1.117541643, 1.0033120090000001, 0.030080407999999999, 0.76968613299999999, 0.69749599299999998, 1.0576881499999999, 0.0, 0.83300212299999998, 1.1283489920000001, 1.143324655, 0.98327628700000003, 1.0165631639999999, 1.032957809, 0.98355331999999995, None, None, None, None],
                         e.observations[0].replicates[3].data)
        self.assertEqual([0.52655776399999998, 0.527912575, 0.74103441999999997, 0.95540150599999996, 0.43184275700000002, 1.050134439, 1.13331111, 0.0, 0.815341125, 0.88325357999999998, 0.97624306000000005, 0.027980603999999999, 0.66067077900000004, 0.65828952200000002, 0.62700372299999996, 1.0460405310000001, 0.70804228199999997, 0.80890652600000001, 0.87479638000000004, None, None, None, None],
                         e.observations[0].replicates[4].data)
        self.assertEqual([1.1301977679999999, 1.9425434370000001, 2.0133912230000002, 1.283272996, 1.2821712750000001, 1.019763398, 0.97400028800000005, 0.0, 0.644041698, 0.45773100900000002, 1.0249197969999999, 0.0011996929999999999, 0.98808386400000003, 1.043539676, 1.0353654189999999, 1.004192561, 1.0612239779999999, 1.073350139, 0.98812471199999996, None, None, None, None],
                         e.observations[0].replicates[5].data)

        # Check replicate data for observation at time = 5
        self.assertEqual([2.2197077439999999, 1.0587469060000001, 1.259369068, 1.4000742230000001, 1.9942974979999999, 1.235476606, 1.072133722, 0.39718082700000001, 1.319687718, 2.1970682510000001, 0.95500473399999997, 0.0, 1.2241317279999999, 1.1617170189999999, 1.095500908, 1.056548163, 1.133690855, 1.198000449, 0.94576619399999995, None, None, None, None],
                         e.observations[1].replicates[0].data)
        self.assertEqual([1.246760943, 0.79277996500000003, 1.2694272179999999, 1.3786521620000001, 1.680346882, 0.878759183, 1.0359387250000001, 0.22608019700000001, 1.346046107, 0.53990023300000001, 0.96917034099999999, 0.0, 1.148940294, 1.0809237739999999, 1.1492511940000001, 0.93709105999999998, 1.026342394, 0.89781222999999999, 1.142491229, None, None, None, None],
                         e.observations[1].replicates[1].data)
        self.assertEqual([1.1891438990000001, 0.61330181900000003, 1.1343452700000001, 0.77941355000000001, 0.93012904699999999, 0.698324732, 0.78130414500000001, 0.083516039, 1.10519722, 1.224550934, 1.0169739170000001, 0.0, 1.1451712119999999, 0.927181017, 0.94955409999999996, 0.97285139799999998, 1.0541373279999999, 0.98897284699999999, 1.0652681639999999, None, None, None, None],
                         e.observations[1].replicates[2].data)
        self.assertEqual([1.2908902470000001, 0.80186845699999998, 1.353733071, 1.2702116750000001, 1.5327521690000001, 1.117541643, 1.0033120090000001, 0.030080407999999999, 0.76968613299999999, 0.69749599299999998, 1.0576881499999999, 0.0, 0.83300212299999998, 1.1283489920000001, 1.143324655, 0.98327628700000003, 1.0165631639999999, 1.032957809, 0.98355331999999995, None, None, None, None],
                         e.observations[1].replicates[3].data)
        self.assertEqual([0.52655776399999998, 0.527912575, 0.74103441999999997, 0.95540150599999996, 0.43184275700000002, 1.050134439, 1.13331111, 0.0, 0.815341125, 0.88325357999999998, 0.97624306000000005, 0.027980603999999999, 0.66067077900000004, 0.65828952200000002, 0.62700372299999996, 1.0460405310000001, 0.70804228199999997, 0.80890652600000001, 0.87479638000000004, None, None, None, None],
                         e.observations[1].replicates[4].data)
        self.assertEqual([1.1301977679999999, 1.9425434370000001, 2.0133912230000002, 1.283272996, 1.2821712750000001, 1.019763398, 0.97400028800000005, 0.0, 0.644041698, 0.45773100900000002, 1.0249197969999999, 0.0011996929999999999, 0.98808386400000003, 1.043539676, 1.0353654189999999, 1.004192561, 1.0612239779999999, 1.073350139, 0.98812471199999996, None, None, None, None],
                         e.observations[1].replicates[5].data)

       
class ExperimentLoaderTest(unittest.TestCase):
    def testLoadNullExperimentFile(self):
        """should not load a missing file"""
        self.assertRaises(experiment.FileMissingError,
                          experiment.Loader, None, 5)
    
    def testLoadValidExperimentFile(self):
        """should load valid experiment file and return an array of experiments"""
        file = open("MOAD_dataset.csv")
        loader = experiment.Loader(file,5)
        self.assertTrue(loader)
        loader.load()
        self.assertEqual(12,
                        len(loader.experiments))
        
        # Test first and last experiment
        e = loader.experiments[0]

        self.assertEqual(['TNF (ng/ml)', 'EGF (ng/ml)', 'Ins (ng/ml)', 'C225 (\xc2\xb5g/ml)', 'IL-1ra (\xc2\xb5g/ml)'],
                         e.header.input_header)
        self.assertEqual(['ERK', 'Akt', 'JNK', 'IKK', 'MK2', 'pMEK', 'pAkt (IB)', 'pFKHR', 'pIRS1-636', 'pIRS1-896', 'ProC8', 'ClvC8', 'ProC3', 'pEGFR', 'tEGFR', 'ptEGFR', 'pAkt (AA)', 'tAkt', 'ptAkt', 'CC3/CCK', 'Annexin', 'PI', 'Sub G1'],
                         e.header.observation_header)
        self.assertEqual('Time (min)',
                         e.header.time_header)
        self.assertEqual('Replicate',
                         e.header.replicate_header)
        self.assertEqual('Experiment: 0 TNF (ng/ml) 0 EGF (ng/ml) 0 Ins (ng/ml) 0 C225 (\xc2\xb5g/ml) 0 IL-1ra (\xc2\xb5g/ml)',
                         e.description)
        self.assertEqual(14,
                         len(e.observations))
        self.assertEqual(6,
                         len(e.observations[0].replicates))
        self.assertEqual([2.219707744, 1.058746906, 1.259369068, 1.400074223, 1.994297498, 1.235476606, 1.072133722, 0.397180827, 1.319687718, 2.197068251, 0.955004734, 0, 1.224131728, 1.161717019, 1.095500908, 1.056548163, 1.133690855, 1.198000449, 0.945766194, None, None, None, None],
                         e.observations[0].replicates[0].data)
        self.assertEqual([1.246760943, 0.792779965, 1.269427218, 1.378652162, 1.680346882, 0.878759183, 1.035938725, 0.226080197, 1.346046107, 0.539900233, 0.969170341, 0, 1.148940294, 1.080923774, 1.149251194, 0.93709106, 1.026342394, 0.89781223, 1.142491229, None, None, None, None],
                         e.observations[0].replicates[1].data)
        self.assertEqual([1.189143899, 0.613301819, 1.13434527, 0.77941355, 0.930129047, 0.698324732, 0.781304145, 0.083516039, 1.10519722, 1.224550934, 1.016973917, 0, 1.145171212, 0.927181017, 0.9495541, 0.972851398, 1.054137328, 0.988972847, 1.065268164, None, None, None, None],
                         e.observations[0].replicates[2].data)
        self.assertEqual([1.290890247, 0.801868457, 1.353733071, 1.270211675, 1.532752169, 1.117541643, 1.003312009, 0.030080408, 0.769686133, 0.697495993, 1.05768815, 0, 0.833002123, 1.128348992, 1.143324655, 0.983276287, 1.016563164, 1.032957809, 0.98355332, None, None, None, None],
                         e.observations[0].replicates[3].data)
        self.assertEqual([0.526557764, 0.527912575, 0.74103442, 0.955401506, 0.431842757, 1.050134439, 1.13331111, 0, 0.815341125, 0.88325358, 0.97624306, 0.027980604, 0.660670779, 0.658289522, 0.627003723, 1.046040531, 0.708042282, 0.808906526, 0.87479638, None, None, None, None],
                         e.observations[0].replicates[4].data)
        self.assertEqual([1.130197768, 1.942543437, 2.013391223, 1.283272996, 1.282171275, 1.019763398, 0.974000288, 0, 0.644041698, 0.457731009, 1.024919797, 0.001199693, 0.988083864, 1.043539676, 1.035365419, 1.004192561, 1.061223978, 1.073350139, 0.988124712, None, None, None, None],
                         e.observations[0].replicates[5].data)
        
        e = loader.experiments[-1]                
        self.assertEqual(['TNF (ng/ml)', 'EGF (ng/ml)', 'Ins (ng/ml)', 'C225 (\xc2\xb5g/ml)', 'IL-1ra (\xc2\xb5g/ml)'],
                         e.header.input_header)
        self.assertEqual( ['ERK', 'Akt', 'JNK', 'IKK', 'MK2', 'pMEK', 'pAkt (IB)', 'pFKHR', 'pIRS1-636', 'pIRS1-896', 'ProC8', 'ClvC8', 'ProC3', 'pEGFR', 'tEGFR', 'ptEGFR', 'pAkt (AA)', 'tAkt', 'ptAkt', 'CC3/CCK', 'Annexin', 'PI', 'Sub G1'],
                         e.header.observation_header)
        self.assertEqual('Experiment: 100 TNF (ng/ml) 0 EGF (ng/ml) 0 Ins (ng/ml) 0 C225 (\xc2\xb5g/ml) 10 IL-1ra (\xc2\xb5g/ml)',
                         e.description)
        self.assertEqual(14,
                         len(e.observations))
        self.assertEqual(6,
                         len(e.observations[0].replicates))
        self.assertEqual([1.324634747, 0.929754821, 1.429329435, 1.096052638, 0.837174972, 1.004008797, 1.07863371, 0.074538395, 0.856347465, 1.046510575, 1.257627204, 0.010032981, 0.922171013, 0.952609506, 0.873186099, 1.082074615, 0.809910114, 0.824646338, 0.973452959, None, None, None, None],
                         e.observations[0].replicates[0].data)
        self.assertEqual([1.223461476, 1.089638674, 1.332677901, 1.133103722, 1.184216135, 0.861974228, 1.082077167, 0, 0.988510339, 0.998889796, 1.333564486, 0.019336919, 0.973539682, 0.96205557, 0.997789496, 0.956335641, 0.97697387, 0.910579888, 1.063434576, None, None, None, None],
                         e.observations[0].replicates[1].data)
        self.assertEqual([1.382014794, 1.154337483, 1.613522166, 1.662006385, 0.891598604, 0.849417672, 0.939556517, 0, 0.85394292, 0.954599629, 1.17901024, 0.023701855, 0.94305168, 1.056172147, 0.971461537, 1.078346196, 1.045215312, 1.006887979, 1.028893656, None, None, None, None],
                         e.observations[0].replicates[2].data)
        self.assertEqual([1.142300549, 1.125248811, 1.73949877, 1.356031973, 0.482802007, 1.347463534, 1.109138132, 0.151945026, 1.08324742, 1.031550305, 0.795768087, 0.030868614, 1.208833467, 1.004602858, 0.985208043, 1.011382818, 0.987160238, 1.252695842, 0.7810663, None, None, None, None],
                         e.observations[0].replicates[3].data)
        self.assertEqual([1.206641002, 1.039743604, 1.268059924, 1.354971326, 1.092095645, 0.961372045, 0.895650938, 0.279433321, 1.076357972, 0.998210257, 0.708824051, 0.015790474, 0.970989445, 1.048684173, 0.983254189, 1.05785957, 1.169146123, 1.032358173, 1.122494638, None, None, None, None],
                         e.observations[0].replicates[4].data)
        self.assertEqual([1.166916656, 1.315466955, 1.463973383, 1.520868297, 1.476459957, 0.975763723, 0.894943535, 0.171876633, 1.141593885, 0.970239438, 0.725205931, 0.033237038, 0.981414714, 0.975875745, 1.189100636, 0.814001159, 1.011594343, 0.97283178, 1.030657871, None, None, None, None],
                         e.observations[0].replicates[5].data)
if __name__ == "__main__":
    unittest.main()