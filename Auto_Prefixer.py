##  Auto_Prefix - Python  ##

# We want to prefix each asset with a specific value - found a good list here:
# https://www.tomlooman.com/unreal-engine-naming-convention-guide/

import unreal

# instances of unreal classes
editor_util = unreal.EditorUtilityLibrary()
system_lib = unreal.SystemLibrary()

# prefix mapping
prefix_dict = {
    "Blueprint": "BP_",
    "StaticMesh": "SM_",
    "Material": "M_",
    "MaterialInstanceConstant": "MI_",
    "MaterialFunction": "MF_",
    "ParticleSystem": "PS_",
    "SoundCue": "SC_",
    "SoundWave": "S_",
    "Texture2D": "T_",
    "WidgetBlueprint": "WBP_",
    "MorphTarget": "MT_",
    "SkeletalMesh": "SK_",
    "RenderTarget": "RT",
    "TextureRenderTarget2D": "TRT",
}

# get the selected assets
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
prefixed = 0

for asset in selected_assets:
    # get the class instance and the clear text name
    asset_name = system_lib.get_object_name(asset)  # asset.get_fname doesn't work
    # have to use system library to get the actual string instead of an object that .get_fname gives

    asset_class = asset.get_class()
    class_name = system_lib.get_class_display_name(asset_class)  # will give us the clear text name for the class

    # get the prefix for the given class
    class_prefix = prefix_dict.get(class_name, None)

    if class_prefix is None:
        unreal.log_warning("No mapping for asset {} of type {}".format(asset_name, class_name))
        continue

    if not asset_name.startswith(class_prefix):
        # rename the asset and add prefix
        new_name = class_prefix + asset_name
        editor_util.rename_asset(asset, new_name)
        prefixed += 1
        unreal.log("Prefixed {} of type {} with {}".format(asset_name, class_name, class_prefix))

    else:
        unreal.log("Asset {} of type {} is already prefixed with {}".format(asset_name, class_name, class_prefix))

unreal.log("Prefixed {} of {} assets".format(prefixed, num_assets))
