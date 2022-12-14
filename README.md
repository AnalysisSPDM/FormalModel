# Formal Analysis of SPDM

This repository contains all models of the 
'Formal Analysis of SPDM: Security Protocol and Data Model version 1.2'
paper

----------

## Tamarin

In our analysis we used the latest version of the [tamarin provers develop branch](https://github.com/tamarin-prover/tamarin-prover)


```
tamarin-prover 1.7.1, (C) David Basin, Cas Cremers, Jannik Dreier, Simon Meier, Ralf Sasse, Benedikt Schmidt, ETH Zurich 2010-2020
Git revision: dc65c788da9b920a0f40122e810785399dd40e43, branch: develop
Compiled at: 2022-10-11 21:15:25.006329019 UTC

This program comes with ABSOLUTELY NO WARRANTY. It is free software, and you
are welcome to redistribute it according to its LICENSE, see
https://github.com/tamarin-prover/tamarin-prover/blob/master/LICENSE.
```


You can find detailed installation instructions [here](https://tamarin-prover.github.io/manual/book/002_installation.html)

## Models

All files include models of device initialization and VCA

- **device_attestation.spthy**: model up to the key exchange including runtime responder authentication and measurements
- **preshared_pk_auth/fs.spthy**: model with focus on the key exchange and sessions using preshared public keys
- **key_exchange_auth.spthy**: model with focus on the key exchange and sessions using certificate based public keys
- **preshared_psk_refl.spthy**: model with focus on the key exchange and sessions using preshared symmetric keys that allows reflection
- **preshared_psk_auth.spthy**: model with focus on the key exchange and sessions using preshared symmetric keys that disallows reflection


## Running the Models

To install all dependencies on Ubuntu for the tamarin_wrapper.py file, run

```
apt-get install python3
apt-get install python3-pip
pip3 install tabulate matplotlib
```


------

To run all tamarin models with all lemmas, execute


`python3 tamarin_wrapper.py -f case_studies.tamjson`




All results can be found as .csv files in the 'results' folder.

All models were run on a machine with strong computation power (refer to paper for details)

Depending on your machine, not all results may terminate immediatly for the given timeout. Either increase the integer of the timeout field in

`case_studies.tamjson`

file or run the single lemmas using


`tamarin-prover --prove=LEMMA_NAME FILENAME -D=Sanity -D=Auth -D=Secrecy -D=fs -D=fast`


To compute the proofs for forward secrecy, run

```
time tamarin-prover --prove=ForwardSecrecyInitMaster preshared_pk_fs.spthy -D=oracle -D=fs
time tamarin-prover --prove=ForwardSecrecyRespMaster preshared_pk_fs.spthy -D=oracle -D=fs
```

### Stored proofs

For some reachabilty/sanity lemmas in the 'key_exchange_auth.spthy' file, automatic proofs were only possible using Tamarins 'C' heuristic which takes a long time. We hence excluded those sanity traces from the model. For completion, you can find the stored proofs in the 'stored_proofs' folder in this repository

