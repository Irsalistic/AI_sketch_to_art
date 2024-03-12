from shared import *

router = APIRouter()
expected_keys_sketch = ["XsGCpFOxHZlCOptSiCNKOgS1sxRMSxy5"]


@router.post("/sketch")
async def sketch(key: str = Form(...), image: UploadFile = File(...), prompt: str = Form(...)):
    if key is None or key not in expected_keys_sketch:
        raise HTTPException(status_code=401, detail="Unauthorized key")

    image_data = await image.read()
    image = Image.open(BytesIO(image_data))
    image = resize_image(image)

    x, y = image.size

    roop_bytes = BytesIO()
    image.save(roop_bytes, format='PNG')
    img_base64 = base64.b64encode(roop_bytes.getvalue()).decode('utf-8')

    desired_model_name = 'realisticVisionV60B1_v51VAE'
    check_and_set_model(desired_model_name)

    prompt = f'HDR photo of {prompt}. High dynamic range, vivid, rich details, clear shadows and highlights, realistic, intense, enhanced contrast, highly detailed'
    negative_prompt = "flat, low contrast, oversaturated, underexposed, overexposed, blurred, noisy"

    controlnet_args = [
        {
            "input_image": img_base64,
            "controlnet_type": "Lineart",
            "model": "control_v11p_sd15_lineart [43d4be0d]",
            "module": "lineart_standard (from white bg & black line)",
            "weight": 1.3,
            "resize_mode": "Crop and Resize",
            "lowvram": False,
            "processor_res": 512,
            "guidance_start": 0,
            "guidance_end": 1,
            "guessmode": False,
            "pixel_perfect": False,
        }
    ]

    result = api.img2img(
        images=[image],
        prompt=prompt,
        negative_prompt = negative_prompt,
        sampler_name="DPM++ 2M Karras",
        steps=25,
        width=x,
        height=y,
        seed=-1,
        cfg_scale=7,
        alwayson_scripts={
            "controlnet": {"args": controlnet_args}
        },
    )

    buffered = BytesIO()
    result.image.save(buffered, format="PNG")
    buffered.seek(0)

    return Response(content=buffered.getvalue(), media_type="image/png")





