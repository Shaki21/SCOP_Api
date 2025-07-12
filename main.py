from fastapi import FastAPI, HTTPException
from scop_parser import load_scop_data

app = FastAPI()
scop_data = load_scop_data("scop.txt")


@app.get("/scop/{pdb_id}/{chain}")
def get_scop(pdb_id: str, chain: str):
  key = (pdb_id.lower(), chain.upper())
  if key not in scop_data:
    raise HTTPException(status_code=404, detail="PDB ID and chain not found in SCOP data.")

  return {
    "pdb_id": pdb_id.upper(),
    "chain": chain.upper(),
    "classification": scop_data[key]
  }
