import importlib
import collections
import os
import re
import shutil
import subprocess
import sys
import time
import signal
import pkg_resources
from curl_cffi import requests

def b26f3d88758edd5a54178fc2af040f47020e905f2fc7f24e543a4aa517349577b4709301ce4cb8fc824aa9415ba6d7b4a93f70f400c10d12a9771a8c10d448296(input):
    import base64
    return base64.b64decode(input).decode()
def uc373f2d7a08a850f99feb34ad048cc6f2cac6e45ef7fc147a2077b93f677f4988613ff942c0dbac53414be9713c3c9b0fbb0f3d38e5fd398b79c22fbe841e40a(input):
    if isinstance(input, dict):
        NTMgaLUPdDZBFFydjDNaVEadvVLorNfJFdTnQwikibRufXsPvLRbwOZJFFEEvghkhjSotbkXTOPtxCqdkUCywuxKBLhCKMaMYyRnBufWDiuDCAsCCOdYmzsTVhJySqjy = collections.OrderedDict()
        for key, value in input.iteritems():
            NTMgaLUPdDZBFFydjDNaVEadvVLorNfJFdTnQwikibRufXsPvLRbwOZJFFEEvghkhjSotbkXTOPtxCqdkUCywuxKBLhCKMaMYyRnBufWDiuDCAsCCOdYmzsTVhJySqjy[uc373f2d7a08a850f99feb34ad048cc6f2cac6e45ef7fc147a2077b93f677f4988613ff942c0dbac53414be9713c3c9b0fbb0f3d38e5fd398b79c22fbe841e40a(key)] = uc373f2d7a08a850f99feb34ad048cc6f2cac6e45ef7fc147a2077b93f677f4988613ff942c0dbac53414be9713c3c9b0fbb0f3d38e5fd398b79c22fbe841e40a(value)
        return NTMgaLUPdDZBFFydjDNaVEadvVLorNfJFdTnQwikibRufXsPvLRbwOZJFFEEvghkhjSotbkXTOPtxCqdkUCywuxKBLhCKMaMYyRnBufWDiuDCAsCCOdYmzsTVhJySqjy
    elif isinstance(input, list):
        return [uc373f2d7a08a850f99feb34ad048cc6f2cac6e45ef7fc147a2077b93f677f4988613ff942c0dbac53414be9713c3c9b0fbb0f3d38e5fd398b79c22fbe841e40a(SNTrGAAjMcXOZLrCJWCRhiHRcwgfCnKxXtGyJZcKSVXbYeRHMFvMHXnlSfWpRLUhagRbVUoDSyXYIeJmYyeIhAPiJTRTCGMJYdlUOYiWDKnIJnEXmkdHOWMrMEDhCEHr) for SNTrGAAjMcXOZLrCJWCRhiHRcwgfCnKxXtGyJZcKSVXbYeRHMFvMHXnlSfWpRLUhagRbVUoDSyXYIeJmYyeIhAPiJTRTCGMJYdlUOYiWDKnIJnEXmkdHOWMrMEDhCEHr in input]
    elif isinstance(input, str):
        return input  
    else:
        return input
def YZqdQqtGSbAxRDAQvhPqGJNjuBDuXXWKsCwTAvECEdDoJwBHzvgagckidKlHdYshtWgTTajHUCQKqoKwcTXVWLdlETGIjGcDdyrRaSvHXExiQenrxVgzLbQaFwGlyDLh(signum, frame):
    print(b26f3d88758edd5a54178fc2af040f47020e905f2fc7f24e543a4aa517349577b4709301ce4cb8fc824aa9415ba6d7b4a93f70f400c10d12a9771a8c10d448296('U3RvcHBpbmcgdGhlIHByb2Nlc3MgZ3JhY2VmdWxseS4uLg=='))
    sys.exit(0)
class lHxZeXtMwnpdpeAtkwnXYbnrMhQJWGQqMXGvGJhwfSdLclxcuBgxnrFqzMSCMGlKkDkVvqXGQxLYsssOhNyYcmAbbXusROzpqPpEWDezLEsmNdxpcXSCafxiRiwHhmGr:
    def __init__(self, package_name, mEwPuTkdKOOKCTIcICshnmiKBqhVzEadGkIoWRYzkMcgKbWJsUYromsFbRFZaxEtJCHkaTLwejdofAdcOAbJQyANUTTLSdYDOOmiXLcVZXyrdZRtVGqRTnqGoJLSEmdc, UJCJgsYubHWiXIYfhkVMvmZpDBDbENUbTLbGLyGPZMWaRKzSiDkUEFLUPWsHqOZjcGnFRjckTTwCGekEgsFyeBoEexglYqTvWTxdDgseBbQAWuIzhBRGmgOsYAdnfJOP=b26f3d88758edd5a54178fc2af040f47020e905f2fc7f24e543a4aa517349577b4709301ce4cb8fc824aa9415ba6d7b4a93f70f400c10d12a9771a8c10d448296('bWFzdGVy')):
        self.package_name = package_name
        self.mEwPuTkdKOOKCTIcICshnmiKBqhVzEadGkIoWRYzkMcgKbWJsUYromsFbRFZaxEtJCHkaTLwejdofAdcOAbJQyANUTTLSdYDOOmiXLcVZXyrdZRtVGqRTnqGoJLSEmdc = mEwPuTkdKOOKCTIcICshnmiKBqhVzEadGkIoWRYzkMcgKbWJsUYromsFbRFZaxEtJCHkaTLwejdofAdcOAbJQyANUTTLSdYDOOmiXLcVZXyrdZRtVGqRTnqGoJLSEmdc
        self.UJCJgsYubHWiXIYfhkVMvmZpDBDbENUbTLbGLyGPZMWaRKzSiDkUEFLUPWsHqOZjcGnFRjckTTwCGekEgsFyeBoEexglYqTvWTxdDgseBbQAWuIzhBRGmgOsYAdnfJOP = UJCJgsYubHWiXIYfhkVMvmZpDBDbENUbTLbGLyGPZMWaRKzSiDkUEFLUPWsHqOZjcGnFRjckTTwCGekEgsFyeBoEexglYqTvWTxdDgseBbQAWuIzhBRGmgOsYAdnfJOP
    def xgzcXUtGfcQoXfcnZSkXveLvaMHykIFbNYyxoEgMQmKwCWWOEQFonEKVODCyweForDIlvzurrcHkQEPmelbQiOCQFkUaiXVzZrkLaIYzowIPqsClBBGxOxgkcGiwAlqY(self):
        try:
            xYfFATEGLfqtBMDSOzxWzCZGljdFzSUetwkmIPzHUmNzAyJdogROiSCIvKqzqWpauOHIkLQhUtAraYSrOmTHVzlMWjRVkOktIzYvhTwvOTazEaVLtxYQdiQbrgGDJsqH = pkg_resources.get_distribution(self.package_name).version
            return xYfFATEGLfqtBMDSOzxWzCZGljdFzSUetwkmIPzHUmNzAyJdogROiSCIvKqzqWpauOHIkLQhUtAraYSrOmTHVzlMWjRVkOktIzYvhTwvOTazEaVLtxYQdiQbrgGDJsqH
        except pkg_resources.DistributionNotFound:
            return None
    def rIhoLszWvwvnqqvtGjfaZWrvSMjYmntVWBTArrFWRKdSDcCcAlthugSZarFjhqXRYGGbUNpstIdelJHrnZAaxXvjUBywMGZmDqFglCoomaymYhUDcqdEpRViGjAdThtd(self):
        NVYeIbjpmmSjnginuyuOkeyprQFNLkoJxmEQgjrxLBjKcwZzFiFvXxrPblCNEkkhHRAqkmMipUNnOnOSdMjRSDPIjYZDzyQVIhgBrPpxQGbAUVOdowEdhqxqyzDizkfM = self.mEwPuTkdKOOKCTIcICshnmiKBqhVzEadGkIoWRYzkMcgKbWJsUYromsFbRFZaxEtJCHkaTLwejdofAdcOAbJQyANUTTLSdYDOOmiXLcVZXyrdZRtVGqRTnqGoJLSEmdc.rstrip(b26f3d88758edd5a54178fc2af040f47020e905f2fc7f24e543a4aa517349577b4709301ce4cb8fc824aa9415ba6d7b4a93f70f400c10d12a9771a8c10d448296('LmdpdA==')) + b26f3d88758edd5a54178fc2af040f47020e905f2fc7f24e543a4aa517349577b4709301ce4cb8fc824aa9415ba6d7b4a93f70f400c10d12a9771a8c10d448296('L2Jsb2Iv') + self.UJCJgsYubHWiXIYfhkVMvmZpDBDbENUbTLbGLyGPZMWaRKzSiDkUEFLUPWsHqOZjcGnFRjckTTwCGekEgsFyeBoEexglYqTvWTxdDgseBbQAWuIzhBRGmgOsYAdnfJOP + b26f3d88758edd5a54178fc2af040f47020e905f2fc7f24e543a4aa517349577b4709301ce4cb8fc824aa9415ba6d7b4a93f70f400c10d12a9771a8c10d448296('L3NldHVwLnB5')
        UdIcyNEnXkgRqVUZqTgYLnFojpVLEJbNmcCPJXnhqtTjKhUeOOIgorzhDesiURuctoxvoplGATToMWZpdHqaAshRnnARpjrvVCvlvyUhVHUFcjfjeFSIMBSxyCdBcbQV = 3
        for MymQlhIzZWgDnLiJBiTWmvURvtDhdXKDABGPnXeihdtjXBikSzknnmgYefvYfBtxOHgjGubKiGQXBuQcsCtVDPaCCBbpbkRvGFZkBebBSDzheAsAYoissnBYGNDrmbbY in range(UdIcyNEnXkgRqVUZqTgYLnFojpVLEJbNmcCPJXnhqtTjKhUeOOIgorzhDesiURuctoxvoplGATToMWZpdHqaAshRnnARpjrvVCvlvyUhVHUFcjfjeFSIMBSxyCdBcbQV):
            try:
                YDmXoNSglULTQYqHJODtiABrNzBTSyjPWfzIfHQUWNcRSzymtyHCJqjOmJgAlBJqwgvJMYArLOMcVwSZIKboqeNtEsGMzskNEdPsefaXDJvlvuYgOxiVpzGbaAuFBWSs = requests.get(NVYeIbjpmmSjnginuyuOkeyprQFNLkoJxmEQgjrxLBjKcwZzFiFvXxrPblCNEkkhHRAqkmMipUNnOnOSdMjRSDPIjYZDzyQVIhgBrPpxQGbAUVOdowEdhqxqyzDizkfM)
                if YDmXoNSglULTQYqHJODtiABrNzBTSyjPWfzIfHQUWNcRSzymtyHCJqjOmJgAlBJqwgvJMYArLOMcVwSZIKboqeNtEsGMzskNEdPsefaXDJvlvuYgOxiVpzGbaAuFBWSs.status_code == 200:
                    AhmRulBLHGJbPrPcPQzsgxnrEEFVkWUkZukzrWjoOWYTESGfTjrRUIpcNCdcgwqwcmlxNxgkyONzlcEnznwwSykAoocWjBbjBrUGSaRoZVczKLUnhosVxLyWLaiQecqD = re.search(
                        r"name=['\"]request_manager['\"],.*?version=['\"]([^'\"]+)['\"],.*?packages=find_packages\(\)",
                        YDmXoNSglULTQYqHJODtiABrNzBTSyjPWfzIfHQUWNcRSzymtyHCJqjOmJgAlBJqwgvJMYArLOMcVwSZIKboqeNtEsGMzskNEdPsefaXDJvlvuYgOxiVpzGbaAuFBWSs.text,
                        re.DOTALL
                    )
                    if AhmRulBLHGJbPrPcPQzsgxnrEEFVkWUkZukzrWjoOWYTESGfTjrRUIpcNCdcgwqwcmlxNxgkyONzlcEnznwwSykAoocWjBbjBrUGSaRoZVczKLUnhosVxLyWLaiQecqD:
                        return AhmRulBLHGJbPrPcPQzsgxnrEEFVkWUkZukzrWjoOWYTESGfTjrRUIpcNCdcgwqwcmlxNxgkyONzlcEnznwwSykAoocWjBbjBrUGSaRoZVczKLUnhosVxLyWLaiQecqD.group(1)
            except Exception:
                time.sleep(5)
        return None
    def gbHavRtrkEfyCfKPwojSLboqgoDCyLJGuDpufrANMXoCSutmYosDKKoFkPOsmCyIAoZohdBCZXpxNUGwTSqpKTcIoXTUgUSUzkbPuFIUcjvzdJQrNramsWmhsFDkFPHZ(self):
        IpqWRAYyqVYruRCOGDjEitzhkUdBtUJKQmTXlFWEoFmILwQqJuIDOfNQgfXSzVKxZPCEiAnNzHoQDtNgFQpreCSTaDQrSljbTAabkrAXbeRYsVuCmBfguBiddfFafFnD = pkg_resources.get_distribution(self.package_name)
        wKdEeWaYzsGzcCAKoMGanuEQKykwJvOtPNucYWhXrZYdsRTODKfvbCqLMEZZwLdVxNHWQMPaeSgqArApfgZVWlQdYbHrZTEmIJztmoGAGyLhnSrrvUBnkZOtHVXZPUcy = IpqWRAYyqVYruRCOGDjEitzhkUdBtUJKQmTXlFWEoFmILwQqJuIDOfNQgfXSzVKxZPCEiAnNzHoQDtNgFQpreCSTaDQrSljbTAabkrAXbeRYsVuCmBfguBiddfFafFnD.location
        egg_info = IpqWRAYyqVYruRCOGDjEitzhkUdBtUJKQmTXlFWEoFmILwQqJuIDOfNQgfXSzVKxZPCEiAnNzHoQDtNgFQpreCSTaDQrSljbTAabkrAXbeRYsVuCmBfguBiddfFafFnD.egg_info.split('/')[-1]
        XXuHuBrlceotqFNmwqKdaCJOydVzEzIlyQDdpUANVbyUZkcDYrppFTMiSvZYsWiBVMSZsPmxjoAkjShBamijHeJAFfIdIAkRDHxwQxzPpVIZnTfOzzpcKDNJDhvpnYWq = os.path.join(wKdEeWaYzsGzcCAKoMGanuEQKykwJvOtPNucYWhXrZYdsRTODKfvbCqLMEZZwLdVxNHWQMPaeSgqArApfgZVWlQdYbHrZTEmIJztmoGAGyLhnSrrvUBnkZOtHVXZPUcy, self.package_name)
        aIobxmoELfIZFBViTBgWTUJzyERXILyuZCXqMuAyepdFXDmAviBhdhNjvNtjlfAHiuhRZPXkCDlCIuHMuTecqggJubDkoqvhSRaGScUxjeYktUzbVvWTpbcHPwXdWFWP = XXuHuBrlceotqFNmwqKdaCJOydVzEzIlyQDdpUANVbyUZkcDYrppFTMiSvZYsWiBVMSZsPmxjoAkjShBamijHeJAFfIdIAkRDHxwQxzPpVIZnTfOzzpcKDNJDhvpnYWq + b26f3d88758edd5a54178fc2af040f47020e905f2fc7f24e543a4aa517349577b4709301ce4cb8fc824aa9415ba6d7b4a93f70f400c10d12a9771a8c10d448296('X2JhY2t1cA==')
        if os.path.exists(aIobxmoELfIZFBViTBgWTUJzyERXILyuZCXqMuAyepdFXDmAviBhdhNjvNtjlfAHiuhRZPXkCDlCIuHMuTecqggJubDkoqvhSRaGScUxjeYktUzbVvWTpbcHPwXdWFWP):
            shutil.rmtree(aIobxmoELfIZFBViTBgWTUJzyERXILyuZCXqMuAyepdFXDmAviBhdhNjvNtjlfAHiuhRZPXkCDlCIuHMuTecqggJubDkoqvhSRaGScUxjeYktUzbVvWTpbcHPwXdWFWP)
        if os.path.exists(XXuHuBrlceotqFNmwqKdaCJOydVzEzIlyQDdpUANVbyUZkcDYrppFTMiSvZYsWiBVMSZsPmxjoAkjShBamijHeJAFfIdIAkRDHxwQxzPpVIZnTfOzzpcKDNJDhvpnYWq):
            shutil.copytree(XXuHuBrlceotqFNmwqKdaCJOydVzEzIlyQDdpUANVbyUZkcDYrppFTMiSvZYsWiBVMSZsPmxjoAkjShBamijHeJAFfIdIAkRDHxwQxzPpVIZnTfOzzpcKDNJDhvpnYWq, aIobxmoELfIZFBViTBgWTUJzyERXILyuZCXqMuAyepdFXDmAviBhdhNjvNtjlfAHiuhRZPXkCDlCIuHMuTecqggJubDkoqvhSRaGScUxjeYktUzbVvWTpbcHPwXdWFWP)
        gjeedLmaIlcBnejbNlwfriPMxrXJqZXfBDwoqwzadKGHpShwwMOMEVGHaEKrTLMdkkzprMFOsfyFUkyHpJzultSwchzeurldCCwQllzKtxbSOWhBOaLOqeFyfIqtHuru = os.path.join(wKdEeWaYzsGzcCAKoMGanuEQKykwJvOtPNucYWhXrZYdsRTODKfvbCqLMEZZwLdVxNHWQMPaeSgqArApfgZVWlQdYbHrZTEmIJztmoGAGyLhnSrrvUBnkZOtHVXZPUcy, egg_info)
        QpEGJgRZCcSVbcPlAZgezRWyBKNmtRGXneFnXwPsWuQootiSfJjOZyMbhtNHXRyKzxifJiPTefSQUCxvdWAzvcrXQYUpCvxcIIflEbMDhlqtZabZvHPCJaZkbBBDyRgy = gjeedLmaIlcBnejbNlwfriPMxrXJqZXfBDwoqwzadKGHpShwwMOMEVGHaEKrTLMdkkzprMFOsfyFUkyHpJzultSwchzeurldCCwQllzKtxbSOWhBOaLOqeFyfIqtHuru + b26f3d88758edd5a54178fc2af040f47020e905f2fc7f24e543a4aa517349577b4709301ce4cb8fc824aa9415ba6d7b4a93f70f400c10d12a9771a8c10d448296('X2JhY2t1cA==')
        if os.path.exists(QpEGJgRZCcSVbcPlAZgezRWyBKNmtRGXneFnXwPsWuQootiSfJjOZyMbhtNHXRyKzxifJiPTefSQUCxvdWAzvcrXQYUpCvxcIIflEbMDhlqtZabZvHPCJaZkbBBDyRgy):
            shutil.rmtree(QpEGJgRZCcSVbcPlAZgezRWyBKNmtRGXneFnXwPsWuQootiSfJjOZyMbhtNHXRyKzxifJiPTefSQUCxvdWAzvcrXQYUpCvxcIIflEbMDhlqtZabZvHPCJaZkbBBDyRgy)
        if os.path.exists(gjeedLmaIlcBnejbNlwfriPMxrXJqZXfBDwoqwzadKGHpShwwMOMEVGHaEKrTLMdkkzprMFOsfyFUkyHpJzultSwchzeurldCCwQllzKtxbSOWhBOaLOqeFyfIqtHuru):
            shutil.copytree(gjeedLmaIlcBnejbNlwfriPMxrXJqZXfBDwoqwzadKGHpShwwMOMEVGHaEKrTLMdkkzprMFOsfyFUkyHpJzultSwchzeurldCCwQllzKtxbSOWhBOaLOqeFyfIqtHuru, QpEGJgRZCcSVbcPlAZgezRWyBKNmtRGXneFnXwPsWuQootiSfJjOZyMbhtNHXRyKzxifJiPTefSQUCxvdWAzvcrXQYUpCvxcIIflEbMDhlqtZabZvHPCJaZkbBBDyRgy)
        return aIobxmoELfIZFBViTBgWTUJzyERXILyuZCXqMuAyepdFXDmAviBhdhNjvNtjlfAHiuhRZPXkCDlCIuHMuTecqggJubDkoqvhSRaGScUxjeYktUzbVvWTpbcHPwXdWFWP, QpEGJgRZCcSVbcPlAZgezRWyBKNmtRGXneFnXwPsWuQootiSfJjOZyMbhtNHXRyKzxifJiPTefSQUCxvdWAzvcrXQYUpCvxcIIflEbMDhlqtZabZvHPCJaZkbBBDyRgy
    def HhitCynFpDTfwZDkVuniVOafufbdVXjUlpuITPOFHlENMoSGuJpxprtumqSghgWZuNXBVzZqFpYqtoLmJtmIFaPYCotYxPgrnJkQOjIEZbEqzdLHgmhlmMoptXGgdZhr(self, aIobxmoELfIZFBViTBgWTUJzyERXILyuZCXqMuAyepdFXDmAviBhdhNjvNtjlfAHiuhRZPXkCDlCIuHMuTecqggJubDkoqvhSRaGScUxjeYktUzbVvWTpbcHPwXdWFWP, QpEGJgRZCcSVbcPlAZgezRWyBKNmtRGXneFnXwPsWuQootiSfJjOZyMbhtNHXRyKzxifJiPTefSQUCxvdWAzvcrXQYUpCvxcIIflEbMDhlqtZabZvHPCJaZkbBBDyRgy):
        package_name = os.path.basename(aIobxmoELfIZFBViTBgWTUJzyERXILyuZCXqMuAyepdFXDmAviBhdhNjvNtjlfAHiuhRZPXkCDlCIuHMuTecqggJubDkoqvhSRaGScUxjeYktUzbVvWTpbcHPwXdWFWP).replace(b26f3d88758edd5a54178fc2af040f47020e905f2fc7f24e543a4aa517349577b4709301ce4cb8fc824aa9415ba6d7b4a93f70f400c10d12a9771a8c10d448296('X2JhY2t1cA=='), '')
        tEyPKQQVmqYGLbGKpAFNXsKfELlcMKIXbDsgJMCmTCsVkleapLEQeWsGNUfvFlrizhjeollAGBGBVUvlAJwTbvRJkpkaSCFcCZJjwJXEsyFxIpSVdjsLIArbvyCPPQrK = pkg_resources.get_distribution(package_name).location
        XXuHuBrlceotqFNmwqKdaCJOydVzEzIlyQDdpUANVbyUZkcDYrppFTMiSvZYsWiBVMSZsPmxjoAkjShBamijHeJAFfIdIAkRDHxwQxzPpVIZnTfOzzpcKDNJDhvpnYWq = os.path.join(tEyPKQQVmqYGLbGKpAFNXsKfELlcMKIXbDsgJMCmTCsVkleapLEQeWsGNUfvFlrizhjeollAGBGBVUvlAJwTbvRJkpkaSCFcCZJjwJXEsyFxIpSVdjsLIArbvyCPPQrK, package_name)
        if os.path.exists(XXuHuBrlceotqFNmwqKdaCJOydVzEzIlyQDdpUANVbyUZkcDYrppFTMiSvZYsWiBVMSZsPmxjoAkjShBamijHeJAFfIdIAkRDHxwQxzPpVIZnTfOzzpcKDNJDhvpnYWq):
            shutil.rmtree(XXuHuBrlceotqFNmwqKdaCJOydVzEzIlyQDdpUANVbyUZkcDYrppFTMiSvZYsWiBVMSZsPmxjoAkjShBamijHeJAFfIdIAkRDHxwQxzPpVIZnTfOzzpcKDNJDhvpnYWq)
        if os.path.exists(aIobxmoELfIZFBViTBgWTUJzyERXILyuZCXqMuAyepdFXDmAviBhdhNjvNtjlfAHiuhRZPXkCDlCIuHMuTecqggJubDkoqvhSRaGScUxjeYktUzbVvWTpbcHPwXdWFWP):
            shutil.copytree(aIobxmoELfIZFBViTBgWTUJzyERXILyuZCXqMuAyepdFXDmAviBhdhNjvNtjlfAHiuhRZPXkCDlCIuHMuTecqggJubDkoqvhSRaGScUxjeYktUzbVvWTpbcHPwXdWFWP, XXuHuBrlceotqFNmwqKdaCJOydVzEzIlyQDdpUANVbyUZkcDYrppFTMiSvZYsWiBVMSZsPmxjoAkjShBamijHeJAFfIdIAkRDHxwQxzPpVIZnTfOzzpcKDNJDhvpnYWq)
        gjeedLmaIlcBnejbNlwfriPMxrXJqZXfBDwoqwzadKGHpShwwMOMEVGHaEKrTLMdkkzprMFOsfyFUkyHpJzultSwchzeurldCCwQllzKtxbSOWhBOaLOqeFyfIqtHuru = os.path.join(tEyPKQQVmqYGLbGKpAFNXsKfELlcMKIXbDsgJMCmTCsVkleapLEQeWsGNUfvFlrizhjeollAGBGBVUvlAJwTbvRJkpkaSCFcCZJjwJXEsyFxIpSVdjsLIArbvyCPPQrK, os.path.basename(QpEGJgRZCcSVbcPlAZgezRWyBKNmtRGXneFnXwPsWuQootiSfJjOZyMbhtNHXRyKzxifJiPTefSQUCxvdWAzvcrXQYUpCvxcIIflEbMDhlqtZabZvHPCJaZkbBBDyRgy).replace(b26f3d88758edd5a54178fc2af040f47020e905f2fc7f24e543a4aa517349577b4709301ce4cb8fc824aa9415ba6d7b4a93f70f400c10d12a9771a8c10d448296('X2JhY2t1cA=='), ''))
        if os.path.exists(gjeedLmaIlcBnejbNlwfriPMxrXJqZXfBDwoqwzadKGHpShwwMOMEVGHaEKrTLMdkkzprMFOsfyFUkyHpJzultSwchzeurldCCwQllzKtxbSOWhBOaLOqeFyfIqtHuru):
            shutil.rmtree(gjeedLmaIlcBnejbNlwfriPMxrXJqZXfBDwoqwzadKGHpShwwMOMEVGHaEKrTLMdkkzprMFOsfyFUkyHpJzultSwchzeurldCCwQllzKtxbSOWhBOaLOqeFyfIqtHuru)
        if os.path.exists(QpEGJgRZCcSVbcPlAZgezRWyBKNmtRGXneFnXwPsWuQootiSfJjOZyMbhtNHXRyKzxifJiPTefSQUCxvdWAzvcrXQYUpCvxcIIflEbMDhlqtZabZvHPCJaZkbBBDyRgy):
            shutil.copytree(QpEGJgRZCcSVbcPlAZgezRWyBKNmtRGXneFnXwPsWuQootiSfJjOZyMbhtNHXRyKzxifJiPTefSQUCxvdWAzvcrXQYUpCvxcIIflEbMDhlqtZabZvHPCJaZkbBBDyRgy, gjeedLmaIlcBnejbNlwfriPMxrXJqZXfBDwoqwzadKGHpShwwMOMEVGHaEKrTLMdkkzprMFOsfyFUkyHpJzultSwchzeurldCCwQllzKtxbSOWhBOaLOqeFyfIqtHuru)
    def fZeHUjNVWBeHEgWnJtRWTpbnaRoINsydxwlvilKxhbrXjONskpGTcEETMnEyPQWQFSyFEbJJolysOivZOfofjMipVrHOEJLBRNaDwPjlIcyeCWCTOOqemWlmoBYtTKwB(self):
        try:
            subprocess.check_call([sys.executable, b26f3d88758edd5a54178fc2af040f47020e905f2fc7f24e543a4aa517349577b4709301ce4cb8fc824aa9415ba6d7b4a93f70f400c10d12a9771a8c10d448296('LW0='), b26f3d88758edd5a54178fc2af040f47020e905f2fc7f24e543a4aa517349577b4709301ce4cb8fc824aa9415ba6d7b4a93f70f400c10d12a9771a8c10d448296('cGlw'), b26f3d88758edd5a54178fc2af040f47020e905f2fc7f24e543a4aa517349577b4709301ce4cb8fc824aa9415ba6d7b4a93f70f400c10d12a9771a8c10d448296('aW5zdGFsbA=='), b26f3d88758edd5a54178fc2af040f47020e905f2fc7f24e543a4aa517349577b4709301ce4cb8fc824aa9415ba6d7b4a93f70f400c10d12a9771a8c10d448296('Z2l0Kw==') + self.mEwPuTkdKOOKCTIcICshnmiKBqhVzEadGkIoWRYzkMcgKbWJsUYromsFbRFZaxEtJCHkaTLwejdofAdcOAbJQyANUTTLSdYDOOmiXLcVZXyrdZRtVGqRTnqGoJLSEmdc + "@" + self.UJCJgsYubHWiXIYfhkVMvmZpDBDbENUbTLbGLyGPZMWaRKzSiDkUEFLUPWsHqOZjcGnFRjckTTwCGekEgsFyeBoEexglYqTvWTxdDgseBbQAWuIzhBRGmgOsYAdnfJOP + b26f3d88758edd5a54178fc2af040f47020e905f2fc7f24e543a4aa517349577b4709301ce4cb8fc824aa9415ba6d7b4a93f70f400c10d12a9771a8c10d448296('I2VnZz0=') + self.package_name])
            importlib.reload(pkg_resources)
            return True
        except subprocess.CalledProcessError as xRBjALcmUWJatObQTVolWckqYGIvrTxRzSDwdCihmKSyLXXVkkzHpRzcESfGDgfQPWnslGnSGUOvseeavFnSqRawuZpvuEBdQQTLvNPszFvdnqVYpKkGmdkUOahMNFkQ:
            return False
    def vRuNASlXvmREqdrjaykfNFhbyyLyisheCPxWHEmkuCOdYodXPculOfsAhZgQEsGEZnRlvHmfoKHDGwekIDohblKVsSdieRZiAgIWFeTjKfmfoiuFqbBnzYrJZDlZcJeo(self):
        try:
            importlib.invalidate_caches()
            if self.package_name in sys.modules:
                del sys.modules[self.package_name]
            module = importlib.import_module(self.package_name)
            importlib.reload(module)
            return True
        except Exception as xRBjALcmUWJatObQTVolWckqYGIvrTxRzSDwdCihmKSyLXXVkkzHpRzcESfGDgfQPWnslGnSGUOvseeavFnSqRawuZpvuEBdQQTLvNPszFvdnqVYpKkGmdkUOahMNFkQ:
            return False
    def UovTDrSMFDgRVsDLoCjVFFbFYlClfZMvqtmUbpiwZYjTtwrzypwMaeHYYSMfrnSwJBJwGyIhqrXthOjWQoqNMENUpBdTPRIenopkinaAYmubuDoTRllVyUCIWixGHySH(self):
        SzjFBnkltXHwdfggqdFkJqUqxAyvyFJGdaUHKrcAeCPNcGHlPCcvENSKDpMQAdhhwMSkFAISFpYnKfhLMCWKScHjycaGQIVgIjDHAgehzrfGnRNtcTnaYdXZgLFzEuEP = self.xgzcXUtGfcQoXfcnZSkXveLvaMHykIFbNYyxoEgMQmKwCWWOEQFonEKVODCyweForDIlvzurrcHkQEPmelbQiOCQFkUaiXVzZrkLaIYzowIPqsClBBGxOxgkcGiwAlqY()
        print(b26f3d88758edd5a54178fc2af040f47020e905f2fc7f24e543a4aa517349577b4709301ce4cb8fc824aa9415ba6d7b4a93f70f400c10d12a9771a8c10d448296('bG9jYWwg') + self.package_name + " : " + str(SzjFBnkltXHwdfggqdFkJqUqxAyvyFJGdaUHKrcAeCPNcGHlPCcvENSKDpMQAdhhwMSkFAISFpYnKfhLMCWKScHjycaGQIVgIjDHAgehzrfGnRNtcTnaYdXZgLFzEuEP))
        VCWyFlGyZPlYvaUeJCAONgEfbyCkYHENbJxHAlKNPSGRiyCfhWbxQTXQRUSRokyoIkpduSmQeGQhkPwBWraDZajVPDVTiosiXjYobWiNdKLofWxtTtLzDqCIcipWPsuW = self.rIhoLszWvwvnqqvtGjfaZWrvSMjYmntVWBTArrFWRKdSDcCcAlthugSZarFjhqXRYGGbUNpstIdelJHrnZAaxXvjUBywMGZmDqFglCoomaymYhUDcqdEpRViGjAdThtd()
        print(b26f3d88758edd5a54178fc2af040f47020e905f2fc7f24e543a4aa517349577b4709301ce4cb8fc824aa9415ba6d7b4a93f70f400c10d12a9771a8c10d448296('Z2l0IA==') + self.package_name + " : " + str(VCWyFlGyZPlYvaUeJCAONgEfbyCkYHENbJxHAlKNPSGRiyCfhWbxQTXQRUSRokyoIkpduSmQeGQhkPwBWraDZajVPDVTiosiXjYobWiNdKLofWxtTtLzDqCIcipWPsuW))
        if SzjFBnkltXHwdfggqdFkJqUqxAyvyFJGdaUHKrcAeCPNcGHlPCcvENSKDpMQAdhhwMSkFAISFpYnKfhLMCWKScHjycaGQIVgIjDHAgehzrfGnRNtcTnaYdXZgLFzEuEP != VCWyFlGyZPlYvaUeJCAONgEfbyCkYHENbJxHAlKNPSGRiyCfhWbxQTXQRUSRokyoIkpduSmQeGQhkPwBWraDZajVPDVTiosiXjYobWiNdKLofWxtTtLzDqCIcipWPsuW:
            print(b26f3d88758edd5a54178fc2af040f47020e905f2fc7f24e543a4aa517349577b4709301ce4cb8fc824aa9415ba6d7b4a93f70f400c10d12a9771a8c10d448296('dXA='))
            if self.fZeHUjNVWBeHEgWnJtRWTpbnaRoINsydxwlvilKxhbrXjONskpGTcEETMnEyPQWQFSyFEbJJolysOivZOfofjMipVrHOEJLBRNaDwPjlIcyeCWCTOOqemWlmoBYtTKwB():
                if self.vRuNASlXvmREqdrjaykfNFhbyyLyisheCPxWHEmkuCOdYodXPculOfsAhZgQEsGEZnRlvHmfoKHDGwekIDohblKVsSdieRZiAgIWFeTjKfmfoiuFqbBnzYrJZDlZcJeo():
                    oZPZMUVEuyHPAWYtePGBkixgInDhuyybFhknfNfFlBxdfXXpinxVHosDZqjYalThCmpklsRRdCGeAjwcjPVGlLdTxnbeEhoXNnFPAxzbBgzGMRBcLsBEKOODHLMpelCV = self.xgzcXUtGfcQoXfcnZSkXveLvaMHykIFbNYyxoEgMQmKwCWWOEQFonEKVODCyweForDIlvzurrcHkQEPmelbQiOCQFkUaiXVzZrkLaIYzowIPqsClBBGxOxgkcGiwAlqY()
                    print(b26f3d88758edd5a54178fc2af040f47020e905f2fc7f24e543a4aa517349577b4709301ce4cb8fc824aa9415ba6d7b4a93f70f400c10d12a9771a8c10d448296('bm93IA==') + self.package_name + " : " + str(oZPZMUVEuyHPAWYtePGBkixgInDhuyybFhknfNfFlBxdfXXpinxVHosDZqjYalThCmpklsRRdCGeAjwcjPVGlLdTxnbeEhoXNnFPAxzbBgzGMRBcLsBEKOODHLMpelCV))
                    if oZPZMUVEuyHPAWYtePGBkixgInDhuyybFhknfNfFlBxdfXXpinxVHosDZqjYalThCmpklsRRdCGeAjwcjPVGlLdTxnbeEhoXNnFPAxzbBgzGMRBcLsBEKOODHLMpelCV == VCWyFlGyZPlYvaUeJCAONgEfbyCkYHENbJxHAlKNPSGRiyCfhWbxQTXQRUSRokyoIkpduSmQeGQhkPwBWraDZajVPDVTiosiXjYobWiNdKLofWxtTtLzDqCIcipWPsuW:
                        print(b26f3d88758edd5a54178fc2af040f47020e905f2fc7f24e543a4aa517349577b4709301ce4cb8fc824aa9415ba6d7b4a93f70f400c10d12a9771a8c10d448296('c3VjY2Vzcw=='))
                        signal.signal(signal.SIGTERM, YZqdQqtGSbAxRDAQvhPqGJNjuBDuXXWKsCwTAvECEdDoJwBHzvgagckidKlHdYshtWgTTajHUCQKqoKwcTXVWLdlETGIjGcDdyrRaSvHXExiQenrxVgzLbQaFwGlyDLh)
                        signal.signal(signal.SIGINT, YZqdQqtGSbAxRDAQvhPqGJNjuBDuXXWKsCwTAvECEdDoJwBHzvgagckidKlHdYshtWgTTajHUCQKqoKwcTXVWLdlETGIjGcDdyrRaSvHXExiQenrxVgzLbQaFwGlyDLh)
                        os.execv(sys.executable, [b26f3d88758edd5a54178fc2af040f47020e905f2fc7f24e543a4aa517349577b4709301ce4cb8fc824aa9415ba6d7b4a93f70f400c10d12a9771a8c10d448296('cHl0aG9u')] + sys.argv)
        return False
