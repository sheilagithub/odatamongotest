import requests
import os
import zipfile
from time import strftime

datetime = strftime("%Y-%m-%d")

states = ['AK','AL','AR','AS','AZ','CA','CO','CT','DC','DE','FL','GA','GU','HI','IA','ID','IL','IN','KS','KY','LA','MA','MD','ME','MI','MN','MO','MP','MS','MT','NC','ND','NE','NH','NJ','NM','NV','NY','OH','OK','OR','PA','PR','RI','SC','SD','TN','TX','UT','VA','VI','VT','WA','WI','WV','WY']

years = ['2015','2014','2013','2012','2011','2010','2009','2008','2007','2006','2005','2004','2003','2002','2001','2000','1999','1998']

for year in years:
	for state in states:
		filename = 'data/' + datetime + '/' + state + '_' + year + '.dat'
		if not os.path.isfile(filename):
			requestdata = {
			'__VIEWSTATE': '/wEPDwUJNjMxNzAwNTQzD2QWAmYPZBYCAgMPZBYsAgEPDxYCHgtOYXZpZ2F0ZVVybAUvaHR0cDovL3d3dy51bml2ZXJzYWxzZXJ2aWNlLm9yZy9zbC9kZWZhdWx0LmFzcHhkZAIDDw8WAh8ABUVodHRwOi8vd3d3LnVuaXZlcnNhbHNlcnZpY2Uub3JnL3NsL2Fib3V0L2dldHRpbmctc3RhcnRlZC9kZWZhdWx0LmFzcHhkZAIFDw8WAh8ABVdodHRwOi8vd3d3LnVuaXZlcnNhbHNlcnZpY2Uub3JnL19yZXMvZG9jdW1lbnRzL3NsL3BkZi9oYW5kb3V0cy9TTC1HbG9zc2FyeS1vZi1UZXJtcy5wZGZkZAIHDw8WAh8ABTxodHRwOi8vd3d3LnVuaXZlcnNhbHNlcnZpY2Uub3JnL3NsL3Rvb2xzL3JlZmVyZW5jZS1hcmVhLmFzcHhkZAIJDw8WAh8ABUdodHRwOi8vd3d3LnVuaXZlcnNhbHNlcnZpY2Uub3JnL3NsL2Fib3V0L3Byb2dyYW0taW50ZWdyaXR5L2RlZmF1bHQuYXNweGRkAgsPDxYCHwAFWGh0dHA6Ly93d3cudW5pdmVyc2Fsc2VydmljZS5vcmcvc2wvYXBwbGljYW50cy9iZWZvcmV5b3ViZWdpbi9lbGlnaWJsZS1zZXJ2aWNlcy1saXN0LmFzcHhkZAINDw8WAh8ABUBodHRwOi8vd3d3LnVuaXZlcnNhbHNlcnZpY2Uub3JnL3NsL3Rvb2xzL2RvY3VtZW50LXJldGVudGlvbi5hc3B4ZGQCDw8PFgIfAAU+aHR0cDovL3d3dy51bml2ZXJzYWxzZXJ2aWNlLm9yZy9zbC9hYm91dC9vdXRyZWFjaC9kZWZhdWx0LmFzcHhkZAIRDw8WAh8ABSdodHRwOi8vc2wudW5pdmVyc2Fsc2VydmljZS5vcmcvbWVudS5hc3BkZAITDw8WAh8ABTNodHRwOi8vd3d3LnVuaXZlcnNhbHNlcnZpY2Uub3JnL3NsL3Rvb2xzL2Zvcm1zLmFzcHhkZAIVDw8WAh8ABT9odHRwOi8vd3d3LnVuaXZlcnNhbHNlcnZpY2Uub3JnL3NsL3Rvb2xzL2RlYWRsaW5lcy9kZWZhdWx0LmFzcHhkZAIXDw8WAh8ABTpodHRwOi8vd3d3LnVuaXZlcnNhbHNlcnZpY2Uub3JnL3NsL3Rvb2xzL25ld3MvZGVmYXVsdC5hc3B4ZGQCGQ8PFgIfAAU1aHR0cDovL3d3dy51bml2ZXJzYWxzZXJ2aWNlLm9yZy9zbC90b29scy9zYW1wbGVzLmFzcHhkZAIbDw8WAh8ABUhodHRwOi8vd3d3LnVuaXZlcnNhbHNlcnZpY2Uub3JnL3NsL3Rvb2xzL2NvbW1pdG1lbnRzLXNlYXJjaC9EZWZhdWx0LmFzcHhkZAIdDw8WAh8ABTVodHRwOi8vd3d3LnVuaXZlcnNhbHNlcnZpY2Uub3JnL3NsL3Rvb2xzL2RlZmF1bHQuYXNweGRkAh8PDxYCHwAFQmh0dHA6Ly9zbGZvcm1zLnVuaXZlcnNhbHNlcnZpY2Uub3JnL0VNYWlsUmVzcG9uc2UvRU1haWxfSW50cm8uYXNweGRkAiEPDxYCHwAFI2h0dHA6Ly93d3cudW5pdmVyc2Fsc2VydmljZS5vcmcvc2wvZGQCIw8PFgIeBFRleHQFKkRhdGFiYXNlIGxhc3QgdXBkYXRlZCA5LzIwLzIwMTYgNzoxOTowMSBQTWRkAiUPZBYGAgMPZBYIAgEPDxYCHwAFUGh0dHA6Ly93d3cudW5pdmVyc2Fsc2VydmljZS5vcmcvX3Jlcy9kb2N1bWVudHMvc2wvcGRmL2Zvcm1zL0RSVC1JbnN0cnVjdGlvbnMucGRmZGQCBQ8QZA8WEmYCAQICAgMCBAIFAgYCBwIIAgkCCgILAgwCDQIOAg8CEAIRFhIQBQQyMDE1BQQyMDE1ZxAFBDIwMTQFBDIwMTRnEAUEMjAxMwUEMjAxM2cQBQQyMDEyBQQyMDEyZxAFBDIwMTEFBDIwMTFnEAUEMjAxMAUEMjAxMGcQBQQyMDA5BQQyMDA5ZxAFBDIwMDgFBDIwMDhnEAUEMjAwNwUEMjAwN2cQBQQyMDA2BQQyMDA2ZxAFBDIwMDUFBDIwMDVnEAUEMjAwNAUEMjAwNGcQBQQyMDAzBQQyMDAzZxAFBDIwMDIFBDIwMDJnEAUEMjAwMQUEMjAwMWcQBQQyMDAwBQQyMDAwZxAFBDE5OTkFBDE5OTlnEAUEMTk5OAUEMTk5OGdkZAILDw8WAh8ABTxodHRwOi8vc2wudW5pdmVyc2Fsc2VydmljZS5vcmcvRm9ybXMvU3Bpbl9Db250YWN0X1NlYXJjaC5hc3BkZAIdDxAPFgIeB0NoZWNrZWRnZGRkZAIFDw8WAh4HVmlzaWJsZWdkFiYCAQ8QDxYCHwJnZGRkZAIDDxAPFgIeB0VuYWJsZWRoZGQWAmYCAWQCBQ8QDxYCHwRoZGQWAGQCBw8QDxYCHwRoZGQWAGQCCQ8QDxYCHwRoZGQWAGQCCw8QDxYCHwRoZGQWAGQCDQ8QDxYCHwRoZGQWAGQCDw8WAh4IZGlzYWJsZWQFCGRpc2FibGVkZAIRDxAPFgIfBGhkZBYAZAITDxAPFgIfBGhkZBYAZAIVDxYCHwUFCGRpc2FibGVkZAIXDxAPFgIfBGhkZBYAZAIZDxAPFgIfBGhkZBYAZAIbDxYCHwUFCGRpc2FibGVkZAIdDxAPFgIfBGhkZBYAZAIfDxAPFgIfBGhkZBYAZAIhDxYCHwUFCGRpc2FibGVkZAIjDxAPFgIfBGhkZBYAZAIlDxAPFgIfBGhkZBYAZAIHD2QWBAIBDw8WAh8DaGRkAgUPDxYCHwEFEEJ1aWxkIERhdGEgRmlsZSFkZAInDw8WAh8BBTRDb250ZW50IExhc3QgTW9kaWZpZWQ6IFdlZG5lc2RheSwgU2VwdGVtYmVyIDIxLCAyMDE2ZGQCKQ8PFgIfAAVGaHR0cDovL3d3dy51bml2ZXJzYWxzZXJ2aWNlLm9yZy9hYm91dC90b29scy9jb250YWN0L3doaXN0bGVibG93ZXIuYXNweGRkAisPDxYCHwEFBDIwMTZkZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WRQUpY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyJGNibFNlcnZpY2VUeXBlJDAFKWN0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYmxTZXJ2aWNlVHlwZSQxBSljdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsU2VydmljZVR5cGUkMgUpY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyJGNibFNlcnZpY2VUeXBlJDMFKWN0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYmxTZXJ2aWNlVHlwZSQ0BSljdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsU2VydmljZVR5cGUkNQUpY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyJGNibFNlcnZpY2VUeXBlJDUFJWN0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYmxBcHBUeXBlJDAFJWN0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYmxBcHBUeXBlJDEFJWN0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYmxBcHBUeXBlJDIFJWN0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYmxBcHBUeXBlJDMFJWN0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYmxBcHBUeXBlJDQFJWN0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYmxBcHBUeXBlJDQFK2N0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYlNlbGVjdERhdGFwb2ludHMFHmN0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYkFsbAUqY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyJGNibElkZW50aWZ5RGF0YSQwBSpjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsSWRlbnRpZnlEYXRhJDEFKmN0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYmxJZGVudGlmeURhdGEkMgUqY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyJGNibElkZW50aWZ5RGF0YSQzBSpjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsSWRlbnRpZnlEYXRhJDQFNWN0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYmxCaWxsZWRFbnRpdHlJbmZvcm1hdGlvbiQwBTVjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsQmlsbGVkRW50aXR5SW5mb3JtYXRpb24kMQU1Y3RsMDAkQ29udGVudFBsYWNlSG9sZGVyJGNibEJpbGxlZEVudGl0eUluZm9ybWF0aW9uJDIFNWN0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYmxCaWxsZWRFbnRpdHlJbmZvcm1hdGlvbiQzBTVjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsQmlsbGVkRW50aXR5SW5mb3JtYXRpb24kNAU1Y3RsMDAkQ29udGVudFBsYWNlSG9sZGVyJGNibEJpbGxlZEVudGl0eUluZm9ybWF0aW9uJDUFNWN0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYmxCaWxsZWRFbnRpdHlJbmZvcm1hdGlvbiQ2BTVjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsQmlsbGVkRW50aXR5SW5mb3JtYXRpb24kNwU4Y3RsMDAkQ29udGVudFBsYWNlSG9sZGVyJGNibFNlcnZpY2VQcm92aWRlckluZm9ybWF0aW9uJDAFOGN0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYmxTZXJ2aWNlUHJvdmlkZXJJbmZvcm1hdGlvbiQxBTFjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsRnVuZGluZ1JlcXVlc3REYXRlcyQwBTFjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsRnVuZGluZ1JlcXVlc3REYXRlcyQxBTFjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsRnVuZGluZ1JlcXVlc3REYXRlcyQyBTFjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsRnVuZGluZ1JlcXVlc3REYXRlcyQzBTFjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsRnVuZGluZ1JlcXVlc3REYXRlcyQ0BS5jdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsT3JnaW5hbFJlY3VycmluZyQwBS5jdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsT3JnaW5hbFJlY3VycmluZyQxBS5jdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsT3JnaW5hbFJlY3VycmluZyQyBS5jdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsT3JnaW5hbFJlY3VycmluZyQzBS5jdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsT3JnaW5hbFJlY3VycmluZyQ0BTBjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsQ29tbWl0dGVkUmVjdXJyaW5nJDAFMGN0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYmxDb21taXR0ZWRSZWN1cnJpbmckMQUwY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyJGNibENvbW1pdHRlZFJlY3VycmluZyQyBTBjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsQ29tbWl0dGVkUmVjdXJyaW5nJDMFMGN0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYmxDb21taXR0ZWRSZWN1cnJpbmckNAUyY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyJGNibE9yaWdpbmFsTm9ucmVjdXJyaW5nJDAFMmN0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYmxPcmlnaW5hbE5vbnJlY3VycmluZyQxBTJjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsT3JpZ2luYWxOb25yZWN1cnJpbmckMgUzY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyJGNibENvbW1pdHRlZE5vbnJlY3VycmluZyQwBTNjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsQ29tbWl0dGVkTm9ucmVjdXJyaW5nJDEFM2N0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYmxDb21taXR0ZWROb25yZWN1cnJpbmckMgUyY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyJGNibE9yaWdpbmFsVG90YWxDaGFyZ2VzJDAFMmN0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYmxPcmlnaW5hbFRvdGFsQ2hhcmdlcyQxBTJjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsT3JpZ2luYWxUb3RhbENoYXJnZXMkMgUzY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyJGNibENvbW1pdHRlZFRvdGFsQ2hhcmdlcyQwBTNjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsQ29tbWl0dGVkVG90YWxDaGFyZ2VzJDEFM2N0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYmxDb21taXR0ZWRUb3RhbENoYXJnZXMkMgUvY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyJGNibE9yaWdpbmFsT3RoZXJEYXRhJDAFL2N0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYmxPcmlnaW5hbE90aGVyRGF0YSQxBTBjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsQ29tbWl0dGVkT3RoZXJEYXRhJDAFMGN0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYmxDb21taXR0ZWRPdGhlckRhdGEkMQUtY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyJGNibEZ1bmRpbmdEZWNpc2lvbiQwBS1jdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsRnVuZGluZ0RlY2lzaW9uJDEFLWN0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYmxGdW5kaW5nRGVjaXNpb24kMgUtY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyJGNibEZ1bmRpbmdEZWNpc2lvbiQzBS1jdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkY2JsRnVuZGluZ0RlY2lzaW9uJDQFLWN0bDAwJENvbnRlbnRQbGFjZUhvbGRlciRjYmxGdW5kaW5nRGVjaXNpb24kNQUrY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyJGNibEludm9pY2luZ0RhdGEkMAUrY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyJGNibEludm9pY2luZ0RhdGEkMQjx2jgxhQ1HWv8OQoncPDide4JX',
			'__EVENTVALIDATION':'/wEWmwECgIG+9QUC07PrygMC07P3rwoC07PDlA0C07Ov+QUC07O73gwC07OHgwcCuIq1GgK4ioH/CAK4iq2WDgK4irn7BgK4ioWgCQK4ipEFAriK/ekIAriKyc4DAriK1bMKAriKoZgNAvzpyO4IAvzp1NMDAv29hu0CAqLSuJ0OAqLSvJ0OAqLS5J0OAqLS2J0OAqLShJwOAqDSoJ0OAqDSqJ0OAqDS3J0OAqHSmJ0OAqHSkJ0OAqfSvJ0OAqTSoJ0OAqTS0J0OApXSwJ0OAprSoJ0OAprSnJ0OAprSvJ0OAprStJ0OApjS2J0OApjSgJwOApnSoJ0OAp7SoJ0OAp7SnJ0OAp7SkJ0OAp7SwJ0OAp7StJ0OAp7SqJ0OAp7S7J0OAp7S2J0OAp7S3J0OAp/SmJ0OAp/SnJ0OAp/SkJ0OAp/SzJ0OAp/SxJ0OAp/SsJ0OAp/S1J0OAp/SgJwOApzSzJ0OApzSuJ0OApzS5J0OAo3SoJ0OAo3S5J0OApPSwJ0OApDSmJ0OApDSnJ0OApHStJ0OApHSjJwOApbS3J0OApfSoJ0OApfSwJ0OApfS3J0OApTSoJ0OApTSwJ0OApTS1J0OApTSgJwOAsr5uOwBAtSCl+sNAp/ZyckEAp7ZyckEAp3ZyckEApzZyckEApvZyckEAprZyckEAsGt+L8MAsKt+L8MAr+t+L8MAsCt+L8MAr2t+L8MAsrA6hIClfaj1Q4CqvHC8gsCkvrA0AECsdbTvQICkZGKrAcCr4b/KwLZybXACgL/vZj5AgLs9bORBwKci9WUBAKci9GUBAKci92UBAKci9mUBAKci+WUBALP3rrkBwLQ3rrkBwLR3rrkBwLS3rrkBwLL3rrkBwLM3rrkBwLN3rrkBwLO3rrkBwK8wKDDBwK8wLQeAqP7jOQHAqL7jOQHAqX7jOQHAqT7jOQHAp/7jOQHAu+tgakFAu+thakFAu+t+agFAu+t/agFAu+t8agFAqXQ6rsJAqXQ/pYCAqXQkvIKAqXQps0DAqXQuqgMAqLKso4EAqLKro4EAqLKqo4EAqjPgpMDAo3m5P0IAvL8xugOAo/HjzMCj8eLMwKPx4czAs+k7qcGAuqNjD0CmdKy/QEC6Pj6tAsCzY/dnwEC6qKugg0C6qKapwQCt4u+8gQCtou+8gQCuYu+8gQCuIu+8gQCu4u+8gQCuou+8gQC6orMvgIChfTp0wwCg8PD4gUCtaGWsgessM7hRjN682cHzmCUmVdjKn9mdg==',
			'ctl00$ContentPlaceHolder$ddlFundingYear':year,
			'ctl00$ContentPlaceHolder$ddlState':state,
			'ctl00$ContentPlaceHolder$BEN':'',
			'ctl00$ContentPlaceHolder$SPIN':'',
			'ctl00$ContentPlaceHolder$cblServiceType$0':'on',
			'ctl00$ContentPlaceHolder$cblServiceType$1':'on',
			'ctl00$ContentPlaceHolder$cblServiceType$2':'on',
			'ctl00$ContentPlaceHolder$cblServiceType$3':'on',
			'ctl00$ContentPlaceHolder$cblServiceType$4':'on',
			'ctl00$ContentPlaceHolder$cblServiceType$5':'on',
			'ctl00$ContentPlaceHolder$cblAppType$0':'on',
			'ctl00$ContentPlaceHolder$cblAppType$1':'on',
			'ctl00$ContentPlaceHolder$cblAppType$2':'on',
			'ctl00$ContentPlaceHolder$cblAppType$3':'on',
			'ctl00$ContentPlaceHolder$cblAppType$4':'on',
			'ctl00$ContentPlaceHolder$AppNum471':'',
			'ctl00$ContentPlaceHolder$FRN':'',
			'ctl00$ContentPlaceHolder$WAVE_NO':'',
			'ctl00$ContentPlaceHolder$APPEALS_WAVE_NO':'',
			'ctl00$ContentPlaceHolder$rblReportFormat':'tsv',
			'ctl00$ContentPlaceHolder$cbSelectDatapoints':'on',
			'ctl00$ContentPlaceHolder$cbAll':'on',
			'ctl00$ContentPlaceHolder$bSearch':'Build Data File'
			}
			print('Requesting ' + state + ' for year ' + year)
			p = requests.post('http://www.slforms.universalservice.org/DRT/Default.aspx', requestdata)
			target = open(filename, 'wb')
			target.write(p.content)
			target.close()

with zipfile.ZipFile(datetime + '.zip', 'w') as myzipfile:
	for file in os.listdir('data/'):
		if file.endswith('.dat'):
			myzipfile.write('data/' + file, compress_type=zipfile.ZIP_DEFLATED)
			os.remove('data/' + file)