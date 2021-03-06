from amon.system.collector import system_info_collector, process_info_collector
from nose.tools import eq_

class TestSystemCheck(object):

	def __init__(self):
		pass

	def test_memory(self):
		memory_dict = system_info_collector.get_memory_info()
		
		assert 'memfree' in memory_dict
		assert 'memtotal' in memory_dict
		assert 'swapfree' in memory_dict
		assert 'swaptotal' in memory_dict

		for v in memory_dict.values():
			assert isinstance(v, int)


	def test_disk(self):
		disk = system_info_collector.get_disk_usage()

		for k in disk:
			_dict = disk[k]

			assert 'used' in _dict
			assert 'percent' in _dict
			assert 'free' in _dict
			assert 'volume' in _dict
			assert 'total' in _dict


	def test_cpu(self):
		cpu = system_info_collector.get_cpu_utilization()
		
		assert 'idle' in cpu
		assert 'user' in cpu
		assert 'system' in cpu


		for v in cpu.values():
			assert isinstance(v, int)


	def test_loadavg(self):
		loadavg = system_info_collector.get_load_average()

		assert 'minute' in loadavg
		assert 'five_minutes' in loadavg
		assert 'fifteen_minutes' in loadavg
		assert 'scheduled_processes' in loadavg

		for v in loadavg.values():
			assert isinstance(v, str)

class TestProcessCheck(object):

	def __init__(self):
		self.process_checks = ('cron',) # something that's available in most linux distributions


	def test_process(self):
		for process in self.process_checks:
			process_dict = process_info_collector.check_process(process)
			
			assert 'memory' in process_dict
			assert 'cpu' in process_dict
			
