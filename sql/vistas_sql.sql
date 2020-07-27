select CONCAT(dt.id,pro.codigo_producto,pro.codigo_distribuidor,"'",pro.nombre_producto,"','",pro.tipo_venta_producto,"','",tipo_presentacion,"','",dt.cantidad_existencias,"','",dt.cantidad_existencias_blister,"','",dt.cantidad_existencias_unidades) from productos pro 
inner join proveedors prv on pro.fk_id_proveedor = prv.id
inner join departamentos dep on dep.id = pro.fk_id_departamento
inner join detalle_inventarios dt on dt.fk_id_producto = pro.id
inner join sedes sd on sd.id = dt.fk_id_sede
where sd.nombre_sede  = "EMFASUR"

    $p=DB::select('select CONCAT('."'".'pro.codigo_producto,'."','".',pro.codigo_distribuidor,'."','".',pro.nombre_producto,'."','".',pro.tipo_venta_producto,.'."','".',tipo_presentacion,'."','".',dt.cantidad_existencias,'."','".',dt.cantidad_existencias_blister,'."','".',dt.cantidad_existencias_unidades) from productos pro 
inner join proveedors prv on pro.fk_id_proveedor = prv.id
inner join departamentos dep on dep.id = pro.fk_id_departamento
inner join detalle_inventarios dt on dt.fk_id_producto = pro.id
inner join sedes sd on sd.id = dt.fk_id_sede
where sd.nombre_sede  = "EMFASUR"
     ');


     'select CONCAT('pro.codigo_producto,',',pro.codigo_distribuidor,',',pro.nombre_producto,',',pro.tipo_venta_producto,.',',tipo_presentacion,',',dt.cantidad_existencias,',',dt.cantidad_existencias_blister,',',dt.cantidad_existencias_unidades) from productos pro inner join proveedors prv on pro.fk_id_proveedor = prv.id inner join departamentos dep on dep.id = pro.fk_id_departamento inner join detalle_inventarios dt on dt.fk_id_producto = pro.id inner join sedes sd on sd.id = dt.fk_id_sede where sd.nombre_sede = "EMFASUR"'