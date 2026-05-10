def complex_mtext_renderer(ctx: RenderContext, backend: BackendInterface, mtext: MText, properties: Properties) -> None:
    cmr = ComplexMTextRenderer(ctx, backend, properties)
    align = tl.LayoutAlignment(mtext.dxf.attachment_point)
    layout_engine = cmr.layout_engine(mtext)
    layout_engine.place(align=align)
    layout_engine.render(mtext.ucs().matrix)