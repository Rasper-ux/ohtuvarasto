import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_uuden_varaston_tilavuus_0(self):
        self.varasto_tilavuus_0 = Varasto(0)

        self.assertEqual(self.varasto_tilavuus_0.tilavuus, 0)

    def test_saldo_0_kun_annetaan_saldoksi_pienempää_kuin_0(self):
        self.varasto2 = Varasto(10, -4)

        self.assertEqual(self.varasto2.saldo, 0)

    def test_alkusaldo_yli_tilavuuden(self):
        self.varasto3 = Varasto(1, 5)

        self.assertEqual(self.varasto3.saldo, 1)

    def test_lisays_alle_0(self):
        self.varasto.lisaa_varastoon(-2)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisataan_varastoon_liikaa(self):
        self.varasto.lisaa_varastoon(15)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_otetaan_varastosta_alle_0(self):
        maara = self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(maara, 0.0)

    def test_otetaan_varastosta_yli_saldon(self):
        self.varasto.lisaa_varastoon(5)
        otto = self.varasto.ota_varastosta(7)

        self.assertAlmostEqual(otto, 5)

    def test_tulostus(self):
        self.assertAlmostEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")