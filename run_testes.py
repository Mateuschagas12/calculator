# Python run_testes.py
import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    start_dir = 'test'  # diretório onde estão os arquivos de teste
    suite = loader.discover(start_dir)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)