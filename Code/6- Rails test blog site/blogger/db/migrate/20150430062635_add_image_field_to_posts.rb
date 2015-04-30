class AddImageFieldToPosts < ActiveRecord::Migration
  def change
    add_column :posts, :link, :text
  end
end
