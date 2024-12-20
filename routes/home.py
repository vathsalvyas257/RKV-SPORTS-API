from fastapi import APIRouter, File, UploadFile, Form
from controllers.home_controller import Blocks

app = APIRouter(tags=['Home'])

@app.post("/",summary = "creates the block")
async def create_block(block_name : str = Form(...),block_content : str = Form(...),block_image : UploadFile = File(...)) :
    """An API EndPoint to create blocks"""
    return await Blocks.create_block(block_name ,block_content,block_image )

@app.get("/",summary="fetches all blocks")
async def get_all_blocks():
    """An API EndPoints to fetch all blocks"""
    return await Blocks.get_all_blocks()

@app.get("/{block_name}",summary="fetches block by name")
async def get_block_byname(block_name: str) :
    """An API EndPoint to fetch block by name."""
    return await Blocks.get_block_byname(block_name)

@app.put("/",summary = "updates the blocks")
async def update_block(block_name: str, block_content:str):
    """An API EndPoint to update the block."""
    return await Blocks.update_block(block_name,block_content)

@app.put("/update_block_image",summary = "updates the cover image of the block")
async def update_block_image(block_name : str = Form(...),block_image : UploadFile = File(...)):
    """An API EndPoint to update the cover image of the block"""
    return await Blocks.update_block_image(block_name,block_image)

@app.delete("/",summary="deletes the blocks")
async def delete_block(block_name: str):
    """An API EndPoint to delete the blocks."""
    return await Blocks.delete_block(block_name)