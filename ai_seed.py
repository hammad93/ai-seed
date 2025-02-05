
import tpm2_pytss as tpm
import numpy as np

class AISeed:
    """A class for generating random numbers using TPM 2.0 (TRNG) or PRNG with seed for reproducibility.
    
    Attributes:
        seed (int, optional): Seed for PRNG reproducibility. If None, uses TPM (TRNG).
        verbose (bool): If True, prints messages when TPM is used.
    """
    
    def __init__(self, seed=None, verbose=False):
        """Initialize the AISeed instance.
        
        Args:
            seed (int, optional): Seed for reproducible PRNG. Defaults to None (TRNG).
            verbose (bool, optional): Print TPM usage messages. Defaults to False.
        """
        self.seed = seed
        self.verbose = verbose
        self.rng = None
        if self.seed is not None:
            self.rng = np.random.RandomState(seed)
    
    def set_seed(self, seed):
        """Set the seed for PRNG reproducibility.
        
        Args:
            seed (int): The seed value to use for PRNG.
        """
        self.seed = seed
        self.rng = np.random.RandomState(seed)
    
    def get_random_bytes(self, n_bytes):
        """Generate random bytes using TPM (TRNG) if seed is not set, otherwise use PRNG.
        
        Args:
            n_bytes (int): Number of bytes to generate.
            
        Returns:
            bytes: The generated random bytes.
        """
        if self.seed is not None:
            # Generate random bytes using PRNG
            random_numbers = self.rng.randint(0, 256, n_bytes, dtype=np.uint8)
            return random_numbers.tobytes()
        else:
            # Generate true random bytes using TPM
            if self.verbose:
                print("Using TPM to generate true random number.")
            esapi = tpm.ESAPI()
            result = esapi.get_random(n_bytes)
            esapi.close()
            return bytes(result)